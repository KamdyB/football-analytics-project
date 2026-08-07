"""
football_utils.py

Reusable functions for cleaning and analyzing football data pulled from
FBref via soccerdata. Scalar functions (goals_per90, goal_contribution, etc.)
work on single values OR whole pandas Series, since pandas division is
vectorized. The add_*(df) functions call these scalar functions rather than
re-implementing the same math, so there is one source of truth per metric.
"""

import pandas as pd


# ---------------------------------------------------------------------------
# Header cleaning
# ---------------------------------------------------------------------------

def combine_fbref_headers(df):
    """
    FBref exports multi-row headers (top/middle/bottom category labels).
    This flattens them into a single clean row of column names, preferring
    the most specific (bottom) label available for each column.
    """
    if df.shape[0] < 3:
        raise ValueError(
            f"Expected at least 3 header rows before data starts, got {df.shape[0]} rows total."
        )

    header1 = df.iloc[0]
    header2 = df.iloc[1]
    header3 = df.iloc[2]
    new_column_names = []

    for col in range(df.shape[1]):
        top = header1[col]
        middle = header2[col]
        bottom = header3[col]
        if pd.notna(bottom):
            name = bottom
        elif pd.notna(middle):
            name = middle
        elif pd.notna(top):
            name = top
        else:
            name = f'column_{col}'
        name = (
            str(name)
            .strip()
            .lower()
            .replace(' ', '_')
            .replace('g+a-pk', 'g_and_a_nonpk')
            .replace('g-pk', 'g_nonpk')
            .replace('g+a', 'g_and_a')
        )
        new_column_names.append(name)

    clean_data = df.iloc[3:].copy()
    clean_data.columns = new_column_names
    clean_data.reset_index(drop=True, inplace=True)
    return clean_data


# ---------------------------------------------------------------------------
# Scalar / vectorized metric functions
# (each works on single numbers or whole pandas Series)
# ---------------------------------------------------------------------------

def calculate_goal_difference(goals_for, goals_against):
    return goals_for - goals_against


def calculate_player_age(year_born, current_year):
    age = current_year - year_born
    return age


def find_highest_goals(goals):
    if len(goals) == 0:
        raise ValueError("Cannot find highest goals from an empty list.")
    return max(goals)


def calculate_avg_goals(goals):
    if len(goals) == 0:
        raise ValueError("Cannot calculate average goals from an empty list.")
    return sum(goals) / len(goals)


def classify_team_attack(goals):
    if goals >= 80:
        return 'Elite Attack'
    elif goals >= 60:
        return 'Strong Attack'
    elif goals >= 40:
        return 'Average Attack'
    else:
        return 'Weak Attack'


def calculate_points(wins, draws):
    return wins * 3 + draws


def minutes_per_90(minutes_played):
    return minutes_played / 90.0


def player_age_group(age):
    if age < 0:
        raise ValueError('Age cannot be negative!')
    elif age < 21:
        return 'Young Talent'
    elif age <= 28:
        return 'Prime Years'
    else:
        return 'Experienced'


def goal_contribution(goals, assists):
    return goals + assists


def goals_per90(goals, ninetys):
    """
    ninetys must be > 0 (a player's "90s played" count). Raises ValueError
    on zero rather than silently returning inf, since a scouting stat of
    'inf goals per 90' is a red flag, not a real value.
    """
    if pd.Series(ninetys).eq(0).any():
        raise ValueError("Cannot calculate goals per 90 when ninetys is 0.")
    return goals / ninetys


def assists_per90(assists, ninetys):
    if pd.Series(ninetys).eq(0).any():
        raise ValueError("Cannot calculate assists per 90 when ninetys is 0.")
    return assists / ninetys


def minutes_per_match(minutes, matches):
    if pd.Series(matches).eq(0).any():
        raise ValueError("Cannot calculate minutes per match when matches is 0.")
    return minutes / matches


def goal_involvement_percentage(goal_contribution_total, matches):
    if pd.Series(matches).eq(0).any():
        raise ValueError("Cannot calculate goal involvement percentage when matches is 0.")
    return (goal_contribution_total / matches) * 100


# ---------------------------------------------------------------------------
# DataFrame wrappers
# Each of these adds one column, and calls the scalar function above rather
# than re-implementing the calculation; one source of truth per metric.
# ---------------------------------------------------------------------------

def _require_columns(df, columns):
    missing = [c for c in columns if c not in df.columns]
    if missing:
        raise KeyError(f"Missing expected column(s): {missing}")


def add_goal_contribution(df):
    _require_columns(df, ['gls', 'ast'])
    df['goal_contribution'] = goal_contribution(df['gls'], df['ast'])
    return df


def add_goals_per90(df):
    _require_columns(df, ['gls', '90s'])
    df['goals_per90'] = goals_per90(df['gls'], df['90s'])
    return df


def add_assists_per90(df):
    _require_columns(df, ['ast', '90s'])
    df['assists_per90'] = assists_per90(df['ast'], df['90s'])
    return df


def add_goal_involvement_percentage(df):
    _require_columns(df, ['goal_contribution', 'matches'])
    df['goal_involvement_percentage'] = goal_involvement_percentage(
        df['goal_contribution'], df['matches']
    )
    return df


# ---------------------------------------------------------------------------
# Team report
# ---------------------------------------------------------------------------

def team_report(players, goals, assists, passes):
    """
    Builds a plain-text team summary. Validates that all input lists are
    the same length and non-empty before doing any calculation, since a
    mismatched-length input here would silently produce a wrong report
    rather than an obvious error.
    """
    lengths = {len(players), len(goals), len(assists), len(passes)}
    if len(lengths) != 1:
        raise ValueError(
            f"players, goals, assists, and passes must be the same length. "
            f"Got lengths: players={len(players)}, goals={len(goals)}, "
            f"assists={len(assists)}, passes={len(passes)}."
        )
    if len(players) == 0:
        raise ValueError("Cannot generate a team report with no players.")

    total_goals = total_assists = total_passes = 0
    top_scorer, highest_goal = players[0], goals[0]
    top_assister, highest_assist = players[0], assists[0]
    top_passer, highest_pass = players[0], passes[0]
    highest_contributor = players[0]
    highest_contributor_goals = goals[0]
    highest_contributor_assists = assists[0]
    highest_contribution = goals[0] + assists[0]

    for player, goal, assist, pass_count in zip(players, goals, assists, passes):
        total_goals += goal
        total_assists += assist
        total_passes += pass_count
        current_contribution = goal + assist

        if goal > highest_goal:
            highest_goal, top_scorer = goal, player
        if assist > highest_assist:
            highest_assist, top_assister = assist, player
        if pass_count > highest_pass:
            highest_pass, top_passer = pass_count, player
        if current_contribution > highest_contribution:
            highest_contribution = current_contribution
            highest_contributor_goals = goal
            highest_contributor_assists = assist
            highest_contributor = player

    num_players = len(players)
    report_lines = [
        "====================",
        "TEAM REPORT",
        "====================",
        f"Players Analysed: {num_players}",
        "",
        f"Total Goals: {total_goals}",
        f"Total Assists: {total_assists}",
        f"Total Passes: {total_passes}",
        "",
        f"Average Goals: {total_goals / num_players:.2f}",
        f"Average Assists: {total_assists / num_players:.2f}",
        f"Average Passes: {total_passes / num_players:.2f}",
        "",
        f"Top Scorer: {top_scorer} ({highest_goal} goals)",
        f"Top Assister: {top_assister} ({highest_assist} assists)",
        f"Top Passer: {top_passer} ({highest_pass} passes)",
        "",
        f"Top Match Contributor: {highest_contributor} "
        f"with {highest_contributor_goals} goals, "
        f"{highest_contributor_assists} assists, "
        f"and {highest_contribution} total contribution.",
    ]
    return "\n".join(report_lines)

def count(data):
    counter = 0
    for value in data:
        counter += 1
    return counter

def calculate_mean(data):
    total = 0
    if len(data) == 0:
       raise ValueError("Cannot calculate mean of an empty dataset.")
    for value in data:
        total += value
    return total / count(data)

def calculate_median(data):
    if count(data) == 0:
        raise ValueError("Cannot calculate mean of an empty dataset.")
    sorted_data = sorted(data)
    middle = count(data)//2
    return sorted_data[middle]

def calculate_range(data):
    if count(data) == 0:
        raise ValueError("Cannot calculate mean of an empty dataset.")
    maximum = max(data)
    minimum = min(data)
    return maximum - minimum

def calculate_variance(data):
    if count(data) == 0:
       raise ValueError("Cannot calculate mean of an empty dataset.")
    mean = calculate_mean(data)
    total = 0
    for value in data:
        difference = value - mean
        total += difference ** 2
    return total / count(data)

def calculate_standard_deviation(data):
    if count(data) == 0:
        raise ValueError("Cannot calculate mean of an empty dataset.")
    variance = calculate_variance(data)
    return variance ** 0.5

def find_min(data):
    minimum = data[0]
    for value in data:
        if value < minimum:
            minimum = value
    return minimum

def find_max(data):
    maximum = data[0]
    for value in data:
        if value > maximum:
            maximum = value
    return maximum

def calculate_z_score(value, data):
    mean = calculate_mean(data)
    standard_deviation = calculate_standard_deviation(data)
    if standard_deviation == 0:
        raise ValueError('Cannot calculate Z Score when standard deviation equals 0')
    difference = value - mean
    return difference / standard_deviation

def add_goal_z_score(df):
    _require_columns(df, ['gls'])
    df['goal_z_score'] = [
        calculate_z_score(goal, df['gls'])
        for goal in df['gls']]

    return df


import pandas as pd


def combine_fbref_headers(df):
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



def calculate_goal_difference(goals_for, goals_against):
    return goals_for - goals_against


def calculate_player_age(year_born, current_year):
    age = current_year - year_born
    return age


def find_highest_goals(goals):
    highest_goal = max(goals)
    return highest_goal


def calculate_avg_goals(goals):
    avg_goals = sum(goals)/len(goals)
    return avg_goals


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
    points = wins*3 + draws
    return points


def minutes_per_90(minutes_played):
    mins_per90 = minutes_played/90.0
    return mins_per90


def player_age_group(age):
    if age < 0:
        raise ValueError('Age cannot be negative!')
    elif age < 21:
        return 'Young Talent'
    elif age <= 28:
        return 'Prime Years'
    else:
        return 'Experienced'


def team_report(players, goals, assists, passes):
    total_goals = 0
    total_assists = 0
    total_passes = 0

    highest_goal = goals[0]
    top_scorer = players[0]
    highest_assist = assists[0]
    top_assister = players[0]
    highest_pass = passes[0]
    top_passer = players[0]

    highest_contributor = players[0] 
    highest_contributor_goals = goals[0]
    highest_contributor_assists = assists[0]
    highest_contribution = goals[0] + assists[0]
    current_contribution = 0

    for player, goal, assist, pass_count in zip(players, goals, assists, passes):
        total_goals += goal
        total_passes += pass_count
        total_assists += assist
        current_contribution = goal + assist
        if goal > highest_goal:
            highest_goal = goal
            top_scorer = player
        if assist > highest_assist:
            highest_assist = assist
            top_assister = player
        if pass_count > highest_pass:
            highest_pass = pass_count
            top_passer = player
        if current_contribution > highest_contribution:
            highest_contribution = current_contribution
            highest_contributor_goals = goal
            highest_contributor_assists = assist
            highest_contributor = player
    team_report_card = ['==================','\nTEAM REPORT', '\n================',
    '\nPlayers Analysed: ', len(players), '\n'
    '\nTotal Goals: ', total_goals,
    '\nTotal Assists: ', total_assists,
    '\nTotal Passes: ', total_passes, '\n',
    '\nAverage Goals: ', total_goals/len(players),
    '\nAverage Assists: ', total_assists/len(players),
    '\nAverage Passes: ', total_passes/len(players), '\n',
    '\nTop Scorer: ', top_scorer, (highest_goal),
    '\nTop Assister: ', top_assister, (highest_assist),
    '\nTop Passer: ', top_passer, (highest_pass), '\n',
    '\nTop Match Contributor: ', highest_contributor, 'with ', highest_contributor_goals, 'goals, ', highest_contributor_assists, 'assists and ', highest_contribution, 'contribution.']
    return team_report_card

def goal_contribution(goals, assists):
    return goals + assists


def goals_per90(goals, ninetys):
    return goals / ninetys

def minutes_per_match(minutes, matches):
    return minutes / matches

def add_goal_contribution(df):
    df['goal_contribution'] = (df['gls'] + df['ast'])
    return df

def add_goals_per90(df):
     df['goals_per90'] = (df['gls'] / df['90s'])
     return df

def assists_per90(df):
    df['assists_per90'] = (df['ast'] / df['90s'])
    return df

def goal_involvement_percentage(df):
    df['goal_involvement_percentage'] = ((df['goal_contribution'] / df['matches']) * 100)
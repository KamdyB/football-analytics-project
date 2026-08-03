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


def clean_column_names(column):
    column = column.strip()
    column = column.replace(' ', '_')
    column = column.lower()
    return column

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



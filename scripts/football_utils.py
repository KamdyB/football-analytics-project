def calculate_goal_difference(goals_for, goals_against):
    return goals_for - goals_against


def calculate_player_age(year_born, current_year):
    age = current_year - year_born
    return age


goals = [75, 68, 81, 59]

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


 


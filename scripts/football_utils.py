def calculate_goal_difference(goals_for, goals_against):
    goal_diff = goals_for - goals_against
    return goal_diff
print(calculate_goal_difference(34, 20))


def calculate_player_age(year_born, current_year):
    age = current_year - year_born
    return age
print(calculate_player_age(2009, 2026))


def clean_column_name(column_name):
    column_name = column_name.lower()
    column_name = column_name.replace(' ', '_')
    return column_name
print(clean_column_name('Minutes PLayed'))


goals = [75, 68, 81, 59]

def find_highest_goals(goals):
    highest_goal = max(goals)
    return highest_goal
print(find_highest_goals(goals))

def calculate_avg_goals(goals):
    avg_goals = sum(goals)/len(goals)
    return avg_goals
print(calculate_avg_goals(goals))


def classify_team_attack(goals):
    if goals >= 80:
        return 'Elite Attack'
    elif goals >= 60:
        return 'Strong Attack'
    elif goals >= 40:
        return 'Average Attack'
    else:
        return 'Weak Attack'
print(classify_team_attack(81))
print(classify_team_attack(67))
print(classify_team_attack(52))
print(classify_team_attack(31))



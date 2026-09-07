def form_points(form):
    points = 0

    for result in form:
        if result == "W":
            points += 3
        elif result == "D":
            points += 1

    return points

def get_team_data():
    team_name = input("Enter team name: ")

    team_form = input("Enter team's last 5 results (W/D/L): ")

    team_form_score = form_points(team_form) / 15 * 100

    team_value = float(input("Enter team's squad value (in millions): "))

    team_value_score = min(team_value / 10, 100)
   
    if team_value <= 0:
        print("Squad value must be greater than 0.")

    home_advantage = input("Is the team playing at home? (yes/no): ").lower()

    if home_advantage == "yes":
        home_advantage = 15
    
    elif home_advantage == "no":
        home_advantage = 0

    last_h2h = input("Enter last head-to-head result against the opponent (W/D/L): ")

    if last_h2h == "W":
        last_h2h = 15

    elif last_h2h == "D":
        last_h2h = 7.5

    else:
        last_h2h = 0
    
    total_score = (team_form_score * 0.4) + (team_value_score * 0.3) + (home_advantage) + (last_h2h)

    return team_name, total_score

team1 = get_team_data()
team2 = get_team_data()

difference = abs(team1[1] - team2[1])

draw_probability = max(0.15, 0.27 - difference / 700)

remaining_probability = 1 - draw_probability

team1_probability = (team1[1] / (team1[1] + team2[1])) * remaining_probability
team2_probability = (team2[1] / (team1[1] + team2[1])) * remaining_probability

team1_odds = round(1 / team1_probability, 2)
draw_odds = round(1 / draw_probability, 2)
team2_odds = round(1 / team2_probability, 2)

print(f"\n {team1[0]}: {team1_odds}")
print(f"Draw: {draw_odds}")
print(f"{team2[0]}: {team2_odds}")



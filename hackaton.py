# Desenvolva seu código abaixo
hackathon_1 = ["Team Kenzie", "Team Ateliware", "Team VHSYS", "Team Mirum"]
hackathon_2 = ["Team Ateliware", "Team Kenzie", "Team VHSYS", "Team Mirum"]
hackathon_3 = ["Team Mirum", "Team Ateliware","Team VHSYS", "Team Kenzie"]


def get_score(team_name, teams):
    score = teams.index(team_name) + 1
    return f"A {team_name} ficou classificada em {score}"


if __name__ == "__main__":
    score_1 = get_score("Team Ateliware", hackathon_1)
    print(score_1) # A Team Ateliware ficou classificada em 2
    score_2 = get_score("Team Kenzie", hackathon_1)
    print(score_2) # A Team Kenzie ficou classificada em 1
    score_3 = get_score("Team Mirum", hackathon_3)
    print(score_3) # A Team Mirum ficou classificada em 1

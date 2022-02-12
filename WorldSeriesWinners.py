team_wins = {}
year_wins = {}
infile = open("WorldSeriesWinners.txt", "r")
win_file = infile.read()
year = 1903
for team in win_file.splitlines():
    if team not in team_wins:
        team_wins[team] = 1
    elif team in team_wins:
        team_wins[team] += 1
    year_wins[year] = team
    year += 1
    if year in [1904, 1994]:
        year += 1

result = int(input("Choose a year in between 1903 and 2008: "))
while result == 1904 or result == 1994:
    print("The World Series was not played in", result)
    result = int(input("Choose a year in between 1903 and 2008: "))
print(
    "The winner of the",
    result,
    "World Series was the",
    year_wins[result],
    "who have won the World Series",
    team_wins[year_wins[result]],
    "times.",
)
infile.close()

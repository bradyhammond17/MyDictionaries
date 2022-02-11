team_wins = {}
infile = open("WorldSeriesWinners.txt", "r")
win_file = infile.read()

for line in win_file:
    print(line, end="")
print(team_wins)

# r - read mode, 
# other modes - w = write, a= append, 
lineup_file = open("lineup.txt","r")

for player in lineup_file.readlines():
    print(player, end="")

# print(lineup_file.readlines())


lineup_file.close()
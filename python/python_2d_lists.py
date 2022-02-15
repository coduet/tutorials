lineup = [
    ["Courtois"],
    ["Cravajal","Militao","Alaba","Mendy"],
    ["Kroos","Casemiro","Modric"],
    ["Asensio","Benzema","Vini"]
]

def print_line_diff():
    for i in range(30):
        print("#", end="")
    print()

print_line_diff()
print("Team Line up today :")

print(*lineup[0])
print(*lineup[1])
print(*lineup[2])
print(*lineup[3])

print_line_diff()
print("Team Line up today :")

for i in range(len(lineup)):
    for j in range(len(lineup[i])):
        print(lineup[i][j], end =" ")
    print()

print_line_diff()
print("Team Line up today :")

for depth in lineup :
    for player in depth :
        print(player, end = " "),
    print()

print_line_diff()
print("Team Line up today :")

for depth in lineup :
    print(*depth),
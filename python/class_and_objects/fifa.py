from Player import Player, Defender
from Club import Club

real_madrid = Club()

print(real_madrid.players)
# defender = Defender("Ramos", 4,36,5,6)
real_madrid.add_player(Defender("Ramos", 4,36,5,6))
real_madrid.add_player(Player("Ronaldo", 7,36))
real_madrid.add_player(Player("Modric", 10,34))

for player in real_madrid.players : 
    print(player.name)

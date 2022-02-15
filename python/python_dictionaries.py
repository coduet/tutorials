#key value pair, where every key is unique

jerseys ={
    "Ramos" : 4,
    "Ronaldo" : 7,
    "Benzema" : 9,
    "Modric" : 10,
    "Marcelo" : 12
}

print(jerseys["Ramos"])
print(jerseys.get("Ronaldo"))
print(jerseys.get("Ro","Not a player")) #default value if key is bnot in dicctionary

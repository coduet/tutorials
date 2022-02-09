
# lists are python equivalent of arrays

stars = ["Ramos", "Ronaldo", "Benzema","Modric","Kroos" ] #elements can be same type
print(stars)

types = ["Ramos", 1, False, 4.5 ] #elements can be different types
print(types)

#accessing elements
print(stars[0]) #index from start
print(stars[-1]) #index from back
print(stars[1:4]) #elements in range from i to j-1

#list functions
stars.sort() 
print(stars)
 
stars.append("Marcelo") #add element to end of list 
print(stars)

stars.insert(2, "Casemiro") #insert element at an index
print(stars) 

stars.remove("Casemiro")
print(stars) 


stars.pop() #removes last element of the list. gives error if list empty
print(stars) 
print(stars.index("Ronaldo")) 
print(stars.count("Ronaldo")) 

stars.clear()
print(stars) 

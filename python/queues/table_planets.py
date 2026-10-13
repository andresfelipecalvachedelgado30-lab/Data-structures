#table_planets.py
planets = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"]
gravity=[3.7,8.87,9.81,3.71,24.79,10.44,8.69,11.15]

# print(type(gravity) # #class list
print(planets)
print(len(planets))
print (planets[0])
print (planets[1])
print (planets[2])
print (planets[3])
print (planets[4])
print (planets[5])
print (planets[6])
print (planets[7])


print("_"*39)
print(f"| { "planet name" :<15} |{ "gravity" :<10} |")
print("_"*39)
i = 0

while i <= len(planets)-1:
      print(f"| {planets[i]:<15} | {gravity[i]:<10} |")
      print("_"*39)
      i += 1
      

  






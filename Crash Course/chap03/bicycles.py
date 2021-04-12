bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[1])
print(bicycles[2])
print(bicycles[3])

message = f"My first bicycle was a {bicycles[0].title()}"
print(message)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
motorcycles.insert(1, 'bmw')
print(motorcycles)

#del motorcycles[0]
#print(motorcycles)

#popped_motorcycle = motorcycles.pop()
#print(popped_motorcycle)
#print(motorcycles)

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

too_expensive = "bmw"
motorcycles.remove(too_expensive)
print(f"This {too_expensive.title()} make is too expensive.")


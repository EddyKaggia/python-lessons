# LISTS
# Collection of items in a particular order, kind of like a JavaScript array

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles) # ['trek', 'cannondale', 'redline', 'specialized']

# Accessing elements in a list -> Zero-indexed
print(bicycles[0]) # 'trek'

print(bicycles[0].title()) # 'Trek'

message = f"My first bicycle was a {bicycles[0].title()}."
print(message) # 'My first bicycle was a Trek.'

# MODIFYING, ADDING, AND REMOVING ELEMENTS

# MODIFYING
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) # ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
print(motorcycles) # ['ducati', 'yamaha', 'suzuki']

# ADDING

# Appending -> End of list
motorcycles.append('kawasaki')
print(motorcycles) # ['ducati', 'yamaha', 'suzuki', 'kawasaki']

# Inserting -> To any position using index
motorcycles.insert(0, 'bmw')
print(motorcycles) # ['bmw', 'ducati', 'yamaha', 'suzuki', 'kawasaki']

# REMOVING

# Del
del motorcycles[0]
print(motorcycles) # ['ducati', 'yamaha', 'suzuki', 'kawasaki']

# Pop -> Lets you remove an element and use it afterwards
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# Popping Items from any position in a list -> Use index
first_owned = motorcycles.pop(1)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# Removing an item by value -> remove()
motorcycles.remove('suzuki')
print(motorcycles)


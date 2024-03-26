# SORTING 

# Permanently with sort()
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars) # ['audi', 'bmw', 'subaru', 'toyota']

# Reverse alphabetical order
cars.sort(reverse=True)
print(cars) # ['toyota', 'subaru', 'bmw', 'audi']

# Temporarily with sorted()
cars2 = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars2) 
# Here is the original list:
# ['bmw', 'audi', 'toyota', 'subaru']

print("\nHere is the sorted list:")
print(sorted(cars2))
# Here is the sorted list:
# ['audi', 'bmw', 'subaru', 'toyota']

print("\nHere is the original list again:")
print(cars2)
# Here is the original list again:
# ['bmw', 'audi', 'toyota', 'subaru']

# Length of list -> len()
print(len(cars2)) # 4
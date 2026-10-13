#create a list

mobile_phones = ["iPhone", "Samsung Galaxy", "Google Pixel", "OnePlus", "Nokia"]
mobiles = []
print("List of mobile phones:", mobile_phones)
print("mobiles::",mobiles)
print("Datatype of mobile_phones",type(mobile_phones))

#append
mobiles.append("LG")
print("mobiles::",mobiles)

#extend
mobiles.extend(mobile_phones)
print("mobiles::",mobiles)

#property of list

#insert items in the list
mobiles.insert(1, "Motorola")
mobiles.insert(2, "LAVA")
print("mobiles::",mobiles)

#fetch
print("mobiles @ 0th position::",mobiles[0])

#remove

#mobile_phones.remove("iPhone")

#pop

mobile_phones.pop(1)
print("mobile_phones::",mobile_phones)


#clear

cars = ["baleno","qualis","astart","audi","polo","polo"]

#cars.clear()

print("cars::",cars.index("audi"))


dup = cars.copy()

print("occurences of item polo in dup::",dup.count("polo"))
print(id(dup))
dup.sort()
print("dup sorted::", dup)
print(id(dup))
dup.reverse()
print("dup reversed::", dup)
print(id(dup))


numbers=[10,20,30,40,50]

print(sum(numbers))

colors = ["red","blue","green","orange","yellow"]

# print(sorted(colors))

# print("colors::",colors)
print("checking reversed ")
print(list(reversed(colors)))

del(colors)

#print(colors)


# sliciing example

names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"]
#print(names[0:3])


#print(names[0:10:2])

for name in names:
    print(name)



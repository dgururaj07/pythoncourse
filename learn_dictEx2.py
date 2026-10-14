#write a python program to count the number of occurences of a character in a string and store the count in a dictionary with the character as the key and the count as the value.
txt = input("Enter a string: ")
dt = {}
for i in txt:
   dt[i] = dt.get(i, 0) + 1

print(dt)
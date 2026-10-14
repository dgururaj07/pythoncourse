#write a python program to count the number of occurrences of a character in a string and store the count in a dictionary with the character as the key and the count as the value.
txt = input("Enter a string: ")
ch=input("Enter a character to count: ")
count=0
char_count={}

for i in txt:
    if i==ch:
        count=count+1
        char_count[ch]=count
print("count::",count)
print("char_count::",char_count)


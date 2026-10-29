#String Manipulation
# "value" 'value' -> both are considered as strings
# print() -> displays the given value(s) on the console; \n inside the string moves to a new line
print("Welcome to Python\nnext line check")

# \' -> escape character, lets you use a single quote inside a single-quoted string
print('Welcome to \'Python\'')

# \" -> escape character, lets you use a double quote inside a double-quoted string
print("I don\'t know \"python\"")


# use """value""" to store the value with mutiple lines
txt = """Backend development and process automation engineering for an upcoming pipeline project. This role primarily focuses on building robust Python-based backend services, automated workflows, and data pipelines, while supporting secondary Java microservices architecture Python Development & Automation (Primary):
Design, build, and maintain scalable Python solutions, backend services, and automated data/process pipelines to meet committed deliverables."""

# upper() -> returns a new string with all characters converted to UPPERCASE
print(txt.upper())

# isupper() -> returns True if all cased characters in the string are uppercase, else False
print(txt.upper().isupper())


# lower() -> returns a new string with all characters converted to lowercase
print(txt.lower())

# islower() -> returns True if all cased characters in the string are lowercase, else False
print(txt.lower().islower())

#\n -> newline character, moves the remaining text to the next line

print("Welcome to Python\nnext line check")




#\t -> tab character, inserts a horizontal tab space

print("Welcome to Python\tnext line check")




text1 = "India is great"

# startswith(prefix) -> returns True if the string begins with the given prefix (case-sensitive)
print(text1.startswith('imp'))
# endswith(suffix) -> returns True if the string ends with the given suffix (case-sensitive)
print(text1.endswith('great'))




text2 = "BACKEND DEVELOPMENT AND PROCESS AUTOMATION ENGINEERING FOR AN UPCOMING PIPELINE PROJECT"

# split(sep) -> Return a list of the substrings in the string, using sep as the separator string.
print(text2.split(' '))

x=text2.split(' ')
print(x)

# (method) def join(
#  iterable: Iterable[LiteralString],
#  /
# ) -> LiteralString

# Concatenate any number of strings.

# The string whose method is called is inserted in between each given string. The result is returned as a new string.

# Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'

# join(list) -> joins the list items back into one string with a space between each
joined=" ".join(x)
print(joined)


# join(list) -> joins the list items using "###" as the separator
newJoined="###".join(x)

print(newJoined)



newtxt = "             testing values     at both front and end             "
# strip() -> removes leading and trailing whitespace (spaces in the middle are kept)
# lstrip() removes only from the left, rstrip() only from the right
strip1=newtxt.strip()
print(strip1)


userName = "dgururaj.29"
email = "dgururaj.29@gmail.com"


# f-string -> f"...{variable}..." inserts variable/expression values directly into the string
print(f"Username: {userName} Email: {email}")

# range(1,21) -> generates numbers 1 to 20 (end index is excluded); used here to print the 5 times table
for i in range(1,21):
    print(f"5*{i}={5*i}")

#range(index)
#range(startindex,endindex)
#range(startindex,endindex,step)

mainString = "UseName:gururaj12345 Email:gururaj@vedarsh.com"

# in -> returns True if the substring is present in the string (case-sensitive)
print("name" in mainString)
print("UseName" in mainString)

# not in -> returns True if the substring is NOT present in the string
print("name" not in mainString)


# isalnum() -> returns True only if every character is a letter or digit (no spaces/symbols like : @ .)
print(mainString.isalnum())


x="Test"

y="Leaf"

# indexing & slicing -> y[0] gets the first character, x[1:] gets everything from index 1 to the end
# + concatenates the strings: "L" + "est" -> "Lest"
print(y[0]+x[1:])

t1=y[0]+x[1:]
t2=x[0]+y[1:]

# swaps the first letters: "T" + "eaf" -> "Teaf"
print(x[0]+y[1:])

# + " " + -> joins two strings with a space in between
print(t1 +" "+t2)


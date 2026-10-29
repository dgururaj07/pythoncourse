#String Manipulation
# "value" 'value' -> both are considered as strings 
print("Welcome to Python\nnext line check")

print('Welcome to \'Python\'')

print("I don\'t know \"python\"")


# use """value""" to store the value with mutiple lines
txt = """Backend development and process automation engineering for an upcoming pipeline project. This role primarily focuses on building robust Python-based backend services, automated workflows, and data pipelines, while supporting secondary Java microservices architecture Python Development & Automation (Primary):
Design, build, and maintain scalable Python solutions, backend services, and automated data/process pipelines to meet committed deliverables."""

print(txt.upper())

print(txt.upper().isupper())


print(txt.lower())

print(txt.lower().islower())

#\n

print("Welcome to Python\nnext line check")




#\t 

print("Welcome to Python\tnext line check")




text1 = "India is great"

print(text1.startswith('imp'))
print(text1.endswith('great'))




text2 = "BACKEND DEVELOPMENT AND PROCESS AUTOMATION ENGINEERING FOR AN UPCOMING PIPELINE PROJECT"

#Return a list of the substrings in the string, using sep as the separator string.
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

joined=" ".join(x)
print(joined)


newJoined="###".join(x)

print(newJoined)



newtxt = "             testing values     at both front and end             "
strip1=newtxt.strip()
print(strip1)


userName = "dgururaj.29"
email = "dgururaj.29@gmail.com"


print(f"Username: {userName} Email: {email}") 

for i in range(1,21):
    print(f"5*{i}={5*i}")

#range(index)
#range(startindex,endindex)
#range(startindex,endindex,step)

mainString = "UseName:gururaj12345 Email:gururaj@vedarsh.com"

print("name" in mainString)
print("UseName" in mainString)

print("name" not in mainString)


print(mainString.isalnum())


x="Test"

y="Leaf"

print(y[0]+x[1:])

t1=y[0]+x[1:]
t2=x[0]+y[1:]

print(x[0]+y[1:])

print(t1 +" "+t2)


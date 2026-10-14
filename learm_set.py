###create empty set

s={"guru"}

print(type(s))

# to declare an empty set
s1=set()

print("Type of s1::",type(s1))

#how to intialize a set

a_version = {'pie','marshmellow','nugget','oreo'}
b_version = {'lollipop','kitkat','jelly','bean'}

# a_version.add('lpop')

# print(a_version)


# a_version.update(['banana', 'apple'])

a_version.update(b_version)
#print(a_version)



a_version.remove('pie')
print(a_version)

a_version.discard('pie')
print(a_version)

a_version.pop()
print(a_version)

sorted_set = sorted(a_version)
print("sorted_set::",sorted_set)


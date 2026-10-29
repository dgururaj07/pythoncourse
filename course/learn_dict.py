#intialize the dictionary

android_version = {'pie':9,
                   'marshmellow':10,
                   'nugget':11,
                   'oreo':12}





print("android_version::",android_version)


android_version['pie']
print("android_version['pie']::",android_version['pie'])

android_version.get('pie')
print("android_version.get('pie')::",android_version.get('pie'))


print("android_version.items()::",android_version.items())

print("android_version.items()::",android_version.keys())


print("android_version.items()::",android_version.values())

print("android_version.get('122', 'Not Found')::",android_version.get('122', 'Not Found'))


#print("android_version[123]::",android_version[123])


for i,j in android_version.items():
    print("key::",i)
    print("value::",j)


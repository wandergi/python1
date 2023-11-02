courses = ["MIT", "Cybersecurity", "Data science"]
print(courses)
# Assessing elements in an array
print(courses[0])
print(courses[1])
print(courses[2])
# Looping through an array
for course in courses:
    print(course)
# Adding a element in an array use the method .append
courses.append("Android development")
print(courses)
# Removing an element in an array use the method .remove or using an index
courses.remove("MIT")
print(courses)

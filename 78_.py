person = {"li": 18, "wang": 50, "zhang": 20, "sun": 22}
person = list(person.items())
print(person)
person.sort(key=lambda x: x[1])
print(person[-1])
print(dict(person))



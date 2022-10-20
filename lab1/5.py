person_data = {
    "Ana": 1995,
    "Zoran": 1978,
    "Lucija": 2001,
    "Anja": 1997
}

for i in person_data:
    person_data[i] -= 1

year_age = []
for i in person_data.values():
    year_age.append((i, 2022 - i))

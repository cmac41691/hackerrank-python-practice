N = int(input())

records = []

for _ in range(N):
    name = input()
    grade = float(input())
    records.append([name, grade])


grades = [record[1] for record in records]

 
unique_grades = sorted(set(grades))
second_lowest = unique_grades[1]


names = sorted(
    record[0]
    for record in records
    if record[1] == second_lowest
)


for name in names:
    print(name)

 

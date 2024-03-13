numParts, numDays = map(int, input().split())

parts = []

answer = 0

for i in range(numDays):
    name = input()
    if name not in parts:
        parts.append(name)
    if len(parts) == numParts:
        answer = i + 1
        break

if answer !=0:
    print(answer)
else:
    print("paradox avoided")

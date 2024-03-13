time = input()

display = []
for num in time:
    num = int(num)
    places = []
    for i in range(3, -1, -1):
        places.append("*" if num // 2**i > 0 else ".")
        num = num % 2**i
    display.append(places)

for row in range(len(display)):
    for col in range(len(display[0])):
        if col != 3:
            print(display[col][row], end=" ")
        else:
            print(display[col][row], end="")
        if col == 1:
            print("  ", end="")
    print()
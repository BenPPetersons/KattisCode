s = input()

counts = {
    '': 0,
    'A': 0,
    'B': 0,
    'C': 0,
    'AB': 0,
    'AC': 0,
    'BC': 0
}

paths = {
    'A': ['BC', 'B', 'C', ''],
    'B': ['AC', 'A', 'C', ''],
    'C': ['AB', 'A', 'B', '']
}

combos = {
    'BA': 'AB',
    'CA': 'AC',
    'CB': 'BC',
    'ACB': '',
    'BCA': '',
    'BAC': '',
    'CAB': '',
    'CBA': '',
    'ABC': ''
}

for c in s:
    found = False
    for path in paths[c]:
        if counts[path] > 0:
            found = True
            counts[path] -= 1
            new = path + c
            if new not in counts:
                new = combos[new]
            counts[new] += 1
            break
    if not found:
        counts[c] += 1

print(counts[''])
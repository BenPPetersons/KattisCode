from sys import stdin

m = {}
for line in stdin:
    line = line.strip()
    line = line.split()
    if line[0] == 'define':
        m[line[2]] = int(line[1])
    elif line[0] == 'eval':
        if line[1] in m and line[3] in m:
            res = False
            if line[2] == '<':
                res = m[line[1]] < m[line[3]]
            elif line[2] == '>':
                res = m[line[1]] > m[line[3]]
            elif line[2] == '=':
                res = m[line[1]] == m[line[3]]
            print(str(res).lower())
        else:
            print('undefined')
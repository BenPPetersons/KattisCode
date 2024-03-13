r, c = map(int, input().split())
print(pow(r - 1, c - 1, 998244353)*r%998244353)
n = int(input())
for i in range(0, 2 ** n):
    print(bin(i ^ (i//2))[2:].zfill(n))

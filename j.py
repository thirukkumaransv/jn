v,s=map(int,input().split())
c3=list(map(int,input().split()))
for j in range (0,s):
    c3=[c3[-1]]+c3[:-1]
print(*c3,end='')

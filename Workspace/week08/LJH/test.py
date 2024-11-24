N,M = map(int,input().split())
l = [list(input()) for i in range(N)]
e = []

ex1 = '''BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB'''
Ex1 = []
for i in ex1:
    Ex1.append(i)
ex2 = '''WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW'''
Ex2 = []
for i in ex2:
    Ex2.append(i)

for i in range(0,M-8):
    for j in range(0,N-8):
    
        cnt1 = 0
        cnt2 = 0

        for x in range(i,i+9):
            for y in range(j,j+9):
                if l[i][j] != ex1[i][j]:
                    cnt1 += 1
        e.append(cnt1)
        
        for x in range(i,i+9):
            for y in range(j,j+9):
                if l[i][j] != ex2[i][j]:
                    cnt2 += 1
        e.append(cnt2)

print(min(e))
                
#coding:utf-8
'''
从下面展示的三角形的顶端出发，不断移动到在下一行与其相邻的元素，能够得到的最大路径和是23。

3
7 4
2 4 6
8 5 9 3
如上图，最大路径和为 3 + 7 + 4 + 9 = 23。

求从其顶端出发到达底部，所能够得到的最大路径和
'''
rr = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''


l = [map(int,x.split(' ')) for x in rr.split('\n')]
f = [[0]*len(x) for x in l]
N = 15
##################### Enumerate
# l[i][j]代表当前格的值
# f[i][j]保存到达第i层第j数的最大路径和
for i in xrange(0,N):
    for j in xrange(0,i+1):
        if j == 0: #此行打头第一个数
            if i == 0: #第一步特殊情况
                f[i][j] = l[i][j]
            else:#上一行只能取右边的数的f为基
                f[i][j] = f[i-1][j] + l[i][j]
        elif j == i: #到达此行的最后一个数了，i-1行只能取j-1，因为上一行的数肯定在左边
            f[i][j] = f[i-1][j-1] + l[i][j]
        else:
            f[i][j] = max(f[i-1][j-1],f[i-1][j]) + l[i][j]
max_path = 0
for j in xrange(0,N):
    if f[N-1][j] > max_path:
        max_path = f[N-1][j]
print max_path

##################### Recursion
f = [[0]*len(x) for x in l]
def find_max(i,j):
    if f[i][j] > 0:
        return f[i][j]
    if i == N-1:
        return l[i][j]
    else:
        f[i][j] = l[i][j] + max(find_max(i+1,j),find_max(i+1,j+1))
        return f[i][j]
print find_max(0,0)


        

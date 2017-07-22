#coding:utf-8
'''
从下面展示的三角形的顶端出发，不断移动到在下一行与其相邻的元素，能够得到的最大路径和是23。

3
7 4
2 4 6
8 5 9 3
如上图，最大路径和为 3 + 7 + 4 + 9 = 23。

求从其顶端出发到达底部，所能够得到的最大路径和
注意：这是第18题的强化版。由于总路径一共有299条，穷举每条路经来解决这个问题是不可能的！即使你每秒钟能够检查一万亿（1012）条路径，全部检查完也需要两千万年。存在一个非常高效的算法能解决这个问题。;o)
'''
import time

N = 100
l=[]
with open('067_triangle.txt','r') as f:
    for i in xrange(0,N):
        rr = f.readline()
        l.append(map(int,rr.split(' ')))

###########################
a=time.time()
f = [[0]*len(x) for x in l]
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
print max_path,time.time()-a
##############################
a=time.time()
f = [[0]*len(x) for x in l]
def find_max(i,j):
    if f[i][j] > 0:
        return f[i][j]
    if i == N-1:
        return l[i][j]
    else:
        f[i][j] = l[i][j] + max(find_max(i+1,j),find_max(i+1,j+1))
        return f[i][j]
print find_max(0,0),time.time()-a

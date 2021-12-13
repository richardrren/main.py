#7-7
"""
n = int(input())
data = []
max = 0
k = 0
for i in range(n):
    sum = 0
    data.append(input().split())
    for j in range(2, 5):
        sum += int(data[i][j])
    if sum > max:
        max = sum
        k = i
print(data[k][1], data[k][0], max)
"""

#7-4

# def isp(x):
#     if x == 2: return True
#     if x % 2 == 0 or x == 1: return False
#     n = 3
#     while n * n <= x:
#         if x % n == 0: return False
#         n += 2
#     return True
#
#
#
#
# def gdb(n):
#     if n == 4:
#         print('4=2+2')
#         return
#     for i in range(1, n, 2):
#         if isp(i) and isp(n - i):
#             print("{}={}+{}".format(n, i, n - i), sep='')
#             return
#
#
# n = int(input())
# gdb(n)



# #法二
# n = int(input())
# stu = input().split()
# name = stu[1]
# id = stu[0]
# total_score = sum([int(score) for score in stu [-3:]])
# for i in range (n - 1):
#     temp = input().split()
#     total_score_temp = sum([int(score) for score in temp[-3:]])
#     if total_score < total_score_temp:
#         total_score = total_score_temp
#         mane = temp[1]
#         id = temp[0]
#
# print(name, id, total_score)

n = int(input())
total_score = 0
for i in range(n):
    temp = input().split()
    total_score_temp = sum([int(score) for score in temp[-3:]])
    if total_score < total_score_temp:
        total_score = total_score_temp
        name = temp[1]
        id = temp[0]

print(name, id, total_score)


















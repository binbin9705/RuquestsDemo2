#打印九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f'{j}x{i}={i*j}\t',end=' ')
    print()
sun=0
for i in range(101):
    sun=sun+i
print(sun)
# #数组按大小排序
# arr=[1,3,4,9,6,8,2]
# arr.sort()#从小到大排序
# arr.reverse()#将排序过的数组反过来
# # print(arr)
# for x in arr[3:]:
#     print(x)
# select name from cj group by nmae having min(cjf)>80
#
#
# #一个学生表 成绩 学科 姓名
# select *from xs where name in('张三'，'李四'')
# select name from sx where cj BETWEEN 80 and 100
# select name from xs where name like '张%'
# select name from xs where cj>80 and cj name='张三'
# select *from xs order by cj desc
# select name from xs group by name having min(cj)>80
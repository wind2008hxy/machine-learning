1.使用 array 定义矩阵

dataSet = array([[1.0,1.1],[1.0,1.0],[0.0,0.0],[0,0.1]])

2.使用 shape 返回矩阵的行数（列数）

dataSet.shape[0] #4
dataSet.shape[1] #2

3.使用 tile 成倍的扩大矩阵

intX =array([0,1,1,1])

tsample = tile(intX,(4,2)) # 表示将矩阵 行复制4次，列复制2次

4.矩阵各个元素值的平方/开平方

sqDiffMat = diffMat**2

distances = sqDistances**0.5

# 为什么是（4,2) 而不是两个参数呢？详解 6

5.使用 argsort 获得排序后的编号

x = array([3, 1, 2])

argsort(x) #[1,2,0]

# argsort 可以正序也可以逆序，可以按行拍序也可以按列排序

6.{}、[]、（）放元素的区别

{} 相当于 Map	字典
[] 相当于 List	数组
() 相当于 tuple	元组类型，初始化后不能改变

7.map 按照值排序的2种写法

dict= sorted(dic.iteritems(), key=lambda d:d[0])
sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)

https://www.cnblogs.com/oftenlin/p/5466490.html
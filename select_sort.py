__author__ = 'hechaoyi'

'''
选择排序
选择排序比较好理解，好像是在一堆大小不一的球中进行选择（以从小到大，先选最小球为例）：

　　1. 选择一个基准球

　　2. 将基准球和余下的球进行一一比较，如果比基准球小，则进行交换

　　3. 第一轮过后获得最小的球

　　4. 在挑一个基准球，执行相同的动作得到次小的球

　　5. 继续执行4，直到排序好

时间复杂度：O(n^2).  需要进行的比较次数为第一轮 n-1，n-2....1, 总的比较次数为 n*(n-1)/2

直接上代码：
'''
def selectedSort(myList):
    #获取list的长度
    length = len(myList)
    #一共进行多少轮比较
    for i in range(0,length-1):
        #默认设置最小值得index为当前值
        smallest = i
        #用当先最小index的值分别与后面的值进行比较,以便获取最小index
        for j in range(i+1,length-1):
            #如果找到比当前值小的index,则进行两值交换
            if myList[j]<myList[smallest]:
                tmp = myList[j]
                myList[j] = myList[smallest]
                myList[smallest]=tmp
        #打印每一轮比较好的列表
        print("Round ",i,": ",myList)



myList = [1,4,5,0,6]
print("Selected Sort: ")
selectedSort(myList)
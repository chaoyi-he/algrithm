__author__ = 'hechaoyi'


def test(listOne,start,end):
    if start>=end:
            return

    l = start
    r= end
    base = listOne[start]
    try:
        while l<r:
            while l<r and listOne[r]>=base:
                r=r-1
            listOne[start]=listOne[r]
            while l<r and listOne[l]<=base:
                l=l+1
            listOne[r] =listOne[l]
        listOne[l]=base
        test(listOne,start,l-1)
        test(listOne,l+1,end)
    except Exception as e:
        print(l)
        print(r)
        print(e)

def test2(listOne):
    for i in range(len(listOne)):
        for j in range(i+1,len(listOne)):
            if listOne[i]<=listOne[j]:
                temp = listOne[i]
                listOne[i]=listOne[j]
                listOne[j]=temp
    print(listOne)




if __name__=='__main__':
    myList = [49,38,65,97,76,13,27,49]
    # test(myList,0,len(myList)-1)
    # print(myList)

    test2(myList)




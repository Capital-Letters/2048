def bubble_sort(list) :
    for x in range(len(list)-1) :                           #选择趟数 n-1趟
        for y in range(len(list)-1-x) :                     #将最大的元素放到最后
            if list[y] > list[y+1] :
                list[y] , list[y+1] = list[y+1] , list[y]
def selection_sort(list) :
    for x in range(len(list)-1) :
        index_min = x
        for y in range(x+1,len(list)) :
            if list[index_min] > list[y] :
                index_min = y
        if x != index_min :
            list[x] , list[index_min] = list[index_min] , list[x]
def insertion_sort(list) :
    for x in range(len(list)) :
        preindex = x -1
        current = list[x]
        while preindex >= 0 and list[preindex] > current :
            list[preindex+1] = list[preindex]
            preindex -= 1
        list[preindex+1 ] = current #填充最后一个元素
def shell_sort(list) :
    import math
    gap = 1
    while gap < (len(list)/3) :    #创建好合适的步长
        gap = gap*3 + 1
    while gap > 0 :
        for i in range(gap , len(list)) : #从gap开始以gap为步长向前进行比较
            temp = list[i]
            j = i - gap                     #少一个步长的数
            while j >= 0 and list[j] > temp :#前一个数比后一个数大就进行交换
                list[j+gap] = list[j]
                j -= gap
            list[j+gap] = temp
        gap = math.floor(gap/3)
def quick_sort(list,x,y) :
    if x >= y :
        return
    m = x
    n = y
    base = list[x]
    while m < n :
        while m < n and list[n] > base :
            n -= 1
        if m == n :
            break
        list[m] = list[n]
        while m < n and list[m] < base :
            m += 1
        if m == n :
            break
        list[n] = list[m]
def shell_sort2(list) :
    import math
    gap = 1
    while gap < (len(list)/3) :
        gap = gap * 3 + 1
    while gap > 0 :
        for x in range(gap,len(list)) :
            temp = list[x]
            y = x - gap
            while y >= 0 and list[y] > temp :
                list[y+gap] = list[y]
                y -= gap
            list[y+gap] = temp
        gap = math.floor(gap/3)
def merge_sort(list) :
    if len(list) <= 1 :
        return list
    middle = len(list) // 2
    left , right = list[:middle] , list[middle:]
    return merge(merge_sort(left),merge_sort(right))
def merge(left,right) :
    result = []
    while left and right :
        if left[0] <= right[0] :
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left :
        result.append(left.pop(0))
    while right :
        result.append(right.pop(0))
    return result


if __name__ == '__main__' :
    list = [1,6,3,2,4,5,8,7,9]
    print(merge_sort(list))

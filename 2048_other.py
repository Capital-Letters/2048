import random
from tkinter import *
list = [[2, 0, 0, 2],
         [2, 0, 0, 2],
         [2, 0, 4, 2],
         [2, 0, 8, 2],
         ]
#矩阵左右变换
def matrix_transform_right_left(list) :
    for x in range(len(list)) :
        for y in range(len(list[x])//2) :
            list[x][y] , list[x][len(list[x])-1-y] = list[x][len(list[x])-1-y] , list[x][y]
    return list
#矩阵行列变换
def matrix_transform_row_to_column(list) :
    for x in range(len(list)) :
        for y in range(x+1,len(list[x])) :
            list[x][y] , list[y][x] = list[y][x] , list[x][y]
    return list
#矩阵相同元素合并
def merge_the_same_element(list) :
    for x in range(len(list)) :
        for y in range(len(list[x])-1) :
                if list[x][y] == list[x][y+1] :
                    list[x][y] += list[x][y]
                    list[x][y+1] = 0
    return list
#矩阵相同元素合并
def same_element_merge(list) :
    indexA = 0
    indexB = 0
    for x in range(len(list)):
        while indexA < len(list[x]) - 1:
            while indexA < len(list[x]) - 1 and list[x][indexA] == 0:  # 找到第一个非0元素
                indexA += 1
            if indexA == len(list[x]) - 1:
                break
            indexB = indexA + 1
            while indexB <= len(list[x]) - 1 and list[x][indexB] == 0:  # 找到第二个非0元素
                indexB += 1
            if indexB == len(list[x]):
                break
            if list[x][indexA] == list[x][indexB]:  # 如果两个非0元素相等就将indexB合并到indexA
                list[x][indexA] += list[x][indexA]
                list[x][indexB] = 0
                indexA = indexB + 1  # 合并完成之后从indexB+1号元素开始继续寻找下一趟非零元素
            else:
                indexA = indexB  # 下一趟从indexB开始寻找下一个非零元素
        indexA = indexB = 0
    return list
#矩阵零元素后置
def adjust_the_position_of_the_element_of_zero(list) :
    for x in range(len(list)) :
        for y in range(len(list[x])):
            if list[x][y] == 0:
                list[x].remove(list[x][y])
                list[x].append(0)
    return list
#保存上一次与本次游戏记录
def remember_the_list(list) :
    remember_list = []
    for x in range(len(list)) :
        for y in range(len(list[x])) :
            remember_list.append(list[x][y])
    return remember_list
#比较两张表是否相等
def equal_list(list1 , list2) :
     equal = True
     for x in range(len(list1)) :
         for y in range(len(list1[x])) :
             if list1[x][y] != list2[x][y] :
                 equal = False
                 break
         if equal == False :
             break
     return equal

#完成一步之后进行随机数替代零元素
def fill_the_zero(list) :
    zero_count = 0
    indexA = 0
    indexB = 0
    list_indexofzero_row = []
    list_indexofzero_column = []
    for x in range(len(list)) :         #记录列表中零元素的下标
        for y in range(len(list[x])) :
            if list[x][y] == 0 :
                zero_count += 1
                list_indexofzero_row.append(x)
                list_indexofzero_column.append(y)
    fill_count = random.randint(0,zero_count)
    rand_list = []
    for x in range(fill_count) :      #生成一个随机的数组下标列表
        random_index = random.randint(0,zero_count-1)
        if random_index not in rand_list :
            rand_list.append(random_index)
    #按随机生成的下标进行填充
    for x in range(len(rand_list)) :
        number = 2
        if random.randint(0, 1) == 1:
            number = 4
        list[list_indexofzero_row[rand_list[x]]][list_indexofzero_column[rand_list[x]]] = number
    return list
#输出完成一步之后的结果
def output_the_2048(list) :
    for item in list:
        print(item)
#判断游戏是否结束
def game_oevr(list) :
    for x in range(len(list)) :
        for y in range(len(list[x])) :
            if list[x][y] == 0 :
                return
    flag = 0
    for x in range(len(list)-1) :
        if list[x][len(list[x])-1] == list[x+1][len(list[x])-1] :
            return
        for y in range(len(list[x])-1) :
            if list[x][y] == list[x][y+1] or list[x][y] == list[x+1][y] :
                return
            else:
                flag = 1
    if flag == 1 :
        print('***game**over***')
#游戏开始
while True :
    key = input()[0]
    if key == 'a' :
        remember_list = remember_the_list(list)
        merge_the_same_element(list)
        adjust_the_position_of_the_element_of_zero(list)
        list_change = remember_the_list(list)
        if remember_list != list_change :   #如果移动过的列表与原列表不相等就进行零元素随机数的填充,相等就代表本次操作无效
            fill_the_zero(list)
        else:
            print('此次操作无效')
        output_the_2048(list)
        game_oevr(list)
    elif key == 'd':
        remember_list = remember_the_list(list)
        matrix_transform_right_left(list)
        same_element_merge(list)
        adjust_the_position_of_the_element_of_zero(list)
        matrix_transform_right_left(list)
        list_change = remember_the_list(list)
        if list_change != remember_list :   #如果移动过的列表与原列表不相等就进行零元素随机数的填充,相等就代表本次操作无效
            fill_the_zero(list)
        else :
            print('此次操作无效')
        output_the_2048(list)
        game_oevr(list)
    elif key == 'w':
        remember_list = remember_the_list(list)
        matrix_transform_row_to_column(list)
        same_element_merge(list)
        adjust_the_position_of_the_element_of_zero(list)
        matrix_transform_row_to_column(list)
        list_change = remember_the_list(list)
        if list_change != remember_list :   #如果移动过的列表与原列表不相等就进行零元素随机数的填充,相等就代表本次操作无效
            fill_the_zero(list)
        else :
            print('此次操作无效')
        output_the_2048(list)
        game_oevr(list)
    elif key == 's':
        remember_list = remember_the_list(list)
        matrix_transform_row_to_column(list)
        matrix_transform_right_left(list)
        same_element_merge(list)
        adjust_the_position_of_the_element_of_zero(list)
        matrix_transform_right_left(list)
        matrix_transform_row_to_column(list)
        list_change = remember_the_list(list)
        if list_change != remember_list :   #如果移动过的列表与原列表不相等就进行零元素随机数的填充,相等就代表本次操作无效
            fill_the_zero(list)
        else :
            print('此次操作无效')
        output_the_2048(list)
        game_oevr(list)









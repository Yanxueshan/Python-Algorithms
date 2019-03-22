'''
    排序算法--05--快速排序O(nlogn) --- 双路快排

    对单路快排进行的优化
'''
from Insertion_Sort.insertion_sort import insertion_sort_improve
from random import randint

__author__ = 'Yan'
__date__ = '2019/3/21 22:34'


def partition(values, left, right):
    '''
        对values[left...right]部分进行partition操作
        返回left_index, 使得values[left...left_index-1] <= values[left]
        values[left_index+1...right] >= values[left]
    '''
    random_index = randint(left, right)
    values[left], values[random_index] = values[random_index], values[left]
    v = values[left]

    left_index = left + 1
    right_index = right

    while True:
        # while结束后，left_index指向大于等于v的第一个元素
        while left_index < right and values[left_index] < v:
            left_index += 1

        # while结束后，right_index指向小于等于v的第一个元素
        while right >= left + 1 and values[right_index] > v:
            right_index -= 1

        if left_index >= right_index:
            break

        values[left_index], values[right_index] = values[right_index], values[left_index]
        left_index += 1
        right_index -= 1

    values[left], values[right_index] = values[right_index], values[left]
    return right_index


def _quick_sort(values, left, right):
    '''
        排序算法--05--快速排序O(nlogn) --- 单路快排
    '''
    if right - left < 15:
        insertion_sort_improve(values)
        return
    right_index = partition(values, left, right)
    _quick_sort(values, left, right_index-1)
    _quick_sort(values, right_index+1, right)


def quick_sort(values):
    '''
        排序算法--05--快速排序O(nlogn) --- 单路快排
    '''
    _quick_sort(values, 0, len(values)-1)
    return values


if __name__ == "__main__":
    score = [67, 89, 57, 99, 49, 45, 78, 45, 100, 98, 95, 78, 39, 80, 10, 32, 39]
    print(quick_sort(score))

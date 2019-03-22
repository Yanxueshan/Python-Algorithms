'''
    排序算法--05--快速排序O(nlogn) --- 单路快排

    缺点：
        1. 当列表接近有序时，快速排序算法的性能很差，有可能会退化成O(n2)
        2. 当序列重复元素较多时，分层极不平衡，有可能接近O(n2)
'''
from Insertion_Sort.insertion_sort import insertion_sort_improve
from random import randint

__author__ = 'Yan'
__date__ = '2019/3/21 19:34'


def partition(values, left, right):
    '''
        对values[left...right]部分进行partition操作
        返回left_index, 使得values[left...left_index-1] < arr[left_index]
        values[left_index+1...right] >= values[left_index]
    '''
    # 从values[left...right]中随机取出一个元素与values[left]进行交换
    # 当列表接近有序时，快速排序算法的性能很差，有可能会退化成O(n2)
    random_index = randint(left, right)
    values[left], values[random_index] = values[random_index], values[left]
    v = values[left]

    # right_index 表示 v 所应该在的正确索引
    # right_index 永远指向比 v 小的元素
    left_index = left
    for i in range(left+1, right+1):
        if values[i] < v:
            values[left_index+1], values[i] = values[i], values[left_index+1]
            left_index += 1
    values[left_index], values[left] = values[left], values[left_index]
    return left_index


# ------------------------quick_sort 1-------------------------------


def _quick_sort(values, left, right):
    '''
        排序算法--05--快速排序O(nlogn) --- 单路快排
    '''
    if left >= right:
        return
    left_index = partition(values, left, right)
    _quick_sort(values, left, left_index-1)
    _quick_sort(values, left_index+1, right)


def quick_sort(values):
    '''
        排序算法--05--快速排序O(nlogn) --- 单路快排
    '''
    _quick_sort(values, 0, len(values)-1)
    return values


# ------------------------quick_sort 2-------------------------------


def _quick_sort_improve(values, left, right):
    '''
        排序算法--05--快速排序O(nlogn) --- 单路快排 -- 针对quick_sort进行的优化
    '''
    if right - left < 15:
        insertion_sort_improve(values)
        return
    left_index = partition(values, left, right)
    _quick_sort_improve(values, left, left_index-1)
    _quick_sort_improve(values, left_index+1, right)


def quick_sort_improve(values):
    '''
        排序算法--05--快速排序O(nlogn) --- 单路快排 -- 针对quick_sort进行的优化
    '''
    _quick_sort_improve(values, 0, len(values)-1)
    return values


if __name__ == "__main__":
    score = [67, 89, 57, 99, 49, 45, 78, 45, 100, 98, 95]
    # print(quick_sort(score))
    print(quick_sort_improve(score))

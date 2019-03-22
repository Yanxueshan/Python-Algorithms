'''
    排序算法--05--快速排序O(nlogn) --- 三路快排

    对双路快排进行的优化
'''
from Insertion_Sort.insertion_sort import insertion_sort_improve
from random import randint

__author__ = 'Yan'
__date__ = '2019/3/22 10:38'


def partition(values, left, right):
    '''
        对values[left...right]部分进行partition操作
        返回lt_index, gt_index，使得values[left+1...lt_index] < values[left]
        values[gt_index...right] > values[left]
        values[lt_index+1..gt_index-1] == values[left]
    '''
    random_index = randint(left, right)
    values[left], values[random_index] = values[random_index], values[left]
    v = values[left]

    # lt_index --> 最后一个小于v的元素
    # gt_index --> 倒数第一个大于v的元素
    # lt_index + 1 --> 第一个等于v的元素

    lt_index = left  # values[left+1...lt_index] < v
    gt_index = right+1  # values[gt_index...right] > v
    i = left + 1  # values[left+1...i] == v

    while i < gt_index:
        if values[i] < v:
            values[i], values[lt_index+1] = values[lt_index+1], values[i]
            lt_index += 1
            i += 1
        elif values[i] == v:
            i += 1
        else:
            values[i], values[gt_index-1] = values[gt_index-1], values[i]
            gt_index -= 1
    values[left], values[lt_index] = values[lt_index], values[left]
    return lt_index, gt_index


def _quick_sort(values, left, right):
    '''
        排序算法--05--快速排序O(nlogn) --- 单路快排
    '''
    if right - left < 15:
        insertion_sort_improve(values)
        return
    lt_index, gt_index = partition(values, left, right)
    _quick_sort(values, left, lt_index)
    _quick_sort(values, gt_index, right)


def quick_sort(values):
    '''
        排序算法--05--快速排序O(nlogn) --- 单路快排
    '''
    _quick_sort(values, 0, len(values)-1)
    return values


if __name__ == "__main__":
    score = [67, 89, 57, 99, 49, 45, 78, 45, 100, 98, 95, 78, 39, 80, 10, 32, 39]
    print(quick_sort(score))

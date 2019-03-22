'''
    排序算法--04--归并排序--O(nlogn)
'''
from Insertion_Sort.insertion_sort import insertion_sort

__author__ = 'Yan'
__date__ = '2019/3/20 21:56'


def merge(values, left, mid, right):
    '''
        merge函数--将 values[left...mid] 和 values[mid+1...right] 进行归并
    '''
    # 将values复制一份赋值给new_values
    new_values = values[:]
    # values[left...mid] 的左index
    left_index = left
    # values[mid+1...right] 的左index
    right_index = mid+1
    for i in range(left, right+1):
        if left_index >= mid + 1:
            values[i:right+1] = new_values[right_index:right+1]
            break
        elif right_index > right:
            values[i:right+1] = new_values[left_index:mid+1]
            break
        if new_values[left_index] < new_values[right_index]:
            values[i] = new_values[left_index]
            left_index += 1
        else:
            values[i] = new_values[right_index]
            right_index += 1


# ------------------------merge_sort 1（自顶向下）-------------------------------


def _merge_sort(values, left, right):
    '''
        排序算法--04--归并排序--O(nlogn)
    '''
    if left >= right:
        return
    mid = left + (right - left) // 2
    # 对左半部分进行递归
    _merge_sort(values, left, mid)
    # 对右半部分进行递归
    _merge_sort(values, mid+1, right)
    merge(values, left, mid, right)


def merge_sort(values):
    '''
        排序算法--04--归并排序--O(nlogn)
    '''
    _merge_sort(values, 0, len(values)-1)
    return values


# --------------------------merge_sort 2（自顶向下）------------------------------------


def _merge_sort_improve1(values, left, right):
    '''
        排序算法--04--归并排序--O(nlogn)-->针对merge_sort进行的优化1
    '''
    if left - right <= 15:
        # 当n较小时，插入排序要优于归并排序
        insertion_sort(values)
        return
    mid = left + (right - left) // 2
    # 对左半部分进行递归
    _merge_sort_improve1(values, left, mid)
    # 对右半部分进行递归
    _merge_sort_improve1(values, mid+1, right)
    merge(values, left, mid, right)


def merge_sort_improve1(values):
    '''
        排序算法--04--归并排序--O(nlogn)-->针对merge_sort进行的优化
    '''
    _merge_sort_improve1(values, 0, len(values)-1)
    return values


# --------------------------merge_sort 3（自顶向下）------------------------------------


def _merge_sort_improve2(values, left, right):
    '''
        排序算法--04--归并排序--O(nlogn)-->针对merge_sort进行的优化2
    '''
    if left - right <= 15:
        # 当n较小时，插入排序要优于归并排序
        insertion_sort(values)
        return
    mid = left + (right - left) // 2

    # 如果values[mid] < values[mid+1]， 那么说明values[left...right]是排序好了的，不必进行归并了
    if values[mid] < values[mid+1]:
        return

    # 对左半部分进行递归
    _merge_sort_improve2(values, left, mid)
    # 对右半部分进行递归
    _merge_sort_improve2(values, mid+1, right)
    merge(values, left, mid, right)


def merge_sort_improve2(values):
    '''
        排序算法--04--归并排序--O(nlogn)-->针对merge_sort进行的优化
    '''
    _merge_sort_improve2(values, 0, len(values)-1)
    return values


# --------------------------merge_sort 4（自底向上）------------------------------------


def _merge_sort_bu(values, left, right):
    '''
        排序算法--04--归并排序--O(nlogn)-->自底向上排序
    '''
    # size表示要merge的元素个数
    # 第一次merge: 1个元素
    # 第二次merge: 2个元素
    # 第三次merge: 4个元素
    # 第n次merge: 2^(n-1)个元素
    # ....
    size = 1
    while size < right:
        for i in range(0, right, 2 * size):
            if i + size > right:
                break
            if values[i+size-1] < values[i+size]:
                continue
            merge(values, i, i+size-1, min(i+2*size-1, right-1))
        size = 2 * size


def merge_sort_bu(values):
    '''
        排序算法--04--归并排序--O(nlogn)-->自底向上排序
    '''
    _merge_sort_bu(values, 0, len(values)-1)
    return values


# --------------------------merge_sort 5（自底向上）------------------------------------


def _merge_sort_bu_improve(values, left, right):
    '''
        排序算法--04--归并排序--O(nlogn)-->针对merge_sort_bu进行的优化
    '''
    # size表示要merge的元素个数
    # 第一次merge: 1个元素
    # 第二次merge: 2个元素
    # 第三次merge: 4个元素
    # 第n次merge: 2^(n-1)个元素
    # ....

    # 当n较小时，插入排序优于归并排序
    for i in range(0, right, 16):
        insertion_sort(values[i:min(right-1, i+15)])

    size = 16
    while size < right:
        for i in range(0, right, 2 * size):
            if i + size > right:
                break
            if values[i+size-1] < values[i+size]:
                continue
            merge(values, i, i+size-1, min(i+2*size-1, right-1))
        size = 2 * size


def merge_sort_bu_improve(values):
    '''
        排序算法--04--归并排序--O(nlogn)-->针对merge_sort_bu进行的优化
    '''
    _merge_sort_bu(values, 0, len(values)-1)
    return values


if __name__ == "__main__":
    score = [67, 89, 57, 99, 49, 45, 78, 45, 100, 98, 95]
    # print(merge_sort(score))
    # print(merge_sort_improve1(score))
    # print(merge_sort_improve2(score))
    # print(merge_sort_bu(score))
    print(merge_sort_bu_improve(score))

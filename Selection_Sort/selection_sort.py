'''
    排序算法--02--选择排序
'''

__author__ = 'Yan'
__date__ = '2019/3/20 20:36'


def selection_sort(values):
    '''
        排序算法--02--选择排序--O(n2)
    '''
    for i in range(len(values)-1):
        # 假设本次循环 i 为最小值所在的索引
        min_index = i
        for j in range(min_index+1, len(values)):
            if values[j] < values[min_index]:
                # 如果values[j] < values[min_index]，那么说明 j 为min_index
                min_index = j
        values[i], values[min_index] = values[min_index], values[i]
    return values


if __name__ == "__main__":
    score = [67, 89, 57, 99, 49, 45, 78, 45, 100, 98, 95]
    print(selection_sort(score))

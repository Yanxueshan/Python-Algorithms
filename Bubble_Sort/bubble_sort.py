'''
    排序算法--01--冒泡排序
'''

__author__ = 'Yan'
__date__ = '2019/3/20 20:29'


def bubble_sort(values):
    '''
        排序算法--01--冒泡排序--O(n2)
    '''
    for i in range(len(values)-1):
        # 第一次循环(0 -- len(score)-1)，将最大的元素放在最末尾
        # 第二次循环(0 -- len(score)-2)，将剩下的元素中最大的元素放在倒数第二个位置
        # ...依次循环，总共循环len(score)-1次
        for j in range(0, len(values)-i-1):
            if values[j] > values[j+1]:
                values[j], values[j+1] = values[j+1], values[j]

    return values


if __name__ == "__main__":
    score = [67, 89, 57, 99, 49, 45, 78, 45, 100, 98, 95]
    print(bubble_sort(score))

'''
    排序算法--03--插入排序
    当序列近乎有序时，插入排序的效率很高，近乎O(n)
'''

__author__ = 'Yan'
__date__ = '2019/3/20 20:45'


def insertion_sort(values):
    '''
        排序算法--03--插入排序--O(n2)
    '''
    for i in range(1, len(values)):
        for j in range(i, 0, -1):
            if values[j] < values[j-1]:
                # 一次交换值的操作等于三次赋值操作
                values[j], values[j-1] = values[j-1], values[j]
            else:
                break
    return values


def insertion_sort_improve(values):
    '''
        排序算法改进--03--插入排序--O(n2)
    '''
    for i in range(1, len(values)):
        # 将当前位置的值赋值给value
        value = values[i]
        for j in range(i, 0, -1):
            if value < values[j-1]:
                values[j] = values[j-1]
                j = j - 1
            else:
                break
        # j 表示 value 应该插入的位置
        values[j] = value
    return values


if __name__ == "__main__":
    score = [67, 89, 57, 99, 49, 45, 78, 45, 100, 98, 95]
    # print(insertion_sort(score))
    print(insertion_sort_improve(score))

'''
    排序算法--06--堆排序O(nlogn)
'''

__author__ = 'Yan'
__date__ = '2019/3/22 10:38'


class HeapSort:
    '''
        排序算法--06--堆排序O(nlogn)
    '''
    def __init__(self, values):
        self.values = values
        for i in range(self._parent(len(self.values)-1), -1, -1):
            self._sift_down(i)

    def _parent(self, index):
        if index < 0 and index > len(self.values):
            raise IndexError("index id illegal.")
        return (index - 1) // 2

    def _left_child(self, index):
        if index < 0 and index > len(self.values):
            raise IndexError("index id illegal.")
        return 2 * index + 1

    def _right_child(self, index):
        if index < 0 and index > len(self.values):
            raise IndexError("index id illegal.")
        return 2 * index + 2

    def _sift_up(self, index):
        '''
            Sift UP 上浮，若子节点的值大于父节点的值，则Sift UP
        '''
        while index > 0 and self.values[index] > self.values[self._parent(index)]:
            self.values[index], self.values[self._parent(index)] = self.values[self._parent(index)], self.values[index]
            index = self._parent(index)

    def _sift_down(self, index):
        '''
            Sift Down下沉，若父节点小于子节点的值，则Sift Down
        '''
        while self._left_child(index) < len(self.values):
            left_child = self._left_child(index)
            right_child = self._right_child(index)
            max_index = left_child
            if right_child < len(self.values) and self.values[left_child] < self.values[right_child]:
                max_index = right_child

            if self.values[max_index] <= self.values[index]:
                break

            self.values[max_index], self.values[index] = self.values[index], self.values[max_index]
            index = max_index

    def find_max(self):
        '''
            找到最大堆MaxHeap中的最大元素
        '''
        if len(self.values) == 0:
            raise ValueError("heap is empty.")
        return self.values[0]

    def extract_max(self):
        '''
            取出最大堆MaxHeap中的最大元素，总共分两步：
                1. 将第一个元素（最大值）于最后一个元素交换
                2. 对交换后的第一个元素进行Sfit Down操作
        '''
        ret = self.find_max()
        self.values[0], self.values[-1] = self.values[-1], self.values[0]
        self.values.remove(self.values[-1])
        self._sift_down(0)
        return ret

    def heap_sort(self):
        '''
            堆排序
        '''
        result = []
        while self.values:
            result.append(self.extract_max())
        return result


def heap_sort(values):
    '''
        堆排序
    '''
    heapsort = HeapSort(values)
    return heapsort.heap_sort()


if __name__ == "__main__":
    score = [67, 89, 57, 99, 49, 45, 78, 45, 100, 98, 95, 78, 39, 80, 10, 32, 39]
    print(heap_sort(score))

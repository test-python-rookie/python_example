
# 快速排序
def quickSort(arr, left=None, right=None):
    left = 0 if not isinstance(left,(int, float)) else left
    right = len(arr)-1 if not isinstance(right,(int, float)) else right
    if left < right:
        partitionIndex = partition(arr, left, right)
        quickSort(arr, left, partitionIndex-1)
        quickSort(arr, partitionIndex+1, right)
    return arr

def partition(arr, left, right):
    pivot = left
    index = pivot+1
    i = index
    while  i <= right:
        if arr[i] < arr[pivot]:
            swap(arr, i, index)
            index+=1
        i+=1
    swap(arr,pivot,index-1)
    return index-1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

if __name__ == '__main__':
    list = [5, 1, 8, 123, 22, 54, 7, 99, 300, 222]
    print("List source is:", list)
    result = quickSort(list)
    print("List sort is:", result)
"""
def kuaisu(list):
    if len(list) >= 2:
        med = list[0]
        left, right = [], []
        list.remove(med)
        for num in list:
            if num >= med:
                right.append(num)
            else:
                left.append(num)
            print(left + [med] + right)
        return kuaisu(left) + [med] + kuaisu(right)
    else:
        return list

list = [2,3,5,7,1,4,6,15,5,2,7,9,10,15,9,17,12]
print(kuaisu(list))
"""
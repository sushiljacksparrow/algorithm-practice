def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]

    return arr


if __name__ == '__main__':
    arr = [10,1,2,11]
    print bubble_sort(arr)

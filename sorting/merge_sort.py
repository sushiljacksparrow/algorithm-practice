def merge(arr1, arr2):
    p1, p2 = 0, 0
    out = []

    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] <= arr2[p2]:
            out.append(arr1[p1])
            p1 += 1
        else:
            out.append(arr2[p2])
            p2 += 1

    while p1 < len(arr1):
        out.append(arr1[p1])
        p1 += 1

    while p2 < len(arr2):
        out.append(arr2[p2])
        p2 += 1
    return out

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    if len(arr) == 2:
        return sorted(arr)

    mid = len(arr)/2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


if __name__ == '__main__':
    arr = [10,1,2,11]
    print merge_sort(arr)

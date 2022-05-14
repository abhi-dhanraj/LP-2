
def selection_sort(a):
    n = len(a)
    for i in range(n):
        min_ind = i
        for j in range(i+1, n):
            if a[min_ind] > a[j]:
                min_ind = j
        a[min_ind], a[i] = a[i], a[min_ind]
    return a


a = list(map(int, input().split()))
print(selection_sort(a))

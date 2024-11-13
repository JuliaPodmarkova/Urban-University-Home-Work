nums = [5, 6, 2, 1, 3, 4]

def bubbleSort(ls):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ls)-1):
            if ls[i] > ls[i+1]:
                ls[i], ls[i+1] = ls[i+1], ls[i]
                swapped = True

bubbleSort(nums)
print(nums)

def selectionSort(ls):
    for i in range(len(ls)):
        lowest = i
        for j in range(i, len(ls)):
            if ls[j] < ls[lowest]:
                lowest = j
        ls[i], ls[lowest] = ls[lowest], ls[i]

selectionSort(nums)
print(nums)

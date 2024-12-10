import random
  
#Bubble sort vytvarime array a styl jak bude sortovat
array = [4, 87, 31, 70, 96, 11, 2, 42, 63, 28]

def bubble_sort():
    n=len(array)
    for i in range(n-1):
        for j in range (0, n-i-1):
            #hledame index nejmensi hodnoty
            if array[j]>array[j+1]:
                array[j], array[j+1]=array[j+1],array[j]
    return array

#Bogo sort vytvarime array a styl jak bude sortovat
array1=[78, 63, 2, 54, 96, 33, 41, 20 ,15, 7]
def is_sorted(array1):
    for i in range(1, len(array1)):
        #hledame index nejmensi hodnoty
        if array1[i]<array1[i-1]:
            return False
    return True

#Pridava se promena count, ktera ukaze nam pocet pokusu
def bogosort(array1):
    count = 0
    while not is_sorted(array1):
        random.shuffle(array1)
        count += 1
        print("Try", count, ":", array1)

bogosort(array1)

#Selection sort
array2 = [74, 28, 81, 1, 44, 62, 16, 98, 67, 65]

def selection_sort(array2):
    n = len(array2)
    for i in range(n):
        mx = i
        for j in range(i + 1, n):
            #hledame index nejmensi hodnoty
            if array2[j] < array2[mx]:
                mx = j
        array2[i], array2[mx] = array2[mx], array2[i]

selection_sort(array2)

#Insertion sort vytvarime array a styl sortovani
array3 = [82, 16, 28, 34, 3, 78, 52, 92, 65, 70]

def insertion_sort(array3):
    n = len(array3)
    for i in range(1, n):  
        ky = array3[i]     
        j = i - 1
        #element veci od ky posune se v pravo
        while j >= 0 and array3[j] > ky:  
            array3[j + 1] = array3[j]
            j -= 1
        array3[j + 1] = ky

insertion_sort(array3)

#Vypsani vsech
print("Bogo sort:", array1)
print("Bubble sort", bubble_sort()) 
print("Selection sort:", array2)
print("Insertion sort:", array3)

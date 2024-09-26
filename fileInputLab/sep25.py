L = [4,9,1,5,2]

def selectionSort(j):
    if j==0:
        print(L)
    else:
        max = -1
        dolly = 0
        for k in range(len(L)):
            if L[k] > max:
                max = L[k]
                dolly = k
        #exchange L[j] and L[dolly]
        (L[j],L[dolly]) = (L[dolly],L[j])
        selectionSort(j-1)
        
selectionSort(len(L)-1)
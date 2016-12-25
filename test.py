##from tools import *
##def selectionSort(items):
##	ordered=items.copy()
##	print(items)
##	for i in range(len(ordered) -1, 0, -1):
##		nextLarge=0
##
##		for j in range(1, i+1):
##			if ordered[j]>ordered[nextLarge]:
##				nextlarge=j
##		swap(ordered, nextLarge, i)
##	return ordered
##print(selectionSort([3,1,12,21,0,2,5]))
##

from tools import *
def selectionSort(items):
    ordered=items.copy()
    print(items)
    for i in range(len(ordered)):
        nextSmall=-1

        for j in range(i, len(ordered)):
            if ordered[j]<ordered[nextSmall]:
                nextSmall=j

        swap(ordered, nextSmall, i)
    return ordered

print(selectionSort([3,1,12,53,21,0,2,5]))
#print(sorted([3,1,12,53,21,0,2,5]))

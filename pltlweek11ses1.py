##def swap(a_list,x,y):
##    temp=a_list[x]
##    a_list[x]=a_list[y]
##    a_list[y]=temp
##
##itemA="jack john mick"
##itemB="kat nikki sara"
##temp=""
##
##temp=itemA
##itemA=itemB
##itemB=temp
##print("Now the cards have switched: itemA",itemA, "\nitemB",itemB,"\ntemp", temp)

from tools import *
def selectionSort(items):
	ordered=items.copy()
	print(items)
	for i in range(len(ordered) -1, 0, -1):
		nextLarge=0

		for j in range(1, i+1):
			if ordered[j]>ordered[nextLarge]:
				nextlarge=j
		swap(ordered, nextLarge, i)
	return ordered
print(selectionSort([3,1,23,56,12,86,21,0,2,53,5]))
##
##set1={2,3,4,5,3,6,7,4}
##set2={2,3,5,6,7,4,8,0}
##print (set1, "\n", set2)
##print('are the sets equal?',set1==set2)
##print("is set 2 contained in set 1?", set1>set2)
##print("is set one contained in set 2?", set1<set2)
##
##
##

   

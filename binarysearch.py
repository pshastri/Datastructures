import sys
mid=0
def binarysearch(mylist,find,first,last):
	mid=(last-first)/2
	if (last-first<2):
		return (mylist[first]==find) or (mylist[last]==find)
	elif(find<mylist[mid]):
		return binarysearch(mylist,find,0,mid-1)
	elif (find>mylist[mid]):
		return binarysearch(mylist,find,mid+1,len(mylist)-1)
	else:
		return "found"

if __name__=='__main__':
	thislist=[0,3,7,8,9]
	item=8
	
	itemfind=binarysearch(thislist,item,0,len(thislist)-1)
	print itemfind
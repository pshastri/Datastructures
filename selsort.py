import sys
#s=[3,1,2,8,5,4]

# # for i in range (len(s)-1):
	# # ind=i
	# # val=s[i]
	# # j=i+1
	# # while j<len(s):
		# # if s[j]<val:
			# # ind=j
			# # val=s[j]
		# # j+=1
	# # s[i],s[ind]=s[ind],s[i]
# # print s
# # for i in range (len(s)-1):
	# # print s
	# # mixindx=i
	# # minval=s[i]
	# # j=i+1
	# # while j < len(s):
		# # if minval>s[j]:
			# # mixindx=j
			# # minval=s[j]
		# # j+=1
	# # tmp=s[i]
	# # s[i]=s[mixindx]
	# # s[mixindx]=tmp
def selsort(mylist,i,j,mylen):
	while j<mylen:
		if mylist[i]>mylist[j]:
			mylist[i],mylist[j]=mylist[j],mylist[i]
		i=i+1
		j=j+1
		mylen=mylen-1
	return selsort(mylist,i,j,mylen)
if __name__=='__main__':
	s=[3,1,2,8,5,4]
	result=selsort(s,0,1,len(s))
	print result
# for i in range (len(s)-1):
	# j=i+1
	# while j<len(s):
		# if s[i]>s[j]:
			# s[i],s[j]=s[j],s[i]
		# j+=1
# print s
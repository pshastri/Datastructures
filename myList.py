import sys

class Node:
	def __init__(self,init_data):
		self.data=init_data
		self.next=None
	def get_data(self):
		return self.data
	def get_next(self):
		return self.next
	def set_data(self,new_data):
		self.data=new_data
	def set_next(self,new_next):
		self.next=new_next

class myList:
	def __init__(self):
		self.head=None
	def list_add(self,item):
		tmp=Node(item)
		tmp.set_next(self.head)
		self.head=tmp
	def list_isempty(self):
		return self.head==None
	def list_remove(self,item):
		current=self.head
		previous=None
		found=False
		while not found:
			if current.get_data()==item:
				found=True
			else:
				previous=current
				current=current.get_next()
		if previous==None:
			self.head=current.get_next()
		else:
			previous.set_next(current.get_next())
	def list_search(self,item):
		current=self.head
		found=False
		while not found:
			if current.get_data()==item:
				found=True
			else:
				current=current.get_next()
		return found
	def list_size(self):
		count=0
		current=self.head
		while current!=None:
			count+=1
			current=current.get_next()
		return count
	def list_print(self):
		current=self.head
		if current!=None:
			print current.get_data()
			current=current.get_next()
		else:
			print "no data"
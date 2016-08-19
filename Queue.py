import sys

class myQueue():
	def __init__(self):
		self.queue=[]
	def queue_empty(self):
		return self.queue==[]
	def queue_push(self,item):
		self.queue.insert(0,item)
	def queue_pop(self):
		return self.queue.pop()
	def queue_size(self):
		return len(self.queue)
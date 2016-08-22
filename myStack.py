import sys

class myStack():
	def __init__(self):
		self.stack=[]
		
	def stack_empty(self):
		return self.stack==[]
	def stack_print(self):
		return self.stack
	def stack_push(self,item):
		self.stack.append(item)
	def stack_pop(self):
		return self.stack.pop()
	def stack_peek(self):
		return self.stack[len(stack)-1]
	def stack_size(self):
		return len(self.stack)
from Queue import myQueue

if __name__=='__main__':
	newQueue=myQueue()
	print newQueue.queue_empty()
	newQueue.queue_push(93)
	newQueue.queue_push(56)
	newQueue.queue_push(32)
	print newQueue
	print newQueue.queue_pop()
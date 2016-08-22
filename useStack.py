from myStack import myStack

if __name__=='__main__':
	st=myStack()
	print st.stack_empty()
	st.stack_push(10)
	st.stack_push(20)
	st.stack_push(30)
	print st.stack_print()
	
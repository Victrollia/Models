while True:
	user_list = []
	print('\n Enter elements of a list separated by newline. When done, enter "q": ')
	while True:
		input_string = input(">")
		user_list.append(input_string[4:])
		if input_string == 'q':
			#user_list.remove('q')
			print('\n')
			print(','.join(user_list)[1:-1])
	# print list

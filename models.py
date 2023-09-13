user_list = []
while True:
	input_string = input('Enter elements of a list separated by newline. When done, enter "q": ')
	user_list.append(input_string[4:])
	if input_string == 'q':
		#user_list.remove('q')
		print(','.join(user_list)[1:-1])
		break
# print list

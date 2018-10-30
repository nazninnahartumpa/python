# find out the lesser number if two or both number are even and find the greater number if two or one number is odd
# def func(a,b):
# 	if a%2 == 0 and b%2 == 0:
# 		print(min(a,b))
# 	else:
# 		print(max(a,b))
# func(8,30)

# write the function takes two word string return true if two words are start with same letter otherwise return false
# def func2(text):
# 	word_list = text.split()
# 	if word_list[0][0] == word_list[1][0]:
# 		print('match')
# 		return True
# 	else:
# 		print('Not match')
# 		return False
# func2('Lame Bear')

#write a function return true whene sum of the two intiger is 20 or one of the integer is 20 otherwise return false
def func3(a,b):
	if (a+b) == 20 or a == 20 or b == 20:
		print('20')
		return True
	else:
		print('Not 20')
		return False
func3(30,10)
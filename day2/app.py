input = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,19,6,23,2,6,23,27,2,27,9,31,1,5,31,35,1,35,10,39,2,39,9,43,1,5,43,47,2,47,10,51,1,51,6,55,1,5,55,59,2,6,59,63,2,63,6,67,1,5,67,71,1,71,9,75,2,75,10,79,1,79,5,83,1,10,83,87,1,5,87,91,2,13,91,95,1,95,10,99,2,99,13,103,1,103,5,107,1,107,13,111,2,111,9,115,1,6,115,119,2,119,6,123,1,123,6,127,1,127,9,131,1,6,131,135,1,135,2,139,1,139,10,0,99,2,0,14,0]
n = 4

# my_list = [input[i * n:(i + 1) * n] for i in range((len(input) + n - 1) // n )]  

test = [1,1,1,4,99,5,6,0,99]

def sum(num1: int, num2: int):
	return (num1 + num2)

def product(num1: int, num2: int):
	return (num1 * num2)

# def split_list(list: list):
# 	return([list[i * n:(i + 1) * n] for i in range((len(list) + n - 1) // n )])

def app(raw: list):
	# raw_copy = raw
	# input = split_list(raw_copy)
	index = [i for i in range(0, len(raw), 4)]
	for i in range(len(raw)):
		if i in index and raw[i] == 99:
			return raw
		elif i in index and raw[i] == 1:
			raw[raw[i+3]] = sum(raw[raw[i+1]], raw[raw[i+2]])
			# input = split_list(raw_copy)
		elif i in index and raw[i] == 2:
			raw[raw[i+3]] = product(raw[raw[i+1]], raw[raw[i+2]])
			# input = split_list(raw_copy)
print(app(input)[0])
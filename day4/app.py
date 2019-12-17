input = "245318-765747"
input = input.split('-')

def check_password(password: str, check_adjacent_digits_func):
	# check if password have 6 digits and is increasing
	if len(password) != 6 or any(password[i] > password[i+1] for i in range(len(password)-1)):
		return False
	digits = [password.count(digit) for digit in set(password)]
	# return true if there is any double
	return any(check_adjacent_digits_func(int(digit)) for digit in digits)

part_1 = sum(check_password(str(password), lambda x: x >= 2) for password in range(int(input[0]), int(input[1])+1))
part_2 = sum(check_password(str(password), lambda x: x == 2) for password in range(int(input[0]), int(input[1])+1))

print(part_1)
print(part_2)

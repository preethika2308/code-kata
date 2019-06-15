input_string = input()
cout = 0
for s in input_string:
	if s.isdigit() == False and s.isalpha() == False and s.isspace() == False:
		cout = cout + 1

print(cout)

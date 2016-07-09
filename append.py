emails = []

try:
	email_file = open('emails.txt','r')
	for line in email_file:
		emails.append(line.strip())
except IOError:
	print("You made a mistake.")		
	

print(emails)		


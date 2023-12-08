import string
import random

letters_a_to_z = list(string.ascii_lowercase + string.ascii_uppercase)
special_sign = list(string.punctuation)
numbers = list(string.digits)

PW = []

pw_ready = False

length = int(input("Wielang soll ihr Passwort sein: "))
number_special = int(input("Wieviele sonderzeichen soll es enthalten: "))
number_numbers = int(input("Wieviele Zahlen soll es enthalten: "))
while length > 0:
	while number_special > 0:
		asciinr = random.randint(1, 31)
		PW.append(special_sign[asciinr])
		length = length - 1
		number_special = number_special - 1
	while number_numbers > 0:
		asciinr = random.randint(0, 9)
		PW.append(numbers[asciinr])
		number_numbers = number_numbers - 1
		length = length - 1
	PW.append(random.choice(letters_a_to_z))
	length = length - 1
random.shuffle(PW)	
password = ''
for char in PW:
	password += char
print(password)





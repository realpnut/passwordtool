import random
import string
import pyperclip

R = "\033[31m"
RST = "\033[0m"
rnd = str(random.randint(0, 9999))

words = ["dog", "cat", "poop", "loop", "scoop", "peanut",rnd,"putin", "china", "covid", "gay", "poopster","cloud", "england", "osama", "obama", "poland", "apple","orange","grape","melon","lemon","cherry","pear","plum","peach","mango","kiwi","banana","carrot","tomato","potato","onion","garlic","cabbage","lettuce","spinach","table","chair","window","door","floor","ceiling","bridge","road","train","bicycle","phone","camera","laptop","book","paper","pen","pencil","riverbank","sunrise","sunset","island","desert","volcano","castle","temple","garden","market","school","hospital","airport"]

menu = """
	+------------------------+
	|   Password Tool v 0.1  |
	| 1. password generator	 |
	| 2. strength check	 |
	| 3. passphrase generator|
	| 4. password manager	 |
	| 0. exit		 |
	+------------------------+
	
"""

def pgen():
	x = int(input("How much words do you want?: "))
	if x <= 2:
		print(R + "Error" + RST + ": Passphrase must be at least 3 words long!")
		return
	stg = int(input("How strong you want your password to be? (1-3): "))
	if stg == 3:
		pas = "".join(
			c.upper() if random.random() < 0.5 else c
			for c in "-".join(random.sample(words, x))
			)
		print(pas)
	elif stg == 2:
		pas = "".join(
			c.upper() if random.random() < 0.2 else c
			for c in "-".join(random.sample(words, x))
			)
		print(pas)
	elif stg == 1:
		pas = "-".join(random.sample(words, x))
		print(pas)
		pyperclip.copy(pas)
		print("Passphrase copied to clipboard!")
	else:
		print(R + "Error" + RST + ": Wrong option!")

def chkstg():
	password = input("Enter password: ")
	length = len(password)
	has_upper = any(c.isupper() for c in password)
	has_lower = any(c.islower() for c in password)
	has_digit = any(c.isdigit() for c in password)
	has_special = any(not c.isalnum() for c in password)
	score = 0
	if length >= 8:
		score += 1
	if length >= 12:
		score +=1
	if has_upper:
		score += 1
	if has_lower:
		score += 1
	if has_digit:
		score += 1
	if has_special:
		score += 1
	if score == 1:
		print(f"{R}VERY WEAK PASSWORD CHANGE IT RIGHT NOW!!!{RST} (1/6)")
	elif score == 2:
		print(f"Weak password (2/6)")
	elif score <= 3:
 		print(f"Medium password ({score}/6)")
	else:
		print(f"Strong password ({score}/6)")
def gen():
	leng = int(input("Input password lenght: "))
	if leng <= 4:
		print(R + "Error" + RST + ": Password has to be at least 5 characters long!")
		return
	lwc = input("Do you want lowercase letters in your password? (y/n): ")
	lwc = lwc.lower()
	upc = input("Do you want uppercase letters in your password? (y/n): ")
	upc = upc.lower()
	nub = input("Do you want numbers in your passsword? (y/n): ")
	nub = nub.lower()
	spc = input("Do you want special characters in your password? (y/n): ")
	spc = spc.lower()
	pwd = ""
	if lwc == "y" or lwc == "yes":
		pwd += string.ascii_lowercase
	if upc == "y" or upc == "yes":
		pwd += string.ascii_uppercase
	if nub == "y" or nub == "yes":
		pwd += string.digits
	if spc == "y" or spc == "yes":
		pwd += string.punctuation
	if not (lwc in ["y", "yes"] or
        upc in ["y", "yes"] or
        nub in ["y", "yes"] or
        spc in ["y", "yes"]):
		print(R + "Error" + RST + ": You must select at least one 'y' option!")
		return
	pwd = "".join(random.choice(pwd) for _ in range(leng))
	print("Your password is: " + pwd)
	pyperclip.copy(pwd)
	print("Password copied to clipboard!")

def pwdmng():
	www = input("Website: ")
	name = input("Login: ")
	paswd = input("Password: ")
	with open("passwords.txt", "a") as f:
		f.write(f"{www} | {name} | {paswd}\n")

while True:
	print(menu)
	try:
		opt = int(input("Option: "))
	except ValueError:
		print(R + "Error" + RST + ": Enter a number!")
		continue 
	if opt == 1:
		gen()
	elif opt == 2:
		chkstg()
	elif opt == 4:
		pwdmng()
	elif opt == 3:
		pgen()
	elif opt == 0:
		print("Leaving...")
		break
	else:
		print(R + "Error" + RST + ": Choose correct option!")


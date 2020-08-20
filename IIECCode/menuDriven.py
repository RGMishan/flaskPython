import pyttsx3
import os

print("IIEC Python Specialization With Flask")
print("TASK: Create a menu driven program to run OS application\n with the knowledge gained from till date sessions\n.")

print("\nWelcome to Menu Driven Program.\n")
pyttsx3.speak("Welcome to Menu Driven Program.\n")

print("Please enter your name : "  , end='')
name = input()

#ask if user want tutorial
while True:
	print("\nWant to go through tutorial ??")
	print("'Y' for yes / 'N' for no: \t", end="")
	tu = input()
	if (tu == 'n' or tu == "N" ):
		while True:

			#category selection
			os.system("cls")
			print("\nPlease choose the category to work on today", name)
			print("\n1. MS Office\t\t\t2. Text Editors\n3. Design and Animation\t\t4. Exit for today\n")
			c = int(input())
			
			#ms office category
			if(c == 1):
				print("We have two app in this category\n 1. Excel\t2. Powerpoint\n")
				print("Command Me What You Want????\n")
				print("->", end='')
				p = input()
				checker = ("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p)
				negetive = ("do not" in p) or ("don't" in p) or ("dont" in p) or ("not " in p)
				if (negetive):
					print("Sure")
				elif (checker) and ("excel" in p):
					os.system("excel")
				elif (checker) and ("powerpoint" in p) or ("power point" in p):
					os.system("powerpnt")

			#text editor category
			elif(c == 2):
				print("We have two app in this category\n 1. Notepad\t2. Wordpad\n")
				print("Command Me What You Want????\n")
				print("->", end='')
				p = input()
				negetive = ("do not" in p) or ("don't" in p) or ("dont" in p) or ("not " in p)
				if (negetive):
					print("Sure")
				elif (checker) and ("notepad" in p) or ("note pad" in p):
					os.system("notepad")
				elif (checker) and ("wordpad" in p) or ("word pad" in p):
					os.system("wordpad")
				else:
					print("Can't run that Command")

			#drawing and animation category
			elif(c == 3):
				print("We have two app in this category\n 1. Photoshop\t2. Animate\n")
				print("Command Me What You Want????\n")
				print("->", end='')
				p = input()
				negetive = ("do not" in p) or ("don't" in p) or ("dont" in p) or ("not " in p)
				if (negetive):
					print("Sure")
				elif (checker) and ("photoshop" in p) or ("photoshop" in p):
					os.system("photoshop")
				elif (checker) and ("animate" in p):
					os.system("animate")

			elif(c == 4):
				print("Thank You For Using The Program\n")
				exit(0)

			else:
				print("Incorrect Keyword")

#tutorial part
	else:
		print("- As the program start to run it will ask the category of app.")
		print("- You have to select which category you want to get in.")
		print("- Then there will be two app in each category.")
		print("- You can command the program in text to run the listed applications.")
		print("- For Example -> run/execute photoshop for me.")
		print("- Then the app will open and you can work on it.")
		print("- END OF TUTORIAL!!! THANK YOU ENJOY THE PROGRAM\n")
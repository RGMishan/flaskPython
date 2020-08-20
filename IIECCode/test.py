import pyttsx3
import os

printf("Welcome to Menu Driven Program.\n")
pyttsx3.speak("Welcome to Menu Driven Program.")

print("Please enter your name : "  , end='')
name = input()
print("What do you want be to work on today", name, "?")
print("")
print("->", end='') 
p = input()
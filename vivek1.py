import os
import time
import webbrowser

def clear():
    os.system('clear')

clear()
print("Loading...")
for i in range(5):
    print(".")
    time.sleep(1)

clear()
print("Script By Vivek")
print("1. Updates")
print("2. Website")
print("3. More tools")

choice = input("Enter your choice: ")

if choice == '1':
    print("Error message")
elif choice == '2':
    webbrowser.open("http://www.google.com")
elif choice == '3':
    print("No updates")
else:
    print("Invalid choice")

print("\nMade by Vivek")

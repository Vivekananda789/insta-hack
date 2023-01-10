import time
import webbrowser

print("Loading...")
time.sleep(5)
print("Welcome To Vivek Script")
print("1. Insta-Hack")
print("2. Attack")
print("3. Exit")

user_input = input("Enter a choice: ")

if user_input == "1":
    webbrowser.open_new_tab("about:blank")
elif user_input == "2":
    print("Error: Attack option is not available.")
elif user_input == "3":
    print("Exiting...")
    exit()
else:
    print("Invalid choice. Exiting...")
    exit()

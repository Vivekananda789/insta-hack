while True:
    # Get the input from the user
    input_string = input("Enter a calculation: ")

    # Check if the input is 'q' to quit
    if input_string == 'q':
        break

    # Try to evaluate the input as a Python expression
    try:
        result = eval(input_string)
    except Exception as e:
        print("Invalid input:", e)
    else:
        print("Result:", result)

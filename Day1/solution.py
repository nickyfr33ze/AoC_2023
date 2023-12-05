with open('Day1/input.txt', 'r') as file:   # Opens the file, and stores it in 'file'
    strings = file.read()              # Reads the file, and stores it in 'strings'
    
    # Iterate through the file, line by line, and find the first and last number to add together.
    # If there is only 1 number in the line, that is the answer for that line.

    total_sum = 0
    for line in strings:                   # Iterate through the list of strings
        for i in line:                  # Iterate through each character in the passed string
            if i.isdigit():      # Check if the character is a digit
                total_sum += int(i)                # Add the integer to the list of first numbers
                break                      # Exit the loop 
            else: 
                continue
        for i in reversed(line):        # Iterate through the string in reverse
            if i.isdigit():      # Check if the character is a digit
                total_sum += int(i)                # Add the integer to the list of last numbers
                break                      # Exit the loop
            else:
                continue
    print("The total is " + str(total_sum) + ".")

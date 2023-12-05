# Advent of Code 2023 Day 1 Part 2!
# HUGE thanks to gamerplant3 @ https://github.com/gamerplant3 who was a HUGE help with this!
# I was stuck on this for a while, and he helped me out a lot! I highly recommend you check out his GitHub for help with these puzzles!

file = open('Day1/day_01_input.txt', 'r') # import the txt file and reads each line into a list of strings
lines = file.read().splitlines()

new_two_digits_lines = []                  # List of lines that have 2 digits as output

for i in range(len(lines)):
    # check for integers from part 1
    locations = [k for k, x in enumerate(lines[i]) if x.isdigit()]   # Returns index for each pair of [index, value] if value of char is a digit
    firstInt = lines[i][locations[0]]       # Stores the first digit in 'firstInt'
    lastInt = lines[i][locations[len(locations) - 1]]   # Stores the last digit in 'lastInt'
    
    # letter check for part 2
    wordNumbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']   # List of words that represent numbers
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']   # List of numbers that represent numbers for conversion
    zippedNumbers = list(zip(wordNumbers, numbers))   # Zip the two lists together. Think of it like a zipper on a jacket. It zips the two lists together into one.
    
    flatNumbers = []   # Create a new list to store the zipped list in
    for n in range(len(wordNumbers)):
        asFlat = [item for item in zippedNumbers[n]]   # Converts the zipped list into a flat list
        flatNumbers.append(asFlat)
    
    
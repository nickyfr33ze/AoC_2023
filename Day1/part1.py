# Advent of Code 2023 Day 1
# HUGE thanks to gamerplant3 @ https://github.com/gamerplant3 who was a HUGE help with this!
# I was stuck on this for a while, and he helped me out a lot! I highly recommend you check out his GitHub for help with these puzzles!


file = open('Day1/input.txt', 'r')        # Opens the file, and stores it in 'file'
lines = file.read().splitlines()          # Reads the file, and stores it in 'strings'
two_digits_lines = []                     # List of lines that have 2 digits as output

for i in range(len(lines)):               # Loops through all the lines
    locations = [k for k, x in enumerate(lines[i]) if x.isdigit()]   # Returns index for each pair of [index, value] if value of char is a digit
    first = lines[i][locations[0]]         # Stores the first digit in 'first'
    last = lines[i][locations[len(locations) - 1]]   # Stores the last digit in 'last'
    two_digits_lines.append(int(first + last))   # Adds the first and last digit to the list 'two_digits_lines'

answer = sum(two_digits_lines)             # Sums all the digits in 'two_digits_lines'
print("Part 1 answer = " + str(answer))    # Prints the answer to part 1
import sys

if len(sys.argv) < 2:
    print("Error")
    sys.exit(1)

input_string = sys.argv[1]
ascii_sum = sum(ord(char) for char in input_string)
print(ascii_sum) 

"""
Luis Ramirez
Module 08 Programming Assignment


This program prints a movie quote from a text file.
"""
FILE_NAME = 's24_ramirez.md'
try:
    with open(FILE_NAME, 'r') as file:
        # Read file
        contents = file.read()
        # Print contents
        print(contents)
except FileNotFoundError:
    print(f"Error: File '{FILE_NAME}' not found.")
except Exception as e:
    print(f"Error: {str(e)}")
📘 Task 1: Read and Display File Content
Description

This Python program reads the contents of a text file named sample.txt and prints each line with its corresponding line number.
It also handles errors gracefully if the file does not exist.

Features

Opens and reads the file line by line.

Displays each line with its line number for clarity.

Uses exception handling (try-except) to manage file-related errors.

Provides a clear error message if the file is missing.

Example

If sample.txt contains:

How are you?
Hope you are fine


Program Output:

Line 1 : How are you?
Line 2 : Hope you are fine

📝 Task 2: Write, Append, and Read from a File
Description

This Python program demonstrates how to write, append, and read data from a file named output.txt.
It first writes user input to the file, then appends additional text, and finally displays the complete file content.

Features

Prompts the user for input and writes it to output.txt.

Appends new data to the same file without overwriting previous content.

Reads and displays the final contents of the file.

Uses context managers (with open(...)) for safe and automatic file handling.

Example

Input / Output:

Enter text to write to the file: Hello, Python.
Data successfully written to output.txt

Enter additional text to append: Learning file handling in python.
Data successfully appended.

Final content of output.txt:
Hello, Python.
Learning file handling in python.

💡 How to Run

Make sure the program file (e.g., file_read.py or file_write_append.py) is in the same directory as your terminal or IDE.

Run the program using:

python filename.py


Follow the on-screen prompts to test file operations.

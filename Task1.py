# Try to open and read the file
try:
    with open("sample.txt", "r") as file:
        print("Contents of sample.txt:\n")
        for line in file:
            print(line.strip())  # strip() removes extra newline characters
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
except Exception as e:
    print("An unexpected error occurred:", e)

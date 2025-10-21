# Try to open and read the file
try:
    with open("sample.txt", "r") as file:
        line_number = 1
        for line in file:
            print(f"Line {line_number} : {line.strip()}")
            line_number += 1
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
except Exception as e:
    print("An unexpected error occurred:", e)

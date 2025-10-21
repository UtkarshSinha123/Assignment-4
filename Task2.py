# Step 1: Take input from the user and write to the file
text_to_write = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(text_to_write + "\n")

print("Data successfully written to output.txt\n")

# Step 2: Append additional data to the same file
additional_text = input("Enter additional text to append: ")

with open("output.txt", "a") as file:
    file.write(additional_text + "\n")

print("Data successfully appended.\n")

# Step 3: Read and display the final content of the file
print("Final content of output.txt:")

with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())

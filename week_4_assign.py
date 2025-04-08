#Code open a file

with open("content.txt", "r") as file:
    content = file.read() #reads the entire file
    print(content)

#Writing a modified version to a new file.   

with open("information.txt", "w") as file:
    file.write("Welcome to Python!, brace yourself for a new adventure.")


# Error Handling

try:
    with open("database.txt", "r") as file:
        data = file.read()

except FileNotFoundError:
    print("File not found. Please check the filename.")
finally:
    print("Operation completed.")
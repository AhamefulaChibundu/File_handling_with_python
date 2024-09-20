# Writing in a file
with open("my_file.txt", "w" ) as file:
    file.write("Creating a new file named my_file.txt \n")
    file.write("if the file existed before 'w' will overwrite the content of the file\n")
    file.write("I do not need to close the file because 'with' clause will mamke it close automatically\n")
    file.write(str(123))
    file.write("\n")

# reading the file.
with open("my_file.txt", "r") as file:
    content = file.read()
    print(content)

# Appending a file.
with open("my_file.txt", "a") as file:
    file.write("Append add contents to the file without overwriting the file contents\n")
    file.write("Makes file handling easy\n")
    file.write("This is cool\n")

# Handling file error
try:
    with open("unknown_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File does not exist")
except PermissionError:
    print("you do not have permissions for this file")
except Exception as e: # Handles any other exception not stated above
    print(e)

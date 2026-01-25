user_input = input("Enter text to write to the file.")
try:
    with open("output.txt", "wt") as fh:
        fh.write(user_input)
        fh.write("\n")
    user_append_input = input("Enter additional text to append: ")
    with open("output.txt", "at") as fh:
        fh.write(user_append_input)
        fh.write("\n")
    with open("output.txt", "rt") as fh:
        data = fh.read()
except FileNotFoundError:
    print(f"Error: The file was not found")
except Exception as e:
    print(f"Error occurred while performing operations on file: {e}")
else:
    print(f"Final content of 'output.txt':\n{data}")

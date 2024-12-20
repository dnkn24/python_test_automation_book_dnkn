# file=open("file.txt")
#handling exceptions that we can't control
try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found!")

print("Showing when an exception happens")
try:
    print(2/0)
except ZeroDivisionError as error:
    print(f"An error happened: {error}")
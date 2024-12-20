line = 0

try:
    with (open("../03_file_handling_and_regex/assets/file1.txt", "r") as file):
        while True:
            content=file.readline()
            print(f"content: {content}")
            if content:
                line += 1
                if content == "I remove everything\n":
                    break
            else:
                break
        print(f"line: {line}")
except FileNotFoundError:
    print("File not found!")

try:
    with (open("../03_file_handling_and_regex/assets/file1.txt", "r") as file):
        while True:
            file.seek(line)
            content=file.readline()
            if content:
                print(f"content: {content}")
                break
except FileNotFoundError:
    print("File not found!")
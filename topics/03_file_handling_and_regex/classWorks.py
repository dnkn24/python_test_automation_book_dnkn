# file=open("file.txt")
#handling exceptions that we can't control
try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found!")
# finally:
#     file.close()

print("Showing when an exception happens")
my_dict ={"bla": "foo", "John": "Doe"}
my_list=["1","2"]

try:
    # print(my_list[2])
    # print("Concatenate string with integer: " +10)
    print(my_dict["not_existing"])
    print(my_list[2])
#exception error is depending on what line is set first in TRY part
    print(2/0)
except ZeroDivisionError as error:
    print(f"An error happened: {error}")
except TypeError as error:
    print(f"TypeError: {error}")
except IndexError as error:
    print(f"IndexError: {error}")

except KeyError as error:
    print(f"KeyError: {error}")


print("Showing when an exception happens 2nd block")
my_dict ={"bla": "foo", "John": "Doe"}
my_list=["1","2"]

try:
    # print(2 / 0)
    # # print(my_list[2])
    # #print("Concatenate string with integer: " +10)
    # print(my_dict["not_existing"])
    # print(my_list[2])
    print("Showing when an exception happens")
#exception error is depending on what line is set first in TRY part

except Exception as error: # general exception will be called in any case; it's not a good practice to use this generic exception
    print(f"An error happend: {error}")
except IndexError | KeyError as error:
    print(f"An error happened: {error}")
except TypeError as error:
    print(f"TypeError: {error}")
finally:
    print(f"This block will ALWAYS be executed")



#CONTEXT MANAGER
# instead of opening and closing the files, it is better to use WITH operator
# with - it's the way to use the context manager

try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found!")
#there is no need to close the file since we use context manager by calling "with" operator

try:
    with open("../03_file_handling_and_regex/assets/file1.txt", "a+") as file:
       # content = file.read() #will bring all the content as a string
       # content_list= file.readlines() #bring each ling inside a list
       #content_by_line=file.readline()
       #line_1 = file.readline()
       # print("----")
       # # line_2 = file.readline()
       # # line_3 = file.readline()
       # content = file.read()
       # print(content)
       #print(content_list)
       #print(content_by_line)
       # print(line_1)
       # print(line_2)
       # print(line_3)

        file.write("\nI remove everything")

        for i in range(10):
           file.write(f"\n Write line {i}")
        while True:
            content = file.readline()
            if content:
                print(content)
            else:
                break

except FileNotFoundError:
    print("File not found!")
#there is no need to close the file since we use context manager by calling "with" operator
print("finished!")
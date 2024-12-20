print("it's my module")

class some_class:
    def my_function_from_my_module(word):
        return f"Printing the word: {word}"
    my_function_from_my_module('tralala')

    def __my_private_function(param):
        return param
    #we override magic function
    def __str__(self):
        print(f"Print whatever i want")
    def __this_is_my_dunder_method__(self):
        print("this is my dunder method")


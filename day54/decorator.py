import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before
        function()
        # Do something after

    return wrapper_function


# Syntactic sugar
@delay_decorator
def say_hello():
    print("Hello")


@delay_decorator
def say_bye():
    print("Bye")


def say_greeting():
    print("How are you?")


say_bye()
say_greeting()
say_hello()

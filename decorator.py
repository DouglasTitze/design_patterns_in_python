from functools import wraps


def make_blink(function):
    """Defines the decorator"""

    # This makes the decorator transparent in terms of its name and docs
    @wraps(function)

    # Define the inner function
    def decorator():
        # Get the return value of the function to be decorated
        ret = function()

        # Add new functionality to the function being decorated
        return "<blink>" + ret + "</blink>"

    return decorator


def hello_world():
    """Original function"""

    return "Hello, World!"


print(hello_world())  # Original output


# You do not have to redefine hello_world, but simply just place the @decorator_funciton_name above the function you would like to decorate
@make_blink
def hello_world():
    """Original function"""

    return "Hello, World!"


print(hello_world())  # Decorator output

class Korean:
    """Korean speaker"""

    def __init__(self):
        self.language = "Korean"

    def speak_korean(self):
        return "An-neyong?"


class British:
    """English speaker"""

    def __init__(self):
        self.language = "English"

    def speak_english(self):
        return "Hello"


class Adapter:
    """This changes the gaenaric method to an individualized method"""

    def __init__(self, obj, **adapted_method):
        """Change the name of the method"""
        self._obj = obj

        # Add a new dict item that establishes the mapping between name and language
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        return getattr(self._obj, attr)


objects = []

korean = Korean()
british = British()

# Place the instance of each class into the objects array
# Change the speak_language() method to just speak() when calling from inside of the array
objects.append(Adapter(korean, speak=korean.speak_korean))
objects.append(Adapter(british, speak=british.speak_english))

for obj in objects:
    print(obj.language, "says", obj.speak())

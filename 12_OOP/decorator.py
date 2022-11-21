
def uppercase(func_as_param):
    def biggy():
        text = func_as_param()
        return text.upper()

    return biggy


@uppercase
def get_string():
    return "eeeesdafasdf"


print(get_string())

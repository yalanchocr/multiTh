x = 'global x'


def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)  # Prints 'inner x'

    inner()
    print(x)  # Prints 'outer x'


print(x)  # Prints 'global x'
x = 'global x'


def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)  # Prints 'inner x'

    inner()
    print(x)  # Prints 'outer x'

outer()
print(x)  # Prints 'global x'

https://github.com/thanhit95/multi-threading/blob/main/python/demo08a_return_value.py
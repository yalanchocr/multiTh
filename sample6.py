# Global namespace

def my_function():
    # Local namespace
    # x = 20  # Local variable
    print("Local x:", x)


x = 10  # Global variable

my_function()  # Output: Local x: 20

print("Global x:", x)  # Output: Global x: 10
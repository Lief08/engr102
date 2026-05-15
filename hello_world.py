class HelloWorld:
    def __init__(self):
        print("Hello World")

    def print_message(self):
        print("Hello World")


# Usage example
if __name__ == "__main__":
    # Option 1: Print on instantiation
    hw = HelloWorld()
    
    # Option 2: Print using method
    hw.print_message()
def hello(to):
    return f"Hello {to}!"

def goodbye(to):
    print("Please to meet you.")
    return f"Goodbye {to}!"

def main():
    user = input("Name: ")
    print(hello(user))
    print(goodbye(user))
          

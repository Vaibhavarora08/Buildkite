import sys

def greet(name="World"):
    message = f"Hello, {name}!"
    print(message)
    return message

if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "World"
    greet(name)
    print("Pipeline ran successfully!")

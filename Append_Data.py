def write_to_file(filename):
    user_input = input("Enter text to write to the file: ")
    with open(filename,'w') as file:
        file.write(user_input + '\n')
    print(f"Data successfully written to {filename}")

def append_to_file(filename):
    additional_input = input("Enter additional text to append: ")
    with open(filename,'a') as file:
        file.write(additional_input)
    print(f"Data successfully appended to {filename}")

def display(filename):
    print(f"Final content of {filename}:")
    try:
        with open(filename,'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")


filename = 'output.txt'
write_to_file(filename)
append_to_file(filename)
display(filename)
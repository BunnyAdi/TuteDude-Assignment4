def read_file(filename):
    try:
        with open(filename,'r') as txt:
            print(txt.read())
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")

read_file('Sample.txt')






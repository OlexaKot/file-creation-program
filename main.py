# File creation program

def create():
    amount = int(input("Amount of files: "))
    parent_folder = input("Parent folder's path: ")
    prefix = input("File name prefix: ")
    extension = input("Extension (example: \".txt\"): ")
    for file in range(1, amount+1):
        with open(parent_folder + "\\" + prefix + str(file) + extension, "w"):
            pass
    print("Files created.")

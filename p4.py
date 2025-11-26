import os  # Importing the 'os' module to interact with the operating system

def print_directory_contents(path):
    """
    This function prints all files and folders present in the given directory path.
    """
    try:
        # os.listdir(path) returns a list of all entries (files + subdirectories)
        entries = os.listdir(path)

        # Printing the directory name
        print(f"Contents of directory '{path}':")

        # Loop through each item in the directory and print its name
        for entry in entries:
            print(entry)

    # Handling common errors that may occur
    except FileNotFoundError:
        # Raised if the directory does not exist
        print(f"The directory {path} does not exist.")
    except NotADirectoryError:
        # Raised if the given path is not a directory
        print(f"The path {path} is not a directory.")
    except PermissionError:
        # Raised if the program doesn’t have permission to access the directory
        print(f"Permission denied to access the directory {path}.")
    except OSError as e:
        # Catches any other OS-related errors
        print(f"An error occurred: {e}")

# Main program starts here
if __name__ == "__main__":
    # Ask the user to enter the directory path
    dir_path = input("Enter directory path (leave empty for current directory): ").strip()

    # If no input is given, use the current directory (".")
    if not dir_path:
        dir_path = "."

    # Call the function to print directory contents
    print_directory_contents(dir_path)

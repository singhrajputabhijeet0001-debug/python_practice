import os

def print_directory_contents(path):
    try:
        entries = os.listdir(path)
        print(f"Contents of directory '{path}':")
        for entry in entries:
            print(entry)
    except FileNotFoundError:
        print(f"The directory {path} does not exist.")
    except NotADirectoryError:
        print(f"The path {path} is not a directory.")
    except PermissionError:
        print(f"Permission denied to access the directory {path}.")
    except OSError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    dir_path = input("Enter directory path (leave empty for current directory): ").strip()
    if not dir_path:
        dir_path = "."  # current directory
    print_directory_contents(dir_path)

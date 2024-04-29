from pathlib import Path
from colorama import Fore
import sys;

def print_directory(path,depth = 1):
    if depth == 1:
        print(Fore.BLUE  + path.name + '/' + Fore.RESET)

    margin = "\t" * depth
    for items in path.iterdir():
        if items.is_dir():
            print(Fore.BLUE  + margin+ items.name + '/' + Fore.RESET)
            print_directory(items,depth + 1)
        else:
            print(margin + items.name)

if len(sys.argv) < 2:
    raise ValueError("directory path is required")

directory = Path(sys.argv[1])
if not (directory.exists() and directory.is_dir()):
    raise ValueError("path must be set to existing directory")

print_directory(directory)
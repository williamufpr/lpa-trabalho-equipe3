import subprocess
import os
from loaddata import load_data
from listdata import print_rows

def call_cowsay(message):
    # Call the cowsay utility with the given message
    result = subprocess.run(['cowsay', '-f', 'dragon', message], capture_output=True, text=True)
    
    # Print the output
    print(result.stdout)
    
def main():
    call_cowsay("Welcome to the Data Loader!")
    data_folder = './data'
    files = os.listdir(data_folder)
    print("Available files:")
    for file in files:
        print(file)
    
    filename = input("Please provide the file name from the data folder to use: ")
    mydatatable = load_data(os.path.join(data_folder, filename), 10)
    print_rows(mydatatable, 7)
    
if __name__ == "__main__":
    main()

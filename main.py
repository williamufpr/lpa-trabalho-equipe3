import subprocess
import os
from loaddata import load_data
from listdata import print_rows
from initlog import initlog

def call_cowsay(message):
    # Call the cowsay utility with the given message
    result = subprocess.run(['cowsay', '-f', 'dragon', message], capture_output=True, text=True)
    
    # Print the output
    print(result.stdout)
    
def main():
    call_cowsay("Welcome to the Data Loader!")
    data_folder = './data'
    log_handle = initlog('config.env')
    log_handle.write("Data Loader started\n")
    files = os.listdir(data_folder)
    print("Available files:")
    for file in files:
        print(file)
    
    filename = input("Please provide the file name from the data folder to use: ")
    mydatatable = load_data(os.path.join(data_folder, filename), 10)
    print_rows(mydatatable, 7)
    
    print("back in main")
    log_handle.write("Data loaded from file: {}\n".format(filename))
    log_handle.close()

if __name__ == "__main__":
    main()

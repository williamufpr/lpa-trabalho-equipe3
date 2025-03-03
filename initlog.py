import os
from datetime import datetime
from dotenv import load_dotenv

def initlog(env_file_path='.env'):
    # Load environment variables from the .env file
    load_dotenv(env_file_path)
    
    # Get the logfile path from the environment variables
    logfile_path = os.getenv('logfile')
    
    if not logfile_path:
        raise ValueError("The 'logfile' key is not found in the .env file.")
    
    # Check if the log file exists
    if not os.path.exists(logfile_path):
        # Create the file if it does not exist
        with open(logfile_path, 'w') as f:
            pass
    
    # Open the file in append mode and write a new line with the current timestamp
    log_handle = open(logfile_path, 'a')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    log_handle.write('New log session Started \n')
    log_handle.write(f'{timestamp}\n')
    
    # Return the file handle for further operations
    return log_handle

# Example usage:
# if __name__ == "__main__":
#    log_handle = initlog('config.env')
#    print("Log file initialized and ready for use.")

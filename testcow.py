import subprocess

def call_cowsay(message):
    # Call the cowsay utility with the given message
    result = subprocess.run(['cowsay', '-f', 'dragon', message], capture_output=True, text=True)
    
    # Print the output
    print(result.stdout)

# Example usage
call_cowsay("Hello, world!")
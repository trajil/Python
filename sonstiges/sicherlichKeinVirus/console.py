### CMD ###
import subprocess
def run_command(command):
    try:
        # Run the command, capture the output and error (if any)
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # If the command was successful, print the output
        if result.stdout:
            print("Output:\n", result.stdout)
        
        # If there was an error, print the error
        if result.stderr:
            print("Error:\n", result.stderr)

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

# Example of using the function to install a package with pip
#run_command("pip install requests")
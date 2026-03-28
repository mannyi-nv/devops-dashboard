def check_log():
        #Docstring:
    """
    Inspect log file:
        - file_log shopuld be provided by user input
        - if 'ERROR:' is found in the log file, print the line containing 'ERROR:'
        - if 'ERROR:' is not found, print a message indicating that no errors were found in the log file.
    Note: The function should handle the case where the specified log file does not exist and prompt the user to try again.

    """
    while True:
        try:
            file_log = (input(f"\nPlease provide log file name: "))
            with open(file_log, 'r') as log_file:
                for line in log_file:
                    if 'ERROR:' in line:
                        print(line)
                    else:
                        print(f"\nNo 'ERROR' found in the log file.")
        except FileNotFoundError:
            print(f"\nFile '{file_log}' not found.")
            if input(f"\nDo you want to try again? (YES / NO): ").lower() != 'yes':
                break
        

        

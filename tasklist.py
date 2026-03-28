def manage_tasks():
    #Docstring:
    """
    Task management function:
        - The function should prompt the user to choose a task
        - The function should maintain a list of tasks in memory and offer:
            - Add a task
            - View all tasks
            - Remove a task by number
            - Return to main menu        -
    Note: The function should handle invalid input and provide appropriate error messages.

    """
    while True:
        try:
            print("\n--- Task Manager ---")
            define = f"--- Task Manager ---"
            print("=" * len(define))
            print()
            print(f"1. Add a task")
            print(f"2. View all tasks")
            print(f"3. Remove a task")
            print(f"0. Return to main menu")


            user_choice = input("\nEnter your choice (1-3): ")
            if user_choice == '1':
            #   action = 'add'
              print(f"\nAdding a task...")
            elif user_choice == '2':
              print(f"\nViewing all tasks...")
            elif user_choice == '3':
              print(f"\nRemoving a task...")
            elif user_choice == '0':
              print("Returning to main menu.")
              break
            else:
              print("Invalid choice. Please enter a number between 1 and 3.")
              continue
          
        except Exception as e:
          print(f"An error occurred: {e}")
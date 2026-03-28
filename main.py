import sysinfo
import logcheck
import tasklist

while True:
    try:

        print("\n--- devops-dashboard Main Menu ---")
        define = (f"--- devops-dashboard Main Menu ---")
        print("=" * len(define))
        print()
        print(f"1. System info")
        print(f"2. Log Checker") 
        print(f"3. Task List")
        print(f"0. Exit")
        choice = input("\nSelect an option (1-3): ")

        if choice == "1":
            sysinfo.show_sysinfo()
        elif choice == "2":
            logcheck.check_log()
        elif choice == "3":
            tasklist.manage_tasks()
        elif choice == "0":
            print("\nExiting the program.")
            break
        else:
            print("\nInvalid choice. Please select a valid option (1-3 or 0).")

    except  Exception as e:
        print(f"\nAn error occurred: {e}")
        

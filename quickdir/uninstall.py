import os

# Ask for user confirmation
confirm = input("Are you sure you want to uninstall the program? (y/n): ")
if confirm.lower() != "y":
    print("Uninstallation cancelled.")
else:
    # Delete the qd script
    try:
        os.system('sudo rm /usr/local/bin/qd')  # System-wide installation
    except FileNotFoundError:
        pass
    try:
        os.remove(os.path.expanduser('~/.local/bin/qd'))  # User-specific installation
    except FileNotFoundError:
        pass

    # Delete the shortcuts directory
    shortcuts_dir = os.path.expanduser('~/.shortcuts')
    if os.path.exists(shortcuts_dir):
        try:
            os.system(f'sudo rm -r {shortcuts_dir}')
        except PermissionError:
            print(f"Error: insufficient permissions to delete directory {shortcuts_dir}.")
            print("Please manually delete this directory to complete the uninstallation.")
    print("Program uninstalled successfully.")

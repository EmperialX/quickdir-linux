import sys

def print_logo():
    logo = r"""

________        .__        __    ________  .__        
\_____  \  __ __|__| ____ |  | __\______ \ |__|______ 
 /  / \  \|  |  \  |/ ___\|  |/ / |    |  \|  \_  __ \
/   \_/.  \  |  /  \  \___|    <  |    `   \  ||  | \/
\_____\ \_/____/|__|\___  >__|_ \/_______  /__||__|   
       \__>             \/     \/        \/           


    """
    print(logo)

def display_help():
    print("QuickDir Help Menu")
    print("-------------------")
    print("Usage: qd [command]\n")
    print("Available commands:")
    print("  install     Install QuickDir")
    print("  uninstall   Uninstall QuickDir")
    print("  upgrade     Upgrade QuickDir to the latest version")
    print("  version     Display the current version of QuickDir")
    print("  shortcut    Create a shortcut for a directory path\n")
    print("  go [name]   Quickly navigate to a previously saved directory shortcut")
    print("  help        Display this help menu\n")
    print("For more information, please visit https://github.com/yourusername/quickdir\n")

if __name__ == '__main__':
    display_help()

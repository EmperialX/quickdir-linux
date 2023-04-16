import os
import shutil
import sys

# Define constants
INSTALL_DIR = '/usr/local/bin/quickdir'
SCRIPT_FILE = 'quickdir.py'
ALIAS_FILE = os.path.expanduser('~/.bash_aliases')
ALIAS_LINE = f"alias qd='python3 {INSTALL_DIR}/{SCRIPT_FILE}'\n"

# Copy script file to install directory
try:
    shutil.copy2(SCRIPT_FILE, INSTALL_DIR)
except FileNotFoundError:
    print("Error: quickdir.py not found. Make sure you are running install.py in the same directory as quickdir.py.")
    sys.exit(1)

# Verify that quickdir is executable
try:
    os.chmod(INSTALL_DIR, 0o755)
except OSError:
    print(f"Error: could not make {INSTALL_DIR} executable.")
    sys.exit(1)

# Add alias to bash_aliases file
try:
    with open(ALIAS_FILE, 'a') as f:
        f.write(ALIAS_LINE)
except IOError:
    print(f"Error: could not write alias to {ALIAS_FILE}.")
    sys.exit(1)

# Print success message
print(f'Successfully installed QuickDir at {INSTALL_DIR}')


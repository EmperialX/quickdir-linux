# Quickdir-Linux
QuickDir is a simple command-line interface (CLI) for creating and managing directories. With QuickDir, you can quickly create new directories, list the directories in a parent directory, and manage shortcuts to frequently used directories. 


## Installation
Clone the repository:

```
git clone https://github.com/username/quickdir.git
cd quickdir
```
### Requirements
Install the required packages
```
pip install -r requirements.txt
```

Update and Upgrade:

    sudo apt update && sudo apt upgrade 
   
Install QuickDir:
```
pip install .
```

## Creating Directories

To create a new directory, simply run:

    quickdir [dir_name]

This will create a new directory with the specified name in the current working directory. If you don't specify a directory name, QuickDir will create a directory called "NewDirectory".


You can also specify a parent directory for the new directory using the -p or --parent option:

    quickdir [dir_name] -p [parent_directory]
      

Listing Directories

To list all directories in the current working directory, run:

    quickdir --list
      

You can also list directories in a specific parent directory by specifying the -p or --parent option:

    quickdir --list -p [parent_directory]

## Shortcuts

QuickDir allows you to create shortcuts to frequently accessed directories. Shortcuts are stored in a JSON file located at ~/.quickdir_shortcuts.

To create a shortcut:
```
quickdir add shortcut_name
```

To go to a directory using a shortcut:
```
quickdir go shortcut_name
```

To remove a shortcut:

`Open ~/.quickdir_shortcuts` in a text editor.


Remove the entry for the shortcut you want to remove.

## Package Management

QuickDir can be installed and managed using your system's package manager.

To install QuickDir:
```
quickdir --install
```

To uninstall QuickDir:
```
quickdir --uninstall
```

To upgrade QuickDir:
```

quickdir --upgrade
```


## Help

To get help with QuickDir, run:

    quickdir --help

##  Options

QuickDir supports the following options:

`-p, --parent`: Specify the parent directory for the new directory or the directory to list. By default, the parent directory is the current working directory.

`-l, --list:` List all directories in the parent directory.

`-n, --name:` Specify the name of the shortcut to create or use.

`-d, --directory:` Specify the directory to associate with the shortcut.

`-v, --version:` Show the current version of QuickDir.

`--upgrade:` Upgrade QuickDir to the latest version.

`--install:` Install QuickDir using the system package manager.

`--uninstall:` Uninstall QuickDir using the system package manager.

`--help:` Show the help message.


## Contributing

If you find a bug or have a feature request, please open an issue on the GitHub repository. Pull requests are also welcome.
## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Directory Structure

Here is the directory structure of this project:
```
quickdir-linux/
├── quickdir/
│   ├── __init__.py
│   ├── main.py
│   ├── licenses.py
│   ├── help.py
│   ├── setup.cfg
│   └── quickdir.py
├── install.py
├── uninstall.py
├── changelog.md
├── README.md
└── requirements.txt


```

If you have any questions or concerns, please contact me at [github](https://github.com/EmperialX).

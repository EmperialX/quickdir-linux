#!/usr/bin/env python

import argparse
import os
import subprocess
import sys
import json


VERSION = '1.1.0'
SHORTCUT_FILE = os.path.expanduser('~/.quickdir_shortcuts')


def main():
    parser = argparse.ArgumentParser(description='QuickDir: A simple CLI for creating and managing directories.')
    parser.add_argument('dir_name', nargs='?', default='NewDirectory', help='the name of the directory to create (default: "NewDirectory")')
    parser.add_argument('-p', '--parent', help='the parent directory for the new directory (default: current working directory)')
    parser.add_argument('-l', '--list', action='store_true', help='list all directories in the parent directory')
    parser.add_argument('command', nargs='?', default='create', choices=['create', 'list', 'install', 'uninstall', 'upgrade', 'go', 'add'], help='the command to execute (default: "create")')
    parser.add_argument('-v', '--version', action='store_true', help='show the current version of QuickDir')
    parser.add_argument('--upgrade', action='store_true', help='upgrade QuickDir to the latest version')
    parser.add_argument('--install', action='store_true', help='install QuickDir using the system package manager')
    parser.add_argument('--uninstall', action='store_true', help='uninstall QuickDir using the system package manager')
    parser.add_argument('-d', '--directory', dest='directory', help='the directory to associate with the shortcut (only used with the "go" and "add" commands)')
    parser.add_argument('-n', '--name', help='the name of the shortcut to create (only used with the "go" command)')
    parser.add_argument('-qd', '--quickdir', action='store_true', help='use QuickDir for the command (default: False)')

    args = parser.parse_args()

    if args.version:
        print(f'QuickDir version {VERSION}')
        sys.exit(0)

    if args.install:
        install()
        sys.exit(0)

    if args.uninstall:
        uninstall()
        sys.exit(0)

    if args.upgrade:
        upgrade()
        sys.exit(0)
    if args.command == 'create':
        create_directory(args.dir_name, args.parent)
    elif args.command == 'list':
        list_directories(args.parent)
    elif args.command == 'install':
        install()
    elif args.command == 'uninstall':
        uninstall()
    elif args.command == 'upgrade':
        upgrade()
    elif args.command == 'go':
        go_to_directory(args.name, args.directory)
    elif args.command == 'add':
        add_shortcut(args.name, args.directory)
    else:
     print(f'Error: Unknown command "{args.command}"')


    if args.list:
        list_directories(args.parent)
    elif args.command == 'go':
        go_to_directory(args.name, args.directory)
    elif args.command == 'add':
        add_shortcut(args.name, args.directory)
    else:
        create_directory(args.dir_name, args.parent)


def create_directory(name, parent=None):
    path = os.path.join(parent, name) if parent else name
    try:
        os.mkdir(path)
        print(f'Successfully created directory "{name}"')
    except FileExistsError:
        print(f'Error: Directory "{name}" already exists')


def list_directories(parent=None):
    if not parent:
        parent = os.getcwd()
    directories = os.listdir(parent)
    print('Directories:')
    for directory in directories:
        if os.path.isdir(os.path.join(parent, directory)):
            print(directory)


def install():
    package_manager = get_package_manager()
    if package_manager is None:
        print('Error: Could not find a package manager')
        sys.exit(1)

    subprocess.call([package_manager, 'install', 'quickdir'])
    print('QuickDir installed successfully')

def uninstall():
    print("WARNING: This will delete all QuickDir data. Do you want to continue? (y/N)")
    response = input().strip().lower()
    if response == "y":
        package_manager = get_package_manager()
        if package_manager is None:
            print('Error: Could not find a package manager')
            sys.exit(1)

        subprocess.call([package_manager, 'uninstall', 'quickdir'])
        print('QuickDir uninstalled successfully')
    else:
        print('Uninstall cancelled.')

def upgrade():
    subprocess.call(['pip', 'install', '--upgrade', 'quickdir'])
    print('QuickDir upgraded successfully')

def go_to_directory(name, directory=None):
    if directory is None:
        directory = get_directory_from_shortcut(name)
    if directory is None:
        print(f'Error: Shortcut "{name}" not found')
        sys.exit(1)

    os.chdir(directory)
    print(f'Successfully changed directory to "{directory}"')

def add_shortcut(name, directory):
    shortcuts = load_shortcuts()
    shortcuts[name] = directory
    save_shortcuts(shortcuts)
    print(f'Successfully created shortcut "{name}" for directory "{directory}"')


def load_shortcuts():
    if not os.path.exists(SHORTCUT_FILE):
        return {}
    with open(SHORTCUT_FILE, 'r') as f:
        return json.load(f)

def save_shortcuts(shortcuts):
    with open(SHORTCUT_FILE, 'w') as f:
        json.dump(shortcuts, f, indent=4)

def get_directory_from_shortcut(name):
    shortcuts = load_shortcuts()
    return shortcuts.get(name)

def get_package_manager():
    for manager in ['apt-get', 'dnf', 'yum', 'brew']:
        try:
            subprocess.call(['which', manager], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return manager
        except OSError:
            pass
    return None

if __name__ == '__main__':
    main()

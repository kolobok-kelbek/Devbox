#!/usr/bin/env python3
# encoding: utf-8

import pathlib
import getch
import os
from colorama import Fore, init

init(autoreset=True)


def go_to(path):
    os.system('clear')
    os.chdir(path)
    os.system("bash")
    quit(0)


def get_menu_struct() -> dict:
    return {
        PROJECTS: get_projects(),
        SANDBOX: get_sandbox_list()
    }


def write_menu(menu_items: dict, selected: int):
    count: int = 0
    for name, value in menu_items.items():
        count += 1
        if count == selected:
            print(' -> ' + Fore.CYAN + name)
        else:
            print('    ' + name)


def key_getch():
    return getch.getch()


def create_directories() -> None:
    if not os.path.exists(DEV_DIR):
        os.makedirs(DEV_DIR)

    if not os.path.exists(PROJECTS_DIR):
        os.makedirs(PROJECTS_DIR)

    if not os.path.exists(SANDBOX_DIR):
        os.makedirs(SANDBOX_DIR)


def get_files_in_directory(path: str) -> dict:
    file_names: dict = {}

    for currentFile in pathlib.Path(path).iterdir():
        project_path: str = str(currentFile)
        file_names[os.path.basename(project_path)] = project_path

    return file_names


def get_home_dir() -> str:
    return str(pathlib.Path.home())


def get_projects() -> dict:
    project_dir = get_home_dir() + "/" + PROJECTS_DIR
    return get_files_in_directory(project_dir)


def get_sandbox_list() -> dict:
    sandbox_list = get_home_dir() + '/' + SANDBOX_DIR
    return get_files_in_directory(sandbox_list)


PROGRAM_NAME: str = 'DevBox'
DEV_DIR: str = "Dev"
PROJECTS: str = "projects"
SANDBOX: str = "sandbox"
PROJECTS_DIR: str = DEV_DIR + "/" + PROJECTS
SANDBOX_DIR: str = DEV_DIR + "/" + SANDBOX

index: int = 1
type = None

while True:
    os.system('clear')

    if type is None:
        data: dict = get_menu_struct()
    else:
        data: dict = get_menu_struct()[type]

    length = len(data)

    if index < 1:
        index = length

    if index > length:
        index = 1

    write_menu(data, index)

    key = key_getch()

    if 'q' == key:
        os.system('clear')
        quit(0)

    if 'w' == key:
        index -= 1

        if index < 1:
            index = length

    if 's' == key:
        index += 1

        if index > length:
            index = 1

    if 'a' == key:
        type = None

    if 'd' == key:
        c: int = 0
        items = data.items()

        for name, item in items:
            c += 1
            if c == index:
                if type is None:
                    type = name
                else:
                    go_to(item)
                break

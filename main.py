#!/usr/bin/env python3
# encoding: utf-8

import npyscreen
import pathlib
import os

DEV_DIR: str = "Dev"
PROJECTS = "projects"
SANDBOX = "sandbox"
PROJECTS_DIR: str = DEV_DIR + "/" + PROJECTS
SANDBOX_DIR: str = DEV_DIR + "/" + SANDBOX


class DevBox(npyscreen.NPSAppManaged):
    def onStart(self):
        self.registerForm("MAIN", MainForm())


class MainForm(npyscreen.FormWithMenus):

    def __init__(self, *args, **keywords):
        super().__init__(*args, **keywords)
        if not os.path.exists(DEV_DIR):
            os.makedirs(DEV_DIR)

        if not os.path.exists(PROJECTS_DIR):
            os.makedirs(PROJECTS_DIR)

        if not os.path.exists(SANDBOX_DIR):
            os.makedirs(SANDBOX_DIR)

    def create(self):
        items = []

        self.m1 = self.add_menu(name="Main Menu", shortcut="^M")

        self.m2 = self.m1.addNewSubmenu(PROJECTS, shortcut="^p")
        self.m2.addItemsFromList(self.get_projects_menu_items())

        self.m3 = self.m1.addNewSubmenu(SANDBOX, shortcut="^s")
        self.m3.addItemsFromList(self.get_sandbox_menu_items())

        items.append(("Exit", self.exit_application))

        self.m1.addItemsFromList(items)

    def get_projects_menu_items(self):
        items = []
        for currentFile in pathlib.Path(str(pathlib.Path.home()) + "/" + PROJECTS_DIR).iterdir():
            items.append((os.path.basename(str(currentFile)), None))
        return items

    def get_sandbox_menu_items(self):
        items = []
        for currentFile in pathlib.Path(str(pathlib.Path.home()) + "/" + SANDBOX_DIR).iterdir():
            items.append((os.path.basename(str(currentFile)), None))
        return items

    def exit_application(self):
        self.parentApp.setNextForm(None)
        self.editing = False
        self.parentApp.switchFormNow()


def main():
    devBox = DevBox()
    devBox.run()


if __name__ == '__main__':
    main()

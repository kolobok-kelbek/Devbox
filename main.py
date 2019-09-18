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

# if not os.path.exists(DEV_DIR):
#     os.makedirs(DEV_DIR)
#
# if not os.path.exists(PROJECT_DIR):
#     os.makedirs(PROJECT_DIR)
#
# if not os.path.exists(SANDBOX_DIE):
#     os.makedirs(SANDBOX_DIE)


class MyTestApp(npyscreen.NPSAppManaged):
    def onStart(self):
        self.registerForm("MAIN", MainForm())


class MainForm(npyscreen.FormWithMenus):

    def create(self):
        items = []

        self.m1 = self.add_menu(name="Main Menu", shortcut="^M")

        self.m2 = self.m1.addNewSubmenu(PROJECTS, shortcut="^p")
        self.m2.addItemsFromList(self.get_projects_menu_items())

        self.m3 = self.m1.addNewSubmenu(SANDBOX, shortcut="^s")
        self.m3.addItemsFromList(self.get_sandbox_menu_items())

        items.append(("Exit", self.exit_application))

        self.m1.addItemsFromList(items)

        # self.m2 = self.add_menu(name="Another Menu", shortcut="b", )
        # self.m2.addItemsFromList([
        #     ("Just Beep", self.whenDisplayText("Just Beep")),
        # ])
        #
        # self.m3 = self.m2.addNewSubmenu("A sub menu", "^F")
        # self.m3.addItemsFromList([
        #     ("Just Beep", self.whenDisplayText("Just Beep")),
        # ])

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
    TA = MyTestApp()
    TA.run()


if __name__ == '__main__':
    main()

#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd


class HBNBCommand(cmd.Cmd):

    """class for the cmd interpreter"""

    prompt = "(hbnb)"

    def do_quit(self, line):
        """Exits the command intepreter
        """
        return True

    def do_EOF(self, line):
        """Exits the command interpreter with EOF (Ctrl+D)"""
        return True

    def emptyline(self):
        """Overrides the default behavior of repeating
        the last command on an empty line
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

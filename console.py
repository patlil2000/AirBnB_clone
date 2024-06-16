#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd


class HBNBCommand(cmd.Cmd):

    """The class for the command line interpreter"""

    prompt = "(hbnb)"

    def do_EOF(self, line):
        """quits the program with ctrl+D"""
        return True

    def emptyline(self):
        """Overrides the default behaviour of repeating
        lines
        """
        pass

    def do_quit(self, line):
        """Exits the program.
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

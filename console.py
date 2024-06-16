#!/udr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Exits the command intepreter"""
        return True

    def do_EOF(self, arg):
        """Exits the command interpreter with EOF (Ctrl+D)"""
        return True

    def emptyline(self):
        """Overrides the default behavior of repeating 
        the last command on an empty line
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd
from models.base_model import BaseModel
from models import storage

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

    def do_create(self, line):
        """Creates a new instance of BaseModel 
        Saves it to JSON stirng
        prints the id
        """
        if not line:
            print("** class name missing **")
        elif line not in globals():
            print("** class doesn't exist **")
        else:
            new_instance = globals()[line]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance
           based on the classname
           prints the id
        """
        
        if not line:
            print("** class name missing **")
            return
        parts = line.split()
        if len(parts) == 0 or parts[0] not in globals():
            print("** class doesn't exist **")
            return
        if len(parts) < 2:
            print("** instance id missing **")
            return
        class_name = parts[0]
        instance_id = parts[1]
        key = f"{class_name}.{instance_id}"
        object_list = storage.all()
        if key not in object_list:
            print("** no instance found **")
            return
        print(object_list[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if not line:
            print("** class name missing **")
            return
        parts = line.split()
        if len(parts) == 0 or parts[0] not in globals():
            print("** class doesn't exist **")
            return
        if len(parts) < 2:
            print("** instance id missing **")
            return
        class_name = parts[0]
        instance_id = parts[1]
        key = f"{class_name}.{instance_id}"
        object_list = storage.all()
        if key not in object_list:
            print("** no instance found **")
            return
        del object_list[key]
        storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()

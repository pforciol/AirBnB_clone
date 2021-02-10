#!/usr/bin/python3
"""This is the Console module."""
import cmd
import shlex
import models

from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """The Console class of our HBNB project."""
    prompt = "(hbnb) "
    file = None

    errors = {
        "missingClass": "** class name missing **",
        "wrongClass": "** class doesn't exist **",
        "missingID": "** instance id missing **",
        "wrongID": "** no instance found **"
    }

    classes = [
        "BaseModel"
    ]

    def do_quit(self, arg):
        """
        Exits the program.
            usage: quit
        """
        return True

    def do_EOF(self, arg):
        """
        Exits the program.
            usage: EOF (Ctrl+D)
        """
        return True

    def emptyline(self):
        """Handles the emptyline behaviour."""
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it and prints the id.
            usage: create <class_name>
        """
        args = shlex.split(arg)
        if len(args) < 1:
            print(self.errors["missingClass"])
        elif args[0] in self.classes:
            new = eval(args[0])()
            new.save()
            print(new.id)
        else:
            print(self.errors["wrongClass"])

    def do_show(self, arg):
        """
        Prints the string representation of an instance.
            usage: show <class_name> <id>
        """
        args = shlex.split(arg)
        if len(args) < 1:
            print(self.errors["missingClass"])
        elif args[0] in self.classes:
            if len(args) < 2:
                print(self.errors["missingID"])
            else:
                key = args[0] + '.' + args[1]
                if key in models.storage.all().keys():
                    print(models.storage.all()[key])
                else:
                    print(self.errors["wrongID"])
        else:
            print(self.errors["wrongClass"])


if __name__ == "__main__":
    HBNBCommand().cmdloop()

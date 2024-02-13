#!/usr/bin/python3

""" the entry point of the command interpreter """

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Entry to command interpreter """

    prompt = "(hbnb)"
    models = ["BaseModel"]

    def do_EOF(self, line):
        """ Exit on Ctrl-D """
        print()
        return True

    def do_quit(self, line):
        """ Exit on quit """
        return True

    def emptyline(self):
        """ empty line """
        pass

    def do_create(self, line):
        """ Creates a new instance """
        if len(line) == 0:
            print("** class name missing **")
        elif line not in self.models:
            print("** class doesn't exist **")
        else:
            instance = eval(line)()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """ Prints the string representation of an instance """
        if len(line) == 0:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in self.models:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
        else:
            name = "{}.{}".format(args[0], args[1])
            if name not in storage.all().keys():
                print("** no instance found **")
            else:
                print(storage.all()[name])

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] not in self.models:
            print("** class doesn't exist **")
        else:
            name = "{}.{}".format(args[0], args[1])
            if name not in storage.all().keys():
                print("** no instance found **")
            else:
                del storage.all()[name]
                storage.save()

    def do_all(self, line):
        """ Prints all string representation of all instances """
        args = line.split()
        objects = []
        if len(args) == 0:
            for obj in storage.all().values():
                objects.append(obj)
            print(objects)
        elif args[0] in self.models:
            for key, obj in storage.all().items():
                if args[0] in key:
                    objects.append(obj)
            print(objects)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """ Updates an instance attribute """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        elif args[0] not in self.models:
            print("** class doesn't exist **")
        elif ("{}.{}".format(args[0], args[1])) not in storage.all().keys():
            print("** no instance found **")
        else:
            key = "{}.{}".format(args[0], args[1])
            attr = args[2]
            cast = type(eval(args[3]))
            setattr(storage.all()[key], attr, cast(args[3]))
            storage.all()[key].save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()

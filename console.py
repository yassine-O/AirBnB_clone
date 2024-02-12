#!/usr/bin/python3

""" the entry point of the command interpreter """

import cmd


class HBNBCommand(cmd.Cmd):
    """ Entry to command interpreter """

    prompt = "(hbnb)"

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


if __name__ == "__main__":
    HBNBCommand().cmdloop()

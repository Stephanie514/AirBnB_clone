#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """ Defines the HBNBCommand class """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exits the program (Ctrl-D)"""
        print("")
        return True

    def emptyline(self):
        """ No command given """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

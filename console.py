#!/usr/bin/python3
import cmd
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand - Command Interpreter for AirBnB Clone.

    Allows you to interact with the AirBnB Clone data model

    Attributes:
        prompt (str): The command prompt string '(hbnb) '

    Methods:
        do_quit(self, arg): Exits the program.
        do_EOF(self, arg): Exits the program (Ctrl-D).
        emptyline(self): No command given.
        do_create(self, arg): Create a new model instance & save it.
        do_show(self, arg): Show information about an instance.
        do_destroy(self, arg): Delete an instance.
        do_all(self, arg): Show all instances of a class.
        do_update(self, arg): Update an instance attribute.
    """

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

    def do_create(self, arg):
        """Create a new instance of BaseModel and save it to the JSON file"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
        except Exception:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = args[0] + '.' + args[1]
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = args[0] + '.' + args[1]
            if key in objects:
                objects.pop(key)
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of instances"""
        objects = storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
            return
        args = arg.split()
        if args[0] in storage.classes:
            print([str(obj) for key, obj in objects.items()
                  if key.startswith(args[0])])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            objects = storage.all()
            key = args[0] + '.' + args[1]
            if key not in objects:
                print("** no instance found **")
            else:
                obj = objects[key]
                setattr(obj, args[2], args[3].strip('"'))
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

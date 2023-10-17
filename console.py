#!/usr/bin/python3
"""Import cmd, file storage and BaseModel modules"""
import cmd
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

"""Defines the HBNBCommand class"""


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
        """Create a new instance of a BaseModel class and save it to the JSON file"""
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.strip()
        classes = {
            'BaseModel': BaseModel,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
        }

        if class_name in classes:
            new_instance = classes[class_name]()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]

        classes = {
            'BaseModel': BaseModel,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
        }

        if class_name in classes:
            if len(args) < 2:
                print("** instance id missing **")
            else:
                object_id = args[1]
                objects = FileStorage().all()
                key = "{}.{}".format(class_name, object_id)
                if key in objects:
                    print(objects[key])
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]

        classes = {
            'BaseModel': BaseModel,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
        }

        if class_name in classes:
            if len(args) < 2:
                print("** instance id missing **")
            else:
                object_id = args[1]
                objects = FileStorage().all()
                key = "{}.{}".format(class_name, object_id)
                if key in objects:
                    del objects[key]
                    FileStorage().save()
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representations of instances"""
        objects = FileStorage().all()

        if not arg:
            print([str(obj) for obj in objects.values()])
        else:
            args = arg.split()
            class_name = args[0]

            classes = {
                'BaseModel': BaseModel,
                'State': State,
                'City': City,
                'Amenity': Amenity,
                'Place': Place,
                'Review': Review
            }

            if class_name in classes:
                print([str(obj) for key, obj in objects.items() if key.startswith(class_name)])
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]

        classes = {
            'BaseModel': BaseModel,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
        }

        if class_name in classes:
            if len(args) < 2:
                print("** instance id missing **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                object_id = args[1]
                attribute_name = args[2]
                new_value = args[3].strip('"')
                objects = FileStorage().all()
                key = "{}.{}".format(class_name, object_id)
                if key in objects:
                    obj = objects[key]
                    setattr(obj, attribute_name, new_value)
                    obj.save()
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    FileStorage().reload()
    HBNBCommand().cmdloop()

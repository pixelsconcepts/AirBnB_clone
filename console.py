#!/usr/bin/python3
"""Console Intepreter for AirBnB_clone"""
import cmd
import models
from datetime import datetime
import json
import sys


class HBNBCommand(cmd.Cmd):
    """AirBnB Command Intepreter"""
    prompt = "(hbnb) "

    def do_EOF(self, args):
        """"Quit command to exit the program"""
        return True

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Prints empty line, if no argument is passed"""
        pass

    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file),
        and prints the id.
        Usage: create <class name>
        """

        args = args.split()

        if not args or len(args) == 0:
            print("** class name missing **")
            return

        cl_name = args[0]

        if cl_name not in models.storage.classes.keys():
            print("** class doesn't exist **")
            return

        new_instance = models.storage.classes[cl_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """
        Prints the string representation of an instance
        based on the class name and id.
        Usage: show <class name> <id>
        """
        args = args.split()

        if not args or len(args) == 0:
            print("** class name missing **")
            return

        cl_name = args[0]

        if cl_name not in models.storage.classes.keys():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        k = "{}.{}".format(cl_name, instance_id)
        all_instances = models.storage.all()

        if k not in all_instances:
            print("** no instance found **")
            return

        print(all_instances[k])

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        (saves the change into the JSON file).
        Usage: destroy <class name> <id>
        """

        args = args.split()

        if not args or len(args) == 0:
            print("** class name missing **")
            return

        cl_name = args[0]

        if cl_name not in models.storage.classes.keys():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        k = "{}.{}".format(cl_name, instance_id)
        all_instances = models.storage.all()

        if k not in all_instances:
            print("** no instance found **")
            return

        del all_instances[k]
        models.storage.save()

    def do_all(self, args):
        """
        Prints all string representations of all instances based
        or not on the class name.
        Usage: all [<class name>]
        """

        args = args.split()

        if args and args[0] not in models.storage.classes.keys():
            print("** class doesn't exist **")
            return

        if args and args[0]:
            cl_name = args[0]
            objs = models.storage.all().values()
            show_cl = models.storage.classes[cl_name]
            instances = [str(obj) for obj in objs if isinstance(obj, show_cl)]
        else:
            objs = models.storage.all().values()
            instances = [str(obj) for obj in objs]

        print(instances)

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (saves the change into the JSON file).
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """

        args = args.split()

        if not args:
            print("** class name missing **")
            return

        cl_name = args[0]

        if cl_name not in models.storage.classes.keys():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        k = "{}.{}".format(cl_name, instance_id)
        all_instances = models.storage.all()

        if k not in all_instances:
            print("** no instance found **")
            return

        if len(args) < 4:
            print("** attribute name and attribute value are required **")
            return
        attr_name, val_str = args[2], args[3]
        obj = all_instances[k]

        if attr_name == "id":
            print("** cannot update id **")
            return

        elif attr_name == "created_at":
            print("** cannot update created_at **")
            return

        elif attr_name == "updated_at":
            print("** cannot update updated_at **")
            return

        if not hasattr(obj, attr_name):
            print("** attribute name missing **")
            return

        if len(args) > 4:
            print("** only one attribute can be updated at a time **")
            return
        try:
            attr_type = type(getattr(obj, attr_name))
            val = attr_type(val_str.strip('"'))
        except (ValueError, TypeError):
            print("** invalid value for the attribute type **")
            return

        setattr(obj, attr_name, val)
        models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

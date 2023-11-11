#!/usr/bin/python3
"""Console Intepreter for AirBnB_clone"""
import cmd
import models


class HBNBCommand(cmd.Cmd):
    """AirBnB Command Intepreter"""
    intro = "Welcome to AirBnB Console. (type help <topic>) for more info "
    prompt = "(hbnb) "

    def do_emptyline(self):
        print('emptyline()')
        return cmd.Cmd.emptyline(self)

    def do_create(self, args):
        if not args:
            print("** class name missing **")
            return

        cl_name = args

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
        if not args or len(args) < 2:
            print("** class name or instance id missing **")
            return

        cl_name, instance_id = args[0], args[1]
        k = "{}.{}".format(cl_name, instance_id)

        if k not in models.storage.all():
            print("** no instance found **")
            return
        print(models.storage.all()[k])

    def do_destroy(self, args):
        """
            Deletes an instance based on the class name and id
            (saves the change into the JSON file).
            Usage: destroy <class name> <id>
        """

        args = args.split()
        if not args or len(args) < 2:
            print("** class name or instance id missing **")
            return

        cl_name, instance_id = args[0], args[1]
        k = "{}.{}".format(cl_name, instance_id)

        if k not in models.storage.all():
            print("** no instance found **")
            return

        del models.storage.all()[k]
        models.storage.save()

    def do_all(self, args):
        """
        Prints all string representations of all instances based
        or not on the class name.
        Usage: all [<class name>]
        """
        args = args.split()
        if args and args[0] in models.storage.classes.keys():
            cl_name = args[0]
            objs = models.storage.all().values()
            instances = [str(obj) for obj in objs]
        elif not args:
            cl_name = args[0]
            objs = models.storage.all().values()
            instances = [str(obj) for obj in objs]
        else:
            print("** class doesn't exist **")
            return

        print(instances)

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute
        (saves the change into the JSON file).
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = args.split()
        if not args or len(args) < 4:
            print("** class name, instance id, attribute name,**")
            return

        cl_name, instance_id, attr_name, val_str = args
        k = "{}.{}".format(cl_name, instance_id)

        if k not in models.storage.all():
            print("** no instance found **")
            return

        obj = models.storage.all()[k]
        setattr(obj, attr_name, val_str)
        models.storage.save()

    def do_quit(self, args):
        """exits the console. Usage: (Ctrl + D) or (type <quit>)"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

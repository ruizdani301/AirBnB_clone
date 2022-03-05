#!/usr/bin/python3
""" This is a module with the commands to use
    is possible add new commands
"""

import cmd
from models.base_model import BaseModel
from models import storage as fs


class HBNBCommand(cmd.Cmd):
    """command interpreter"""

    prompt = "(hbnb) "
    pass

    def emptyline(self):
        """pass an empty line and avoid to create
           a new line"""
        pass

    def do_quit(self, args):
        """Quit command to exit the program"""
        return(True)

    def do_EOF(self, args):
        """exit with crtl + d"""
        return(True)

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it
           (to the JSON file) and prints the id
        """
        if len(args) == 0:
            print("** class name missing **")

        elif args in fs.clases:
            args = fs.clases[args]()
            print(args.id)

        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an instance
           based on the class name and id
        """
        clase = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(clase) == 1:
            print("** instance id missing **")

        elif clase[0] in fs.clases:
            key = args.replace(" ", ".")
            if key in fs.all():
                storage = fs.all()
                print(storage[key])
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name"""

        clase = args.split()

        if len(args) == 0:
            print("** class name missing **")

        elif clase[0] in fs.clases:
            if len(clase) == 1:
                print("** instance id missing **")
            else:
                try:
                    key = args.replace(" ", ".")
                    del fs.dic_j()[key]
                    del fs.all()[key]
                    fs.update_json()

                except Exception:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        """Prints all string representation of all instances
           based or not on the class name
        """

        all_objs = fs.all()
        for obj_key in all_objs.keys():
            obj = all_objs[obj_key]
            print(obj)

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or
           updating attribute (save the change into the JSON file)
        """

        if len(args) == 0:
            print("** class name missing **")
        else:
            arg_split = args.split()

            if arg_split[0] in fs.clases:
                if len(arg_split) == 1:
                    print("** instance id missing **")
                else:
                    key = "{}.{}".format(arg_split[0], arg_split[1])

                    if key in fs.all():
                        if len(arg_split) == 2:
                            print("** attribute name missing **")
                        else:
                            if len(arg_split) == 3:
                                print("** value missing **")
                            else:
                                li_insta = fs.all()
                                insta = li_insta[key]
                                try:
                                    if atri.isnumeric():
                                        atri = int(arg_split[3])
                                    else:
                                        atri = float(arg_split[3])
                                except ValueError:
                                    atri = arg_split[3]
                                setattr(insta, arg_split[2], atri)

                                li_dir = fs.dic_j()
                                li_dir[key] = insta.to_dict()
                                fs.update_json()

                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")


if __name__ == '__main__':
    interprete = HBNBCommand()
    interprete.cmdloop()

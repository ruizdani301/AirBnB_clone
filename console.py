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
    list_command = ["all()", "show()", "count()", "destroy()", "update()"]

    def emptyline(self):
        """pass an empty line and avoid to create
           a new line"""
        pass

    def default(self, args):
        """operation or commands for default"""
        clase = ""
        key = ""
        parameters = ""
        separate = args.split(".")
        if separate[0] in fs.clases:
            clase = separate[0]
            name_command = separate[1]
            pos1 = name_command.find("(") + 1
            pos2 = name_command.rfind(")")
            for x in range(pos1, pos2):
                parameters = parameters + name_command[x]
            name_command = name_command.replace(parameters, "")
            key = parameters.replace('"', '')
            if name_command in self.list_command:
                key = "{} {}".format(clase, key)
                if(name_command == self.list_command[0]):
                    self.do_all(clase)
                elif(name_command == self.list_command[1]):
                    self.do_show(key)
                elif(name_command == self.list_command[2]):
                    self.do_count(clase)
                elif(name_command == self.list_command[3]):
                    self.do_destroy(key)
                elif(name_command == self.list_command[4]):
                    separate2 = parameters.split(",")
                    k = separate2[0].replace('"', '')
                    name_atr = separate2[1].replace('"', '')
                    value_atr = separate2[2].replace('"', '')
                    key = "{} {}".format(clase, k)
                    key = "{} {} {}".format(key, name_atr, value_atr)
                    print(key)
                    self.do_update(key)

        else:
            print("*** Unknown syntax: ", args)

    def do_quit(self, args):
        """Quit command to exit the program"""
        return(True)

    def do_EOF(self, args):
        """exit with crtl + d"""
        return(True)

    def do_count(self, args):
        """shows the number of instances"""
        all_objs = fs.all()
        cant = 0
        if args in fs.clases:
            #recorre el obj de file storage
            for obj_key in all_objs.keys():
                #Encuentra la instancia
                instancia = (all_objs[obj_key])
                #regresa el diccionario de la instancia
                dic_instancia = instancia.to_dict()
                #compara la llave class con args
                if (dic_instancia)["__class__"] == args:
                    cant += 1
            print(cant)
        else:
            print("** class doesn't exist **")

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

        elif clase[0] in fs.clases:
            if len(clase) == 1:
                print("** instance id missing **")
            else:
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
                    key = "{}.{}".format(clase[0], clase[1])
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
        if len(args) == 0:

            for obj_key in all_objs.keys():
                obj = all_objs[obj_key]
                print(obj)
        else:
            if args in fs.clases:
                for obj_key in all_objs.keys():
                    if (all_objs[obj_key]).to_dict()["__class__"] == args:
                        obj = all_objs[obj_key]
                        print(obj)
            else:
                print("** class doesn't exist **")

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
    HBNBCommand().cmdloop()

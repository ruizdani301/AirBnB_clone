#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    """command interpreter"""

    prompt = "(hbnb) "

    def do_quit(self, args):
        #para salir
        return(True)

    def do_EOF(self, args):
        #para salir
        return(True)

    def do_create(self,args):
        pass

    def do_show(self, args):
        pass

    def do_destroy(self, args):
        pass

    def do_all(self, args):
        pass

    def do_update(self, args):
        pass

    #def do_help(self, args):
    #    print("saliste cacharro horrible")
    #    pass

if __name__ == '__main__':
    interprete = HBNBCommand()
    interprete.cmdloop(intro="Bienvenido")

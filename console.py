#!/usr/bin/python3
"""Custom command line interpreter for AirBnB clone project"""
import cmd


class myCommand(cmd.Cmd):
    """Class to define interpreter"""
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """method to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        print("\nSystem exit...")
        return True

    def empty_line(self):
        """Do nothing when empty line is entered"""
        pass


if __name__ == "__main__":
    myCommand().cmdloop()

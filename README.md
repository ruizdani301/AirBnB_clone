# AirBnB clone

## 0x00. AirBnB clone - The console

```
For Holberton School.
Cohort 16.
```
   By Guillaume
 Weight: 5
 Project to be done in teams of 2 people (your team: Daniel Rivera, Jorge Orlando Calambás Conda
 Ongoing project - started 02-28-2022, must end by 03-07-2022 (in 2 days) - you're done with 0% of tasks.
 Checker will be released at 03-05-2022 06:00 AM
 Manual QA review must be done (request it when you are done with the project)
 An auto review will be launched at the deadline
		  ```
![image](https://user-images.githubusercontent.com/81341089/156898379-8e6dfffc-b217-4b41-9c69-fefc53af47c9.png)

## Description

Airbnb is a community market that shares and exchanges goods and services between individuals through digital platforms so that a user can find accommodation in another person's home and not in a hotel, from common apartments to tree houses, igloos, geodomes, mills etc.

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

Create a new object (ex: a new User or a new Place)
Retrieve an object from a file, a database etc…
Do operations on objects (count, compute stats, etc…)
Update attributes of an object
Destroy an object
## Requirements

Create a Base class (BaseModel) containing 3 public attributes and a dictionary

Attributes:
Id: Random identifier
Created_on Date created
Updated_on Date Modified

1) Create a dictionary containing a (number(id), name, modification date and creation date) where the attribute labels will be the keys)

2) Create a method (save) that changes the modification date

3) Create a method (to dict) that retrieves the dictionary

4) Modify __str__ and modify __dict__

5) create a console with cmd python library

6) Recognize diferents commands such as help, all, create, show, update etc... 
   
      
## Installation

   - execute script ./console.py
   - Example `![image](https://user-images.githubusercontent.com/81341089/156897944-ec48c7e0-628e-402e-b89c-6b1278b8fbe2.png)" 


#### Usage

In interactive mode, simply run the program with ()./console) and wait for the prompt to appear. From there, you can type commands freely,

Example `create BaseModel` , `all`, `destroy BaseModel (id)  `etc.`


Our shell has support for the following built-in commands:

| Command             | Definition                                                                                |
| ------------------- | ----------------------------------------------------------------------------------------- |
| EOF , quit          | Exit the console.                                                                         |
| help                | print all the commands                                                                    |
| all                 | show all the instances saved in json file                                                 |
| show                | show the instances dictionary that come  like parameter,  name class and id               |
| update              | modify atributte or created atributte of any instance                                     |

## Files included


| File                   | Details                                       |
|----------------------- | ------------------------------------------    |
| [file.storage.py] | interpret a command and display it in output  |
| [__init__.py]          | containts all the prototypes                  |
| [base_model]           | compares the strings of the PATH 		 |
| [city.py]	         | functions for printing and handle strings     |
| [place.py]	         | function for free a double pointer	         |
| [review.py]	         | get the built-in function accord to a command |
| [state.py]             | compare count and concatenate the strings	 |
| [user.py]              | compare count and concatenate the strings	 |
| [amenity.py]           | compare count and concatenate the strings	 |

## Examples

'in the following example the modules were imported and it shows the commands that were used to create the instances as well as the command that validates if there is an empty line "emptyline" and output "EOF"'

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
	    ........



## Authors
```
* **Jorge Orlando Calambas Conda @jorgecal123** - [JorgeCalambas](https://github.com/JorgeCal123)
* **Daniel Ruiz @ruizdani301** - [DanielRuiz](https://github.com/ruizdani301)
```

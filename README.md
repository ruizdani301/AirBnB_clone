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

## Description

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

Create a new object (ex: a new User or a new Place)
Retrieve an object from a file, a database etc…
Do operations on objects (count, compute stats, etc…)
Update attributes of an object
Destroy an object
## Requirements



## Installation

   - Compile: `gcc -Wall -Werror -Wextra -pedantic *.c -o hsh`
   - Run the shell in interactive mode: `./hsh`
   - Run the shell in non-interactive mode:
   - Example `echo "ls -l" | ./hsh`


## Usage

After compilation, the resulting program can run in interactive or non-interactive mode.

#### Interactive Mode

In interactive mode, simply run the program with ()./console) and wait for the prompt to appear. From there, you can type commands freely,

Example `create BaseModel` , `all`, `destroy BaseModel (id)  `etc.`

#### Non-Interactive Mode

In non-interactive mode, echo your desired command and pipe it into the program like this:

```sh
echo "ls" | ./hsh
```

In non-interactive mode, the program will exit after finishing your desired command(s).

#### Included Built-Ins

Our shell has support for the following built-in commands:

| Command             | Definition                                                                                |
| ------------------- | ----------------------------------------------------------------------------------------- |
| exit                | Exit the shell, with an optional exit status, n.                                          |
| env                 | Print the environment.                                                                    |


## Files included


| File                   | Details                                       |
|----------------------- | ------------------------------------------    |
| [file.storage.py] | interpret a command and display it in output  |
| [__init__.py]        | containts all the prototypes                  |
| [base_model]        | compares the strings of the PATH 		 |
| [city.py]	 | functions for printing and handle strings     |
| [place.py]	 | function for free a double pointer	         |
| [review.py]	 | get the built-in function accord to a command |
| [state.py] | compare count and concatenate the strings	 |
| [user.py] | compare count and concatenate the strings	 |
| [amenity.py] | compare count and concatenate the strings	 |

## Examples



## Authors
```
* **Diego Jojoa @diegojojoayandun** - [Diegojojoa](https://github.com/diegojojoayandun)
* **Daniel Ruiz @ruizdani301** - [DanielRuiz](https://github.com/ruizdani301)
```

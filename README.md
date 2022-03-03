# SIMPLE SHELL

## Our Gates of sHELL. 0x16. C - simple_shell

```
For Holberton School.
Cohort 16.
```
   By Julien Barbier, co-founder & CEO
   Project to be done in teams of 2 people (our team: Daniel Rivera, Diego jojoa.
   Ongoing project - started 11-25-2021, must end by 12-09-2021 (in 14 days) - you're done with 0% of tasks.
   Checker will be released at 12-07-2021 09:07 PM.
   Manual QA review must be done (request it when you are done with the project)
   QA review fully automated.
		  ```

## Description

The simple shell is an simple application that reads lines from the terminal, interprets them, and executes them. This shell includes simple basic functionality of a traditional Unix-like command line user interface. Standard functions and system calls employed in simple_shell include: `stat, execve, exit, fork, free, getline, malloc, perror, wait, write.`

## Requirements

simple_shell is designed to run in the `Ubuntu 20.04.5 LTS` linux environment and to be compiled using the GNU compiler with flags`-Wall, -Werror, -Wextra, and -pedantic.`

## Installation

   - Compile: `gcc -Wall -Werror -Wextra -pedantic *.c -o hsh`
   - Run the shell in interactive mode: `./hsh`
   - Run the shell in non-interactive mode:
   - Example `echo "ls -l" | ./hsh`


## Usage

After compilation, the resulting program can run in interactive or non-interactive mode.

#### Interactive Mode

In interactive mode, simply run the program and wait for the prompt to appear. From there, you can type commands freely,

Example `pwd` , `ls -l`, `echo "Hola mundo!"`, `etc.`

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
| [simple_shell.c](./hsh)| interpret a command and display it in output  |
| [main.h](./hsh)        | containts all the prototypes                  |
| [path.c](./hsh)        | compares the strings of the PATH 		 |
| [codes.c](./hsh)	 | functions for printing and handle strings     |
| [free.c](./hsh)	 | function for free a double pointer	         |
| [built-ins.c](./hsh)	 | get the built-in function accord to a command |
| [_string.c](./hsh)	 | compare count and concatenate the strings	 |

## Examples

```sh
$ ls -l
total 8
drwxrwxr-x 1 vagrant vagrant Dec 2 13:23 hsh
drwxrwxr-x 2 vagrant vagrant Dec 2 20:30 README.md
```

```sh
$ /bin/pwd
/home/vagrant/shell
```

```sh
$ hello world
./hsh: 1: hello: not found
```

## Authors
```
* **Diego Jojoa @diegojojoayandun** - [Diegojojoa](https://github.com/diegojojoayandun)
* **Daniel Ruiz @ruizdani301** - [DanielRuiz](https://github.com/ruizdani301)
```

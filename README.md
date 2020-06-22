# General information

This application reads one plain text file, sorts one line and display it on terminal.

Project developed with Python 3 and Unit Tests.

# Use

1 - Is necessary put the file that will be read on the project **root** folder, before `src/`. If the file is not placed, the program will read `v.txt` file that is in the root of the project.


2 - Run the main file:

```bash
$ python3 run.py
```
3 - Type the name of the file that you wants to read.

4 - After reading the file, will be display the selected line on terminal.

# Tests

Command to run the tests:

```bash
$ python3 -m unittest discover -s tests/
```

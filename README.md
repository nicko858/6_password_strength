# Password Strength Calculator

# Quickstart

The program is represented by the module ```password_strength.py```.
Module ```password_strength.py``` contains the following functions:

- ```check_exist_same_chars()```
- ```check_file()```
- ```get_args()```
- ```get_password_strength()```
- ```get_user_password()```
- ```has_alphabetical()```
- ```has_digit()```
- ```has_digit_and_has_alphabetical()```
- ```has_digit_and_upper_lower_exist()```
- ```has_special_chars()```
- ```has_special_chars_and_has_upper_lower()```
- ```has_upper_and_lower_case()```
- ```is_all_alphabetical()```
- ```is_all_digits()```
- ```is_date()```
- ```is_email()```
- ```is_in_black_list()```
- ```is_phone_number()```
- ```read_black_list()```
- ```perform_checks()```


The program uses these libraries from Python Standart Library:

```python
re
argparse
isfile from os.path 
getpass
string
```

How in works:
- The program reads the first command-line argument(path to black-list file)
- check existing black-list file
- calculates password strength
- prints result in the output

Example of script launch on Linux, Python 3.5:

```bash

$ python password_strength.py  <path black-list file>

```
In the console  output you will see something  like this:
```bash
Enter your password to define the password`s strength:<user input>
Your password strength equals 1.
```

Optionally, the program using black-list.
You can make your own black-list, using different sources. For example:
https://github.com/danielmiessler/SecLists

The program check command-line arguments and if it is wrong,  you will see the warning message 
```error: unrecognized arguments``` and usage-message.

If the the black-list file doesn't present in the file-system, you will see the warning message:<br/>
```Can't find a black-list file!```<br/>
```Continue without black-list considering..."```

The program will not run if the input-value is not a file.
You will see the warning message:<br/>```The <black-list> is not a file!```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)





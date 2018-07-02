# Password Strength Calculator

# Quickstart

The program is represented by the module ```password_strength.py```.
Module ```password_strength.py``` contains the following functions:

- ```get_args()``` - parses script command-line arguments
- ```file_check()``` - check exisisting black-list file
- ```get_user_password()``` - accepts dictionary and returns dict having paths-count > 1
- ```exist_same_chars()``` - prints info about finding files
- ```get_password_length()``` - returns password length
- ```digits_exist()``` - check if digits exists
- ```exist_upper_and_lower_case()``` - check if exist both upper and lower case chars
- ```exist_special_chars()``` - check existing special chars 
- ```get_black_list()``` - read black-list file content(You can make your own black-list, using different sources. For example:
https://github.com/gchan/password_blacklist/blob/master/data/Top95Thousand-probable.txt)


- ```is_date()``` - check if input is date
- ```is_email()``` - check if input is email
- ```is_phone_number()``` - check if input is phone number 
- ```check_passwd_length()``` - check password length
- ```black_list_exist()``` - check existing black-list file 
- ```get_password_strength()``` - calculates password strength      


The program uses these libs from Python Standart Library:

```python
re,
argparse
exists, isfile from os.path 
```

How in works:
- The program reads  the first command-line argument(path to black-list file)
- check existing black-list file
- calculates password strength
- prints result in the output

Example of script launch on Linux, Python 3.5:

```bash

$ python password_strength.py  <path black-list file>

```
in the console  output you will see something  like this:
```bash
Enter your password to define the password`s strength:
<user input>
Your password strength equals 1.
```

In the cases below, the program will not run:

The program check command-line arguments and if it is wrong,  you will see the warning message ```error: unrecognized arguments``` and usage-message.

If the the black-list file doesn't present in the file-system, you will see the warning message:
```No such file or directory <black-list> !```
If the input-value is not a file,  you will see the warning message:
```The <black-list> is not a file!```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

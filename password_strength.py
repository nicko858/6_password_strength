import re
import argparse
from os.path import exists, isfile


def file_check(file_name):
    if not exists(file_name):
        msg_exist = "No such file or directory - '{}' !".format(file_name)
        raise argparse.ArgumentTypeError(msg_exist)
    elif not isfile(file_name):
        msg_isdir = "'{}' is not a file".format(file_name)
        raise argparse.ArgumentTypeError(msg_isdir)
    else:
        return file_name


def get_args():
    script_usage = 'python password_strength.py  <path to black_list file>'
    parser = argparse.ArgumentParser(
        description='How to run dublicates.py:',
        usage=script_usage
    )
    parser.add_argument(
        'black_list_file',
        type=file_check,
        help='Specify the path to black_list file'
    )
    args = parser.parse_args()
    return args


def get_user_password():
    print("Enter your password to define the password`s strength:")
    password = input()
    return password


def exist_same_chars(password):
    return password.lower().count(password[0]) == len(password)


def get_password_length(password):
    return len(password)


def digits_exist(password):
    digit_count = sum(c.isdigit() for c in password)
    return digit_count


def exist_upper_and_lower_case(password):
    letters = set(password)
    is_mixed_case = any(letter.islower() for letter in letters) and \
                    any(letter.isupper() for letter in letters)
    return is_mixed_case


def exist_special_chars(password):
    special_chars = set(" !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~")
    if special_chars.intersection(password):
        return True
    else:
        return False


def get_black_list(black_list_file):
    with open(black_list_file, "r") as source_file:
        return source_file.read()


def is_date(password):
    date_present = bool(re.match(
        "(\d{2})[/.-](\d{2})[/.-](\d{4})$",
        password
    ))
    return date_present


def is_email(password):
    is_email = bool(re.match(
        r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", password
    ))
    return is_email


def is_phone_number(password):
    phone_pattern = re.compile(r'^(\d{3})\D+(\d{3})\D+(\d{2})\D+(\d{2})$')
    return bool(phone_pattern.search(password))


def check_passwd_length(password):
    if 8 < password < 12:
        return "9"
    elif password > 12:
        return "10"
    else:
        return "3"



def black_list_exist(password, black_list_file):
    return password in black_list_file


def get_password_strength(password, black_list_file):
    if black_list_exist(password, black_list_file):
        return "1"
    if exist_same_chars(password):
        return "2"
    if digits_exist(password):
        if is_phone_number(password):
            return "5"
        if is_date(password):
            return "4"
        digits_count = digits_exist(password)
        if digits_count > 1:
            return "6"
        else:
            return "3"
    if exist_special_chars(password):
        if is_email(password):
            return "2"
        return "8"
    if exist_upper_and_lower_case(password):
        return "7"
    passwd_length = get_password_length(password)
    return check_passwd_length(passwd_length)


if __name__ == "__main__":
    args = get_args()
    black_list_file = get_black_list(args.black_list_file)
    password = get_user_password()
    password_strength = get_password_strength(password, black_list_file)
    print("Your password strength equals {}.".format(password_strength))

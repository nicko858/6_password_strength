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
    script_usage = 'python password_strength.py <path to black_list file>'
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


def chars_exist(password, mode, passwd_score):
    if mode == 'any':
        for char in list(password):
            if char.isalpha():
                return True
    elif mode == 'all':
        if password.isalpha():
            passwd_score -= 2
        return passwd_score


def check_exist_same_chars(password, passwd_score):
    if password.lower().count(password[0]) == len(password):
        passwd_score -= 2
    return passwd_score


def get_password_length(password):
    return len(password)


def digits_exist(password, mode, passwd_score):
    if mode == 'any':
        digit_count = sum(c.isdigit() for c in password)
        if digit_count >= 1:
            return True
        else:
            return False
    elif mode == 'all':
        if password.isdigit():
            passwd_score -= 2
        return passwd_score


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


def is_date(password, passwd_score):
    date_present = bool(re.match(
        "(\d{2})[/.-](\d{2})[/.-](\d{4})$",
        password
    ))
    if date_present:
        passwd_score -= 1
    return passwd_score


def is_email(password):
    is_email = bool(re.match(
        r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", password
    ))
    return is_email


def is_phone_number(password, passwd_score):
    phone_pattern = re.compile(r'^(\d{3})\D+(\d{3})\D+(\d{2})\D+(\d{2})$')
    if bool(phone_pattern.search(password)):
        passwd_score -= 1
    return passwd_score


def check_digits_and_chars_exist(password, passwd_score):
    if digits_exist(password, 'any', passwd_score)\
            and chars_exist(password, 'any', passwd_score):
        passwd_score += 2
    return passwd_score


def check_digits_and_upper_lower_exist(password, passwd_score):
    if digits_exist(password, 'any', passwd_score) \
            and exist_upper_and_lower_case(password):
        passwd_score += 3
    return passwd_score


def check_special_chars_and_upper_lower_exist(password, passwd_score):
    if exist_special_chars(password) \
            and exist_upper_and_lower_case(password):
        passwd_score += 4
    return passwd_score


def check_black_list_exist(password, black_list_file, passwd_score):
    if password in black_list_file:
        passwd_score -= 3
    return passwd_score


def get_password_strength(password, black_list_file):
    min_password_length = 6
    passwd_length = get_password_length(password)
    if passwd_length >= min_password_length:
        passwd_score = 5
        result_1 = check_black_list_exist(
            password,
            black_list_file,
            passwd_score)
        result_2 = check_exist_same_chars(password, result_1)
        result_3 = chars_exist(password, 'all', result_2)
        result_4 = check_digits_and_chars_exist(password, result_3)
        result_5 = check_digits_and_upper_lower_exist(password, result_4)
        result_6 = is_phone_number(password, result_5)
        result_7 = is_date(password, result_6)
        result_8 = digits_exist(password, 'all', result_7)
        result_9 = check_special_chars_and_upper_lower_exist(
            password,
            result_8)
        passwd_score = result_9
    else:
        passwd_score = 1
    if passwd_score > 10:
        passwd_score = 10
    elif passwd_score <= 0:
        passwd_score = 1
    return passwd_score


if __name__ == "__main__":
    args = get_args()
    black_list_file = get_black_list(args.black_list_file)
    password = get_user_password()
    password_strength = get_password_strength(password, black_list_file)
    print("Your password strength equals {}.".format(password_strength))
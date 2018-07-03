import re
import argparse
from os.path import isfile
import getpass
import string


def check_file(file_name):
    if not isfile(file_name):
        msg_isdir = "'{}' is not a file".format(file_name)
        raise argparse.ArgumentTypeError(msg_isdir)
    else:
        return file_name


def get_args():
    script_usage = "python password_strength.py <path to black_list file>"
    parser = argparse.ArgumentParser(
        description="How to run dublicates.py:",
        usage=script_usage
    )
    parser.add_argument(
        "black_list",
        nargs='?',
        type=check_file,
        help="Specify the path to black_list file"
    )
    args = parser.parse_args()
    return args


def get_user_password():
    password = getpass.getpass(
        prompt="Enter your password to define the password`s strength:")
    return password


def has_alphabetical(password):
    for char in password:
        if char.isalpha():
            return True


def is_all_alphabetical(password):
    return bool(password.isalpha())


def has_digit(password):
    digit_count = sum(c.isdigit() for c in password)
    return bool(digit_count >= 1)

def is_all_digits(password):
    return bool(password.isdigit())


def check_exist_same_chars(password):
    return bool(len(password) > len(set(password)))


def has_upper_and_lower_case(password):
    letters = set(password)
    is_mixed_case = (any(letter.islower() for letter in letters)
                     and any(letter.isupper() for letter in letters))
    return is_mixed_case


def has_special_chars(password):
    special_chars = set(string.punctuation)
    return bool(special_chars.intersection(password))


def read_black_list(black_list):
    with open(black_list, "r") as source_file:
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
    phone_pattern = re.compile(r"^(\d{3})\D+(\d{3})\D+(\d{2})\D+(\d{2})$")
    return bool(phone_pattern.search(password))


def has_digit_and_has_alphabetical(password):
    return bool(has_digit(password) and has_alphabetical(password))


def has_digit_and_upper_lower_exist(password):
    return bool(has_digit(password)
                and has_upper_and_lower_case(password))


def has_special_chars_and_has_upper_lower(password):
    return bool(
        has_special_chars(password)
        and has_upper_and_lower_case(password))


def is_in_black_list(password, black_list):
    return bool(password in black_list)


def get_password_strength(password, black_list):
    min_password_length = 6
    passwd_length = len(password)
    if passwd_length >= min_password_length:
        passwd_score = 5
        reference_scores = {
            check_exist_same_chars: -2,
            is_all_alphabetical: -2,
            has_digit_and_has_alphabetical: 2,
            has_digit_and_upper_lower_exist: 3,
            is_phone_number: -1,
            is_date: -1,
            is_all_digits: -2,
            has_special_chars_and_has_upper_lower: 4,
            is_in_black_list: -3
        }
        if not black_list:
            del reference_scores[is_in_black_list]
        result_of_check = {}
        for func in reference_scores.keys():
            if func == is_in_black_list:
                result_of_check[func] = func(password, black_list)
            else:
                result_of_check[func] = func(password)
        for (check_name, result) in result_of_check.items():
            if result:
                passwd_score += reference_scores.get(check_name)
    else:
        passwd_score = 1
    passwd_score = max(1, min(passwd_score, 10))
    return passwd_score


if __name__ == "__main__":
    args = get_args()
    try:
        black_list = read_black_list(args.black_list)
    except (FileNotFoundError, TypeError):
        black_list = ''
        print("Can't find a black-list file!\n"
              "Continue without black-list considering...")
    password = get_user_password()
    password_strength = get_password_strength(password, black_list)
    print("Your password strength equals {}.".format(password_strength))
#!/usr/bin/env python3
def validate_password(password):
    if len(password) < 8:
        return False
    elif ' ' in password:
        return False
    else:
        has_upper = False
        has_lower = False
        has_digit = False
        for char in password:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_digit = True
        if has_upper and has_lower and has_digit:
            return True
        else:
            return False

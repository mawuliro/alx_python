#!/usr/bin/python3
def no_c(my_string):
    word_list = []
    if my_string == "":
        return ""
    else:
        for word in my_string:
            if word == "c" or word == "C":
                continue
            word_list.append(word)
            new_string = "".join(word_list)
        return new_string

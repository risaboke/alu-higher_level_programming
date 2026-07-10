#!/usr/bin/python3


def search_replace(my_list, search, replace):
    def replace_search(x):
        if x == search:
            return replace
        else:
            return x
    new_list = list(map(replace_search, my_list))
    return new_list

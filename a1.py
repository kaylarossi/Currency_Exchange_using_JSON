"""
Module for currency exchange

This module provides several string parsing functions to implement a
simple currency exchange routine using an online currency service.
The primary function in this module is exchange.


"""
def before_space(s):
    """
    Returns a copy of s up to, but not including, the first space

    Parameter s: the string to slice
    Precondition: s is a string with at least one space"""
    space_loc=s.find(' ')
    first_part=s[:space_loc]
    return first_part

def after_space(s):
    """
    Returns a copy of s after the first space

    Parameter s: the string to slice
    Precondition: s is a string with at least one space
    """
    space_loc=s.find(' ')
    last_part=s[space_loc+1:]
    return last_part

def first_inside_quotes(s):
    """
    Returns the first substring of s between two (double) quotes

    A quote character is one that is inside a string, not one that
    delimits it.  We typically use single quotes (') to delimit a
    string if want to use a double quote character (") inside of it.

    Examples:
    first_inside_quotes('A "B C" D') returns 'B C'
    first_inside_quotes('A "B C" D "E F" G') returns 'B C',
    because it only picks the first such substring

    Parameter s: a string to search
    Precondition: s is a string containing at least two double quotes
    """
    quote_first=s.find('"')
    quote_next=s[quote_first+1:].find('"')
    adjusted_end_index=quote_next+(quote_first+1)
    return s[quote_first+1:adjusted_end_index]

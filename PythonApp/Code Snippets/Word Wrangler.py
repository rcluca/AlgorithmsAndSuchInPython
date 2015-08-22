"""
Student code for Word Wrangler game
"""

import urllib2
import math
#import codeskulptor
#import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"

# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    new_list = []

    for idx in range(len(list1)):
        if idx > 0:
            if list1[idx] != list1[idx - 1]:
                new_list.append(list1[idx])
        else:
            new_list.append(list1[idx])

    return new_list

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    output_list = []

    if len(list1) <= len(list2):
        short_list = list1
        long_list = list2
    else:
        short_list = list2
        long_list = list1

    for each in range(len(short_list)):
        long_list_min = 0
        long_list_max = len(long_list)
        while long_list_min < long_list_max:
            long_list_mid = int(math.floor((long_list_max + long_list_min) / 2.0))
            if short_list[each] == long_list[long_list_mid]:
                output_list.append(long_list[long_list_mid])
                break
            elif short_list[each] > long_list[long_list_mid]:
                if long_list_min == long_list_mid:
                    long_list_min += 1
                else:
                    long_list_min = long_list_mid
            elif short_list[each] < long_list[long_list_mid]:
                if long_list_max == long_list_mid:
                    long_list_max -= 1
                else:
                    long_list_max = long_list_mid

    return output_list

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in both list1 and list2.

    This function can be iterative.
    """
    sorted_list = []

    list1_idx = 0
    list2_idx = 0

    while list1_idx < len(list1) or list2_idx < len(list2):
        if list1_idx < len(list1) and list2_idx < len(list2):
            if list1[list1_idx] <= list2[list2_idx]:
                sorted_list.append(list1[list1_idx])
                list1_idx += 1
            else:
                sorted_list.append(list2[list2_idx])
                list2_idx += 1
        elif list1_idx >= len(list1):
            sorted_list.append(list2[list2_idx])
            list2_idx += 1
        elif list2_idx >= len(list2):
            sorted_list.append(list1[list1_idx])
            list1_idx += 1

    return sorted_list

def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    if len(list1) <= 1:
        return list1
    else:
        list1_sorted = merge_sort(list1[(len(list1) / 2):])
        list2_sorted = merge_sort(list1[:(len(list1) / 2)])
        return merge(list1_sorted, list2_sorted)

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    rest_strings = []

    if len(word) == 0:
        return [""]
    elif len(word) == 1:
        return word[0]
    else:
        first = word[0]
        rest = word[1:]
        return gen_all_strings(rest)

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    return []

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
# run()
list1 = [4,3,2,6,6,654,65,6,32,34,23654,35,2,2342,4,7,56,4,523,42,36,54,645,756,756,23,23,3,4,65,6,65,4,]
list2 = []
print merge_sort(list1)
#list2 = sorted([12, 13, 14])
# print intersect(list1, list2)
# print merge(list1, list2)
#print gen_all_strings("raul")
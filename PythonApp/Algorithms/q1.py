# Time Spent on Question:
# 1:40

# Time Spent on Initial Solution:
# 1:10

import urllib2
import json

def print_github_graph(search_term):
    results = urllib2.urlopen(r"https://api.github.com/search/users?q=" + search_term).read()

    # deserialize string to object
    obj = json.loads(results)
    items = obj["items"]
    
    # sort list of items
    sortedItems = sorted(items,key=lambda k: k["login"])

    # build array with letters and frequencies
    freq = [[chr(x + 97) + ":"] for x in range(26)]
    freq.append(["other:"])
    for user in sortedItems[:5]:
        for char in user["login"]:
            char = char.lower()
            if _is_other(char):
                freq[26].append("*")
            else:
                freq[_char_to_arr_index(char)].append("*")

    strList = []
    for each in freq:
        strList.append("".join(each))
    
    # return a single string joined by new lines
    return "\n".join(strList)

    ############################################################################

    ## Below is part of the code from my first attempt
    # Issues that arose from this approach:
    # - "other" is sorted to middle of list
    # - missing letters where no frequency

    ## count up letter frequencies in a dictionary (used for quick lookup)
    #dict = {}
    #for user in sortedItems[:5]:
    #    for char in user["login"]:
    #        char = char.lower()
    #        if dict.has_key(char):
    #            dict[char].append("*")
    #        else:
    #            if is_other(char):
    #                if dict.has_key("other"):
    #                    dict["other"].append("*")
    #                else:
    #                    dict["other"] = ["*"]
    #            else:
    #                dict[char] = ["*"]
    
    ## convert dictionary of frequencies into list of strings
    #strList = []
    #for key, value in dict.iteritems():
    #    strList.append(key + ":" + "".join(value))
    ############################################################################

def _is_other(char):
    cVal = ord(char)
    if cVal < 97 or cVal > 122:
        return True
    return False

def _char_to_arr_index(char):
    return ord(char) - 97
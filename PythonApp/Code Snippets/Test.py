# # Valid braces
# mystring = [")(){}","[]({})","([])","{()[]}","([)]"]
#
# def check_order(strings):
#     string_dict = {")":"(", "]":"[", "}":"{"}
#
#     for string in strings:
#         inner_brace_stack = []
#
#         for brace in string:
#             if brace in string_dict.values():
#                 inner_brace_stack.append(brace)
#             elif brace in string_dict.keys():
#                 if len(inner_brace_stack) > 0:
#                     if inner_brace_stack[len(inner_brace_stack) - 1] == string_dict[brace]:
#                         inner_brace_stack.pop()
#                     elif inner_brace_stack[len(inner_brace_stack) - 1] <> string_dict[brace]:
#                         print 0
#                         break
#                 else:
#                     print 0
#                     break
#
#             if brace == string[len(string) - 1]:
#                 print 1
#
# check_order(mystring)
####################################################
# # Factorial with recursion
# def fact(inp):
#     if inp == 1:
#         return 1
#     else:
#         return inp * fact(inp - 1)
# print fact(4)
####################################################
# # Binary Search
# import math
#
# mylist = [1,2,3,4,5,6,7,8,9,10]
#
# def binary_search(item, list, max = -1, min = 0):
#     if max == -1: max = len(list) - 1
#     if max == min:
#         return "Item not found."
#     else:
#         idx = min + int(math.floor(float(max - min) / 2))
#         if item == list[idx]:
#             return idx
#         elif item < list[idx]:
#             max = int(idx) - 1
#             return binary_search(item, list, max, min)
#         elif item > list[idx]:
#             min = int(idx) + 1
#             return binary_search(item, list, max, min)
#
# print binary_search(2,mylist)
####################################################
# # B Tree
# f = open("Cases File.csv", "r")
#
# for line in f:
#     print line
#
# from os import getenv
# import pymssql
####################################################
# # Quicksort
# import math
#
# def quicksort(aList, start, end):
#     if start < end:
#         p = partition(aList, start, end)
#         quicksort(aList,start, p - 1)
#         quicksort(aList,p + 1,end)
#     return aList
#
# def partition(aList, start, end):
#     p = int(math.floor(start + (end - start) / 2))
#     aList[p], aList[end] = aList[end], aList[p]
#     p = end
#     end -= 1
#     while start < p:
#         if aList[start] > aList[p]:
#             aList[start], aList[end], aList[p] = aList[end], aList[p], aList[start]
#             end -= 1
#             p -= 1
#         else:
#             start += 1
#     return p
#
# myList = [5,1,4,2,3,7,8,6,0,10,4,6,87,3,4,565,3,4,10,3,2,2,2,3]
# #myList = ["a", "b", "a", "i", "z", "n", "c"]
# print quicksort(myList, 0, len(myList) - 1)
####################################################
# # Insertion Sort
# def insertion_sort(aList):
#     for idx in range(len(aList)):
#         moving_idx = idx
#         while moving_idx > 0 and aList[moving_idx] < aList[moving_idx - 1]:
#             aList[moving_idx - 1], aList[moving_idx] = aList[moving_idx], aList[moving_idx - 1]
#             moving_idx -= 1
#     return aList
#
# myList = [5,1,4,2,3,7,8,6,0,10,4,6,87,3,4,565,3,4,10,3,2,2,2,3]
# print insertion_sort(myList)
####################################################
# # Selection Sort
# def selection_sort(aList):
#     for idx in range(len(aList) - 1):
#         min_idx = idx + min(aList[idx:])
#         aList[idx], aList[min_idx] = aList[min_idx], aList[idx]
#     return aList
#
# def min(aList):
#     min_num = aList[0]
#     min_idx = 0
#     for idx, val in enumerate(aList):
#         if val < min_num:
#             min_idx = idx
#             min_num = val
#     return min_idx
#
# myList = [5,1,4,2,3,7,8,6,0,10,4,6,87,3,4,565,3,4,10,3,2,2,2,3]
# print selection_sort(myList)
####################################################
# # Bubble Sort
#
# def bubble_sort(aList):
#     count = 1
#     while count > 0:
#         count = 0
#         for idx in range(len(aList) - 1):
#             if aList[idx + 1] < aList[idx]:
#                 aList[idx + 1], aList[idx] = aList[idx], aList[idx + 1]
#                 count += 1
#     return aList
#
# myList = [5,1,4,2,3,7,8,6,0,10,4,6,87,3,4,565,3,4,10,3,2,2,2,3]
# print bubble_sort(myList)
####################################################
# # Merge Sort
#
# import math
#
# def merge_sort(aList):
#     if len(aList) <= 1:
#         return aList
#     else:
#         mid = int(math.floor(float(len(aList) / 2)))
#         left_list = merge_sort(aList[:mid])
#         right_list = merge_sort(aList[mid:])
#         return merge(left_list, right_list)
#
# def merge(list1, list2):
#     merged_list = []
#     list1_idx = 0
#     list2_idx = 0
#
#     while list1_idx < len(list1) or list2_idx < len(list2):
#         if list1_idx < len(list1) and list2_idx < len(list2):
#             if list1[list1_idx] <= list2[list2_idx]:
#                 merged_list.append(list1[list1_idx])
#                 list1_idx += 1
#             else:
#                 merged_list.append(list2[list2_idx])
#                 list2_idx += 1
#         elif list1_idx < len(list1):
#             merged_list.append(list1[list1_idx])
#             list1_idx += 1
#         elif list2_idx < len(list2):
#             merged_list.append(list2[list2_idx])
#             list2_idx += 1
#
#     return merged_list
#
# myList = [5,1,4,2,3,7,8,6,0,10,4,6,87,3,4,565,3,4,10,3,2,2,2,3]
# print merge_sort(myList)
####################################################
# # IO Operations
# fList = []
#
# f = open(r"C:\Users\raul.luca\Google Drive\_DOMO\Domo_POS.csv")
# for lines in f.readlines()[1:-1]:
#     split_lines = lines.split(",")
#     temp_list = []
#     for item in split_lines:
#         clean_item = item.strip()
#         temp_list.append(clean_item)
#     fList.append(temp_list)
# f.close()
#
# numberOfPayments = 0
# paymentAmount = 0.0
#
# for each in fList:
#     numberOfPayments += int(each[2])
#     paymentAmount += float(each[3])
#     print each
#
# print "Number of Payments:", numberOfPayments, ", Payment Amount:", paymentAmount

# mySum = 0
#
# for line in f.readlines()[1:-1]:
#     line_items = line.split(",")
#     # mySum += int(line_items[2])
#     for item in line_items:
#         print item
# print mySum
####################################################
# # Singly Linked List
# class Node:
#
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#     def get_data(self):
#         return self.data
#
#     def get_next(self):
#         return self.next
#
#     def set_data(self, new_data):
#         self.data = new_data
#
#     def set_next(self, new_next):
#         self.next = new_next
#
# class LinkedList:
#
#     def __init__(self):
#         self.head = None
#         self.count = 0
#
#     def is_empty(self):
#         return self.head == None
#
#     def get_size(self):
#         return self.count
#
#     def add(self, data):
#         new = Node(data)
#         new.set_next(self.head)
#         self.head = new
#         self.count += 1
#
#     def remove(self, data):
#         current = self.head
#         previous = None
#         if current != None:
#             while True:
#                 if current.data == data:
#                     if previous == None:
#                         self.head = current.next
#                     else:
#                         previous.next = current.next
#                     self.count -= 1
#                     return current
#                 if current.next != None:
#                     previous = current
#                     current = current.next
#                 else:
#                     return "Not found."
#         else:
#             return "No items in list."
#
#     def search(self, data):
#         node = self.head
#         while node != None:
#             if node.get_data() == data:
#                 return node
#             else:
#                 if node.get_next() == None:
#                     return False
#                 else:
#                     node = node.get_next()
#
#     def print_me(self):
#         if self.head != None:
#             items = []
#             current = self.head
#             items.append(current.data)
#             while current.next != None:
#                 current = current.next
#                 items.append(current.data)
#             return items
#
#         else:
#             return "No items in list."
#
# ll = LinkedList()
# ll.add(4)
# ll.add(23)
# ll.add(9)
# print ll.print_me()
# ll.remove(4)
# ll.add(34)
# ll.add(98)
# print ll.get_size()
# ll.remove(12)
# ll.remove(98)
# print ll.print_me()
# print ll.get_size()
####################################################
# # Singly Linked List with Head and Tail
# class Node:
#
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#     def get_data(self):
#         return self.data
#
#     def get_next(self):
#         return self.next
#
#     def set_data(self, new_data):
#         self.data = new_data
#
#     def set_next(self, new_next):
#         self.next = new_next
#
# class Linked_List:
#
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def add(self, data):
#         new = Node(data)
#         new.set_next(self.head)
#         self.head = new
#
#     def insert_after(self, elem, data):
#         if elem == None:
#             temp = Node(data)
#             temp.next = self.head
#             if self.head == None:
#                 self.tail = temp
#             self.head = temp
#             return True
#         else:
#             cur_elem = self.head
#             while cur_elem != None:
#                 if cur_elem == elem:
#                     temp = Node(data)
#                     if cur_elem.next == None:
#                         cur_elem.next = temp
#                         self.tail = temp
#                     else:
#                         temp.next = cur_elem.next
#                         cur_elem.next = temp
#                     return True
#                 else:
#                     cur_elem = cur_elem.next
#             return False
#
#     def delete(self, elem):
#         if self.head == None:
#             return False
#
#         if elem == self.head and elem == self.tail:
#             self.head = None
#             self.tail = None
#             return True
#
#         cur_elem = self.head
#         pre_elem = None
#         if elem == cur_elem:
#             self.head = cur_elem.next
#             return True
#
#         while cur_elem != None:
#             if cur_elem == elem:
#                 if cur_elem == self.tail:
#                     self.tail = pre_elem
#                 pre_elem.next = cur_elem.next
#                 return True
#             else:
#                 pre_elem = cur_elem
#                 cur_elem = cur_elem.next
#         return False
#
#     def search(self, data):
#         node = self.head
#         while node != None:
#             if node.get_data() == data:
#                 return node
#             else:
#                 if node.get_next() == None:
#                     return False
#                 else:
#                     node = node.get_next()
#
#     def mth_elem(self, m):
#         if m == None or m < 0:
#             return False
#         counter = 0
#         mElem = None
#         curElem = self.head
#         while curElem != None:
#             if mElem != None:
#                 mElem = mElem.next
#             if counter - m == 0:
#                 mElem = self.head
#             curElem = curElem.next
#             counter += 1
#         if mElem != None:
#             return mElem.data
#         return False
#
#     def print_me(self):
#         if self.head != None:
#             items = []
#             current = self.head
#             items.append(current.data)
#             while current.next != None:
#                 current = current.next
#                 items.append(current.data)
#             return items
#
#         else:
#             return "No items in list."
#
# LL = Linked_List()
#
# LL.add(4)
# LL.add(2)
# LL.add(14)
# LL.add(1)
# LL.add(8)
# LL.add(60)
# print LL.print_me()
# print LL.mth_elem(-1)
####################################################
# # Six Degrees of Kevin Bacon: Hash Table Implementation
#
# from collections import deque
# from Tkinter import *
#
# class SixDegrees:
#
#     def __init__(self):
#         self.movies = {}
#         self.actors = {}
#
#     def add_movie(self, movie, actors):
#         self.movies[movie] = actors
#
#     def add_actor(self, actor, movies):
#         self.actors[actor] = movies
#
#     def remove_movie(self, movie):
#         try:
#             del self.movies[movie]
#         except KeyError:
#             return False
#
#     def remove_actor(self, actor):
#         try:
#             del self.actors[actor]
#         except KeyError:
#             return False
#
#     def six_degrees(self, actor):
#         degrees = 1
#         m_que = deque()
#         m_visited = set()
#         a_que = deque([actor])
#         a_visited = set()
#         while a_que or m_que:
#             while a_que:
#                 actor = a_que.popleft()
#                 a_visited.add(actor)
#                 movies = self._search_movies(actor)
#                 for movie in movies:
#                     if movie not in m_visited:
#                         m_que.append(movie)
#             while m_que:
#                 movie = m_que.popleft()
#                 m_visited.add(movie)
#                 actors = self._search_actors(movie)
#                 for actor in actors:
#                     if actor == "Kevin Bacon":
#                         return degrees
#                     if actor not in a_visited:
#                         a_que.append(actor)
#             degrees += 1
#         return None
#
#     def _search_movies(self, actor):
#         try:
#             movies = self.actors[actor]
#             for movie in movies:
#                 yield movie
#         except KeyError:
#             pass
#
#     def _search_actors(self, movie):
#         try:
#             actors = self.movies[movie]
#             for actor in actors:
#                 yield actor
#         except KeyError:
#             pass
#
#     def movies(self):
#         return self.movies
#
#     def actors(self):
#         return self.actors
#
# sixd = SixDegrees()
# sixd.add_movie("Apollo 13", ["Tom Hanks", "Kevin Bacon", "Bill Paxton"])
# sixd.add_movie("Footloose", ["Kevin Bacon", "Lori Singer","John Lithgow"])
# sixd.add_movie("Interstellar", ["Matthew McConaughey", "Anne Hathaway", "John Lithgow"])
# sixd.add_movie("The Dark Knight", ["Christian Bale", "Anne Hathaway", "Gary Oldman"])
# sixd.add_movie("The Prestige", ["Christian Bale", "Hugh Jackman"])
# sixd.add_actor("Kevin Bacon", ["Apollo 13", "Footloose", "Mystic River"])
# sixd.add_actor("Tom Hanks", ["Apollo 13", "Cast Away", "Forrest Gump"])
# sixd.add_actor("John Lithgow", ["Interstellar", "Footloose"])
# sixd.add_actor("Anne Hathaway", ["Les Miserables", "The Dark Knight", "Interstellar"])
# sixd.add_actor("Christian Bale", ["The Prestige", "American Psycho", "The Dark Knight"])
# sixd.add_actor("Hugh Jackman", ["The Prestige", "X-Men"])
# # print sixd.movies
# # print sixd.actors
# print sixd.six_degrees("John Lithgow")
####################################################
# # Binary Search
# import math
#
# def binary_search(arr, val):
#     max = len(arr) - 1
#     min = 0
#     return _iter_binary_search(arr, val, min, max)
#
# def _binary_search(arr, val, min, max):
#     if max < min:
#         return None
#     idx = int(math.floor(float(max - min) / 2 + min))
#     arr_val = arr[idx]
#     if val == arr_val:
#         return idx
#     elif val < arr_val:
#         return _binary_search(arr, val, min, idx - 1)
#     elif val > arr_val:
#         return _binary_search(arr, val, idx + 1, max)
#
# def _iter_binary_search(arr, val, min, max):
#     while max >= min:
#         idx = int(math.floor(float(max - min) / 2 + min))
#         arr_val = arr[idx]
#         if val == arr_val:
#             return idx
#         elif val < arr_val:
#             max = idx - 1
#         elif val > arr_val:
#             min = idx + 1
#     return None
#
# myArr = [3,4,5,7,5623,4,76,8,867,6,345,2,23,3,44,66,45,455,7,8,76,564,34,5364,35]
# myArr.sort()
# val = 5623
# print binary_search(myArr, val)
####################################################
# # Telephone Words
# class PhoneWords:
#
#     def __init__(self):
#         self.options = {
#             2: ["a", "b", "c"],
#             3: ["d", "e", "f"],
#             4: ["g", "h", "i"],
#             5: ["j", "k", "l"],
#             6: ["m", "n", "o"],
#             7: ["p", "r", "s"],
#             8: ["t", "u", "v"],
#             9: ["w", "x", "y"]}
#
#     def print_words(self, nums):
#         chars = [None for x in range(7)]
#         self._pw(nums, chars, 0)
#
#     def _pw(self, nums, chars, d):
#         if d == len(nums):
#             print ", ".join(chars)
#         else:
#             for i in range(3):
#                 chars[d] = self._get_char_key(nums[d], i)
#                 self._pw(nums, chars, d + 1)
#
#     def _get_char_key(self, key, place):
#         return self.options[key][place]
#
# p = PhoneWords()
# p.print_words([8,6,6,2,6,6,5])
####################################################
# Team Formation

#t = 1
#n = [[10, 901, 900, 902, 904, 903, 900, 901, 903, 904, 902]]
#n = [[7,4,5,2,3,-4,-3,-5],[1, -4], [4,3,2,3,1]]
#n = [[8, 101, 102, 103, 104, 105, 106, 103, 104]]

# t = input()
# n = [map(int, raw_input().strip().split(" ")) for _ in range(0,t)]
#
# class contest:
#
#     def __init__(self):
#         self.first_acceptable_list_idx = 0
#         self.min_list = []
#
#     def get_min_max_team(self, t, n):
#         for group in n:
#             cont = group.pop(0)
#             if cont == 0:
#                 self.min_list.append(0)
#             elif cont == 1:
#                 self.min_list.append(1)
#             elif cont > 1:
#                 group.sort()
#                 self.first_acceptable_list_idx = 0
#                 teams = []
#                 cur_team = [1, group[0]] # count of team members, last member added to team
#
#                 for i in range(1, len(group)):
#                     cur_num = group[i]
#                     diff = cur_num - cur_team[len(cur_team) - 1]
#                     if diff == 1:
#                         cur_team[0] += 1 # increment count of team members
#                         cur_team[1] = cur_num # update the last member added to team
#                         continue
#                     elif diff == 0:
#                         if len(teams) > 0:
#                             if self._found_acceptable_list(teams, cur_num):
#                                 continue
#                     elif diff > 1:
#                         self.first_acceptable_list_idx += 1
#                     teams.append(cur_team)
#                     cur_team = [1, cur_num]
#
#                 teams.append(cur_team)
#
#                 min = teams[0][0]
#                 for i in range(1, len(teams)):
#                     if teams[i][0] < min:
#                         min = teams[i][0]
#
#                 self.min_list.append(min)
#
#         print "\n".join(str(x) for x in self.min_list)
#
#     def _found_acceptable_list(self, teams, num):
#         found = False
#         min_acceptable_team = []
#         for team in teams[self.first_acceptable_list_idx:]: # start iterating at last team that was acceptable to skip already unacceptable teams
#             last_item = team[1]
#             if num - last_item == 1:
#                 if len(min_acceptable_team) == 0:
#                     min_acceptable_team = team
#                 else:
#                     if team[0] < min_acceptable_team[0]:
#                         min_acceptable_team = team
#             elif num - last_item > 1:
#                 self.first_acceptable_list_idx += 1 # increment if diff is greater than 1 because that team will never be acceptable again
#
#         if len(min_acceptable_team) > 0:
#             min_acceptable_team[0] += 1
#             min_acceptable_team[1] = num
#             found = True
#
#         return found
#
# c = contest()
# c.get_min_max_team(t, n)
####################################################
# # Numbers
# t = input()
# n = [map(int, raw_input().strip().split(" ")) for _ in range(0,t*2)]
#
# for i in range(0, len(n), 2):
#     elems = n[i]
#     arr = n[i+1]
#
#     if len(arr) == 1:
#         print "YES"
#         continue
#
#     prev_elem = 0
#     for_arr = []
#     for j in range(len(arr)):
#         for_arr.append(prev_elem + arr[j])
#         prev_elem = for_arr[j]
#
#     prev_elem = 0
#     bac_arr = [0 for x in arr]
#     for j in range(len(arr)-1, -1, -1):
#         bac_arr[j] = prev_elem + arr[j]
#         prev_elem = bac_arr[j]
#
#     if 0 == bac_arr[1] or 0 == for_arr[len(for_arr)-2]:
#         print "YES"
#         continue
#     prnt = ""
#     for j in range(1, len(arr)-1):
#         if for_arr[j-1] == bac_arr[j+1]:
#             prnt = "YES"
#             break
#     if prnt == "":
#         print "NO"
#     else:
#         print "YES"
####################################################
# # Primes
# def sum_of_primes():
#     primes = []
#     the_sum = 0
#     i = 2
#
#     while len(primes) < 1000:
#         prime = True
#         for num in primes:
#             if i % num == 0:
#                 prime = False
#                 break
#         if prime:
#             primes.append(i)
#             the_sum += i
#         i += 1
#
#     print the_sum
#
# sum_of_primes()
####################################################
# # Pass Triangle
# test_cases = open('C:\Raul\Pycharm\pass_triangle.txt', 'r')
# i = 0
# j = 1
# the_sum = 0
# for test in test_cases:
#     line = map(int, test.strip().split(' '))
#     if len(line) == 1:
#         the_sum += line[0]
#     else:
#         if line[i] >= line[j]:
#             the_sum += line[i]
#         else:
#             the_sum += line[j]
#             i += 1
#             j += 1
# print the_sum
#
# test_cases.close()
####################################################
# # Sum of Integer
# test = 23
#
# s = map(str, test.strip())
# the_sum = 0
# for num in s:
#     the_sum += int(num)
# print the_sum
####################################################
# Longest Lines
# import heapq
#
# test_cases = open('C:\Raul\Pycharm\pass_triangle.txt', 'r')
# lines_to_print = 0
# the_heap = []
# for test in test_cases:
#     line = test.strip()
#     if line != "":
#         if lines_to_print == 0:
#             lines_to_print = int(line)
#         elif len(the_heap) < lines_to_print:
#             heapq.heappush(the_heap, (len(line), line))
#         elif len(line) > the_heap[0][0]:
#             heapq.heapreplace(the_heap, (len(line), line))
# the_heap.sort()
# for line in reversed(the_heap):
#     print line[1]
#
# test_cases.close()
####################################################
# # Lowercase
#
# test_cases = open('C:\Raul\Pycharm\pass_triangle.txt', 'r')
# for test in test_cases:
#     line = list(test.strip())
#     if len(line) > 0:
#         for i in range(len(line)):
#             char_ord = ord(line[i])
#             if char_ord >= 65 and char_ord <= 90:
#                 line[i] = chr(char_ord + 32)
#         print "".join(line)
# test_cases.close()
#
# print ord('a')
# print ord('A')
# print ord('Z')
####################################################
# # Largest Common String
#
# def LCS(longest_str, cur_str, s1, s2):
#     for idx1 in range(len(s1)):
#         for idx2 in range(len(s2)):
#             if s1[idx1] == s2[idx2]:
#                 cur_str.append(s1[idx1])
#                 if len(s1) == idx1 + 1 or len(s2) == idx2 + 1:
#                     if len(cur_str) > len(longest_str):
#                         return "".join(cur_str)
#                 else:
#                     longest_str = LCS(longest_str, cur_str, s1[idx1 + 1:], s2[idx2 + 1])
#                 cur_str.pop()
#             if len(s2) - 1 == idx2:
#                 cur_str.pop()
#
# test_cases = open('C:\Raul\Pycharm\pass_triangle.txt', 'r')
# for test in test_cases:
#     line = list(test.strip().split(";"))
#     if len(line) > 0:
#         longest_str = ""
#         cur_str = []
#         s1 = line[0]
#         s2 = line[1]
#         LCS(longest_str, cur_str, s1, s2)
#
# test_cases.close()
# ####################################################
# # # Remove Characters
# test_cases = open("C:\Raul\Pycharm\pass_triangle.txt")
# for test in test_cases:
#     line = tuple(test.strip().split(", "))
#     if line[0] != "":
#         chars_to_remove = {c for c in line[1]}
#         output = []
#         for char in line[0]:
#             if char not in chars_to_remove:
#                 output.append(char)
#         print "".join(output)
#
# test_cases.close()
# ####################################################
# # # Reverse and Add
#def is_palindrome(num, reverse):
#    answer = False
#    if str(num) == str(reverse):
#        answer = True
#    return answer

#def reverse_number_add(num, iters):
#    reverse = int(str(num)[::-1])
#    if is_palindrome(num, reverse):
#        return str(iters) + " " + str(num)
#    else:
#        out_str = reverse_number_add(num + reverse, iters + 1)
#    return out_str

#test_cases = open("C:\Raul\Pycharm\pass_triangle.txt")
#for test in test_cases:
#    num = int(test.strip())
#    if num:
#        print reverse_number_add(num, 0)
#test_cases.close()
###############################################
# # Reverse and Add

#test_cases = open("C:\Raul\Pycharm\pass_triangle.txt")
#for test in test_cases:
#    pass
#    # get len of both
#    # iter through s1 from end - len index
#    # if chars from both don't match, print 0
#    # if end, print 1
#test_cases.close()




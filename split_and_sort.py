import sys
import operator

def split_and_sort(sentence, n):
    l = list()
    try:
        n = int(n)
    except TypeError as error:
        return l
    except ValueError as error:
        return l

    # Create a local list to maniulate with ease all data
    l = sentence.split(" ")
    # Create a local dictonary to store all data
    dic =  {}
    for word in l:
        # Store each word in a dictionary with its number of occurence 
        dic.setdefault(word, l.count(word))
    # Return a sorted list from the dictionary created of size n
    l = sorted(dic.items(), key=lambda x:x[0])
    l = sorted(l, key=lambda x:x[1], reverse=True)
    return l[:n]

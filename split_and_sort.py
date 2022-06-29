def split_and_sort(sentence : str, n : int):
    # Working list
    word_list = list()
    # Store all data
    dic = {}
    try:
        n = int(n)
    except TypeError:
        return word_list
    except ValueError:
        return word_list

    # Create a local list to manipulate with ease all data
    word_list = sentence.split(" ")
    for word in word_list:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1

    word_list = sorted(dic.items(), key=lambda x: x[0])
    # Using sort stability to preserve the order after the first sort
    word_list = sorted(word_list, key=lambda x: x[1], reverse=True)

    return word_list[:n]

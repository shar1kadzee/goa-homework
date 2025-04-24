
# 1
def filter_list(l):
    new_list = []
    for i in l:
        if type(i) is int:
            new_list.append(i)
    return new_list

# 2
def disemvowel(string_):
    result = ""
    for j in string_:
        if j not in "aeiouAEIOU":
            result += j
    return result


# 3
def descending_order(num):
    num_str = str(num)
    num_list = list(num_str)
    num_list.sort(reverse=True) 
    sorted_string = "".join(num_list)
    return int(sorted_string)
def unique(ele_list=[]):
    to_return = []
    for el in ele_list:
        if el not in to_return:
            to_return.append(el)
    return to_return


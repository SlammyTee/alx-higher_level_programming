def element_at(my_list, idx):
    if idx < 0:
        return "None"
    list_length = len(my_list)
    if idx >= list_length:
        return "None"
    return my_list[idx]

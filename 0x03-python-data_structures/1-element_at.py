def element_at(my_list, idx):
    # Check if idx is negative
    if idx < 0:
        return "None"
    
    # Calculate the length of the list
    list_length = len(my_list)
    
    # Check if idx is out of range
    if idx >= list_length:
        return "None"
    
    # Return the element at the specified index
    return my_list[idx]

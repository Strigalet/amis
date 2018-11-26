"""
Program which gets list of integers from user and reversing it
"""


def get_list(prompt):
    """
    This function gets a list from the user

    Args:
        prompt:  message to user

    Returns:
         list of strings
    """
    user_string = input(prompt)
    new_list = user_string.split()
    if len(new_list) == 0:
        get_list("It can't be empty! Try again: ")
    return new_list

def int_list(input_list, count=0):
    """
    This function converts list of strings to  list of integers

    Args:
        input_list: A list with strings
        count: stepping in recursion

    Returns:
         list with integers
    """
    if count + 1 == len(input_list):
        return [int(input_list[count])]
    return [int(input_list[count])] + int_list(input_list, count+1)

def get_and_validate_list(prompt):
    """
    This function gets and validates  list from user

    Args:
        prompt:  message to user

    Returns:
         list of integers
    """
    try:
        return int_list(get_list(prompt))
    except ValueError:
        print("Print correct data please: ")
        return get_and_validate_list(prompt)


def reverse(list_to_reverse, step=-1):
    """
    This function reverses a list via accumulation recursion
    Args:
        list_to_reverse: A list to reverse
        step: A step of accumulation recursion
    Returns:
        A reversed list
    """
    if abs(step) == len(list_to_reverse):
        return [list_to_reverse[step]]
    return [list_to_reverse[step]] + reverse(list_to_reverse, step-1)


user_list = get_and_validate_list("Input the spaced string which constains only integers: ")
print(reverse(user_list))
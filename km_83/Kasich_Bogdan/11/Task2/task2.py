"""
Program displays the smallest item in the list using recursion.
"""


def mini(numbers, count=0):
    """
    The  function  that finds minimum in the list with recursion

    Args:
        numbs: list  numbers
        count:  stepping in recursion

    Returns:
         minimum in list
    """
    if count >= len(numbers):
        return numbers[-1]
    conter = numbers[count]
    other = mini(numbers, count+1)
    if conter < other:
        return conter
    else:
        return other



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
        return get_list("It can't be empty! Try again: ")
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


user_list = get_and_validate_list("Input the spaced string which constains only integers: ")
print("The minimum is {}".format(mini(user_list)))
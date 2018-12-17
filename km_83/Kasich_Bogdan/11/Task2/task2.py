"""
Program displays the smallest item in the list using recursion.
"""


def mini(numbers,count=0):
    """
    The  function  that finds minimum in the list with recursion

    Args:
        numbers: list of numbers

    Returns:
         minimum in list
    """
    if count >= len(numbers):
        return numbers[-1]
    current = numbers[count]
    other = mini(numbers, count + 1)
    if current < other:
        return current
    else:
        return other


def inted_list(input_list, count=0):
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
    return [int(input_list[count])] + inted_list(input_list, count+1)


def get_and_validate_list(prompt):
    """
    This function gets and validates list from user

    Args:
        prompt:  message to user

    Returns:
         list of integers
    """
    try:
        user_string = input(prompt)
        user_string = user_string.split()
        if len(user_string) == 0:
            return get_and_validate_list("It can't be empty! Try again: ")
        return inted_list(user_string)
    except ValueError:
        print("Print correct data please: ")
        return get_and_validate_list(prompt)


user_input = get_and_validate_list("Input the spaced string which constains only integers: ")
print("The minimum is "+str(mini(user_input)))
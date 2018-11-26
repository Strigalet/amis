print("The program complements the symbol '*' with words that are less than the specified length(maximum) to the maximum")

def get_max_length(prompt):
    """
    This function gets max length of each word from user


    Args:
        prompt: message to user

     Returns:
         max length

    """
    global length
    try:
        length=int(input(prompt))
    except ValueError:
        print("Print correct data")
        get_max_length("Try aganin: ")
    if length <=0:
        print("Print correct data")
        get_max_length("Try aganin: ")
    return length

def get_string(prompt):
    """
     This function gets from user string and returns it

     Args:
         prompt: message to user

     Returns:
          string
     """
    global text
    text = input(prompt)
    if len(text) == 0:
        print("String can't be empty!")
        get_string("Try again please: ")
    return text


def complementing(length,text):
    """
       This function complements the symbol '*' with words that are less than the specified length(maximum) to the maximum

       Args:
            text: string to change

       Returns:
           Edited string
       """
    list= [str(i) for i in text.split()]
    sort=[]
    for i in list:
        while len(i) < length:
            i+="*"
        sort.append(i)
    return " ".join(sort)


print(complementing(get_max_length("Design the max length of words: "),get_string("Type yourt string: ")))
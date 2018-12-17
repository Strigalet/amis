"""
The program complements the symbol '*' with words that are less than the specified length(maximum) to the maximum
"""

def get_max_length(prompt):
    """
    This function gets max length of each word from user


    Args:
        prompt: message to user

     Returns:
         max length

    """
    try:
        length=int(input(prompt))
    except ValueError:
        print("Print correct data")
        get_max_length("Try again: ")
    if length <=0:
        print("Print correct data")
        get_max_length("Try again: ")
    return length

def get_string(prompt):
    """
     This function gets from user string and returns it

     Args:
         prompt: message to user

     Returns:
          string
     """
    #global text
    text = input(prompt)
    if len(text) == 0:
        print("String can't be empty!")
        get_string("Try again please: ")
    text=text.split()
    return text


def complementing(length,textus,listi=[]):
    """
       This function complements the symbol '*' with words that are less than the specified length(maximum) to the maximum

       Args:
            length: the max length of single word
            textus: string to work
            listi: empty list for joining

       Returns:
           Edited string
       """
    if len(textus)==0:
        return " ".join(listi)
    if len(textus[0])<length:
        listi.append(textus[0]+"*"*(length-len(textus[0])))
    else:
        listi.append(textus[0])
    return complementing(length,textus[1:],listi)



print(complementing(get_max_length("Design the max length of words: "),get_string("Type your string: ")))
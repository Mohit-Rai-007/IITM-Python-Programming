def is_odd_indices_alpha_and_even_indices_digits(string: str) -> bool:
    '''
    Given a string, check if all the odd indices are alphabets and the even indices are digits.

    Note: indices starts from 0.

    Arguments:
    string: str - the input string

    Return:
    bool - True if all odd indices are alphabets and even indices are digits, else False
    '''
    for x in range(len(string)):
        if x%2==0:
            if not string[x].isdigit():
            return False
            
        else:
           if not string[x].isalpha()
           return False
           
    return True
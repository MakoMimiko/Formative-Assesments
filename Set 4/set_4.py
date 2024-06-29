#!/usr/bin/env python
# coding: utf-8

# In[119]:


def bin_to_dec(binary_string):
    '''
    Convert a binary string to its base-10 integer representation.
    
    Example:
    bin_to_dec("101") -> 5
    bin_to_dec("1010") -> 10
    bin_to_dec("11111111") -> 255
    bin_to_dec("0") -> 0
    bin_to_dec("1") -> 1
    
    Parameters
    ----------
    binary_str: str
        The binary string to be converted to a base-10 integer.
        The string should contain only the characters '0' and '1'.
    
    Returns
    -------
    int
        The base-10 integer representation of the input binary string.
    
    Notes
    -----
    Binary is a base-2 number system that uses only two digits: 0 and 1. 
    Each digit in a binary number is called a "bit". The position of each bit 
    represents a power of 2, starting from the rightmost bit (2^0), the next bit 
    to the left (2^1), and so on. To understand a binary number, convert it to 
    decimal by summing the products of each bit and its corresponding power of 2.
    
    For example, the binary string "1011" is calculated as:
    (1 * 2^3) + (0 * 2^2) + (1 * 2^1) + (1 * 2^0)
    = 8 + 0 + 2 + 1 = 11
    '''
    #make a list out of the binary_string
    #then for every element in the string, raise it to the power of the index
    binary_list = list(binary_string)
    leng = len(binary_list)
    numba = 0
    for i in range(leng):
        # print(binary_list[i] + " * " + str(2 **(leng-i-1)))
        # print(binary_list[i])
        numba += int(binary_list[i]) * (2**(leng-i-1))
        # print(numba)
    return numba


# In[ ]:


def dec_to_bin(number):
    '''
    Convert a base-10 number to its binary string representation.
    
    Example:
    dec_to_bin(5) -> "101"
    dec_to_bin(10) -> "1010"
    dec_to_bin(255) -> "11111111"
    dec_to_bin(0) -> "0"
    dec_to_bin(1) -> "1"
    
    Binary is a base-2 number system that uses only two digits: 0 and 1. 
    Each digit in a binary number is called a "bit". The position of each bit 
    represents a power of 2, starting from the rightmost bit (2^0), the next bit 
    to the left (2^1), and so on. To understand a binary number, convert it to 
    decimal by summing the products of each bit and its corresponding power of 2.
    
    Parameters
    ----------
    number: int
        The base-10 integer to be converted to a binary string.
        The number should be a non-negative integer.
    
    Returns
    -------
    str
        The binary string representation of the input base-10 number.
    '''
    #bruh don't you just modulo it until it is a 0 or sm
    #start with the simplest input "11111111"
    binary_poggies = []
    le_remainder = number
    le_power = 0
    #2 while loops (lazy probs smn more efficient) first while loop figures out which power to start at, 2nd while loop is the poggeis
    #im doing an if statement because i am LAZY and also iyak ako
    if number == 0:
        ansuh = '0'
        return ansuh
    while number % (2**le_power) != number:
        le_power += 1
        # print(number % (2**le_power))
    le_power -= 1 # this is the poggers power IM GOING INSANE
    le_stop = le_power + 1
    #noow the actual while loop that does your work for you
    while len(binary_poggies) != le_stop:
        if le_remainder % (2**le_power) < le_remainder:
            le_remainder = le_remainder % (2**le_power)
            binary_poggies.append("1")
        else:
            binary_poggies.append("0")
        # print((2**le_power))
        le_power -=1
        # print(binary_poggies)
    '''chat gpt made it 1 loop idk what to do with my life '''
    ansuh = ''.join(binary_poggies)
    return ansuh


# In[318]:


encoder_dict = {
        " ":"0",
        "A":"2",
        "B":"22",
        "C":"222",
        "D":"3",
        "E":"33",
        "F":"333",
        "G":"4",
        "H":"44",
        "I":"444",
        "J":"5",
        "K":"55",
        "L":"555",
        "M":"6",
        "N":"66",
        "O":"666",
        "P":"7",
        "Q":"77",
        "R":"777",
        "S":"7777",
        "T":"8",
        "U":"88",
        "V":"888",
        "W":"9",
        "X":"99",
        "Y":"999",
        "Z":"9999"
    }
def telephone_cipher(message):
    '''
    Before, when phones did not have touchscreen keypads, 
    the way to input letters was to click the physical keypads 
    repeatedly.
    
    For example:
    Clicking "222" will result in the letter C. 
    Clicking "7777" will result in the letter S. 
    and so on
    
    To read more about it, you may visit the following link:
    Telephone Keypad: https://en.wikipedia.org/wiki/Keypad
    
    Using the `encoder_dict` in "set_4_given.py",
    your task is to convert a letter string into its equivalent
    numerical string as typed in a Telephone Keypad.
    
    Note: In the case of text inputs like "ABC", to demarcate the
    same letters, an underscore "_" is placed in between.
    
    Examples:
    telephone_cipher("ABC") -> "2_22_222"
    telephone_cipher("HELLO WORLD") -> "4433555_555666096667775553"
    telephone_cipher("TEST") -> "83377778"
    telephone_cipher("HOW DO YOU DO") -> "4466690366609996668803666"
    telephone_cipher("ABRACADABRA") -> "2_227772_222_232_227772"
    
    Parameters
    ----------
    message: str
        the text string consisting of capital letters
    
    Returns
    -------
    str
        the equivalent numerical string typed in a Telephone Keypad
        with underscores demarcating characters who share the same key
    '''
    #make a list with the message
    #just do a call LMAO ez MONEH
    lispy_list = list(message)
    krazy = []
    for numba in range(len(message)):
        #wtf list index error
        #ok i need a variable for the current letter
        current_number = encoder_dict.get(message[numba])
        if numba>0:
        #it breaks because append adds to the length
            last_number = encoder_dict.get(message[numba-1])
            if current_number[0] == last_number[0]:
                krazy.append('_')
        krazy.append(current_number)
    ansuh = ''.join(krazy)
    return ansuh


# In[9]:


decipher_dict = {
        "0":" ",
        '2': 'A',
        '22': 'B',
        '222': 'C',
        '3': 'D',
        '33': 'E',
        '333': 'F',
        '4': 'G',
        '44': 'H',
        '444': 'I',
        '5': 'J',
        '55': 'K',
        '555': 'L',
        '6': 'M',
        '66': 'N',
        '666': 'O',
        '7': 'P',
        '77': 'Q',
        '777': 'R',
        '7777': 'S',
        '8': 'T',
        '88': 'U',
        '888': 'V',
        '9': 'W',
        '99': 'X',
        '999': 'Y',
        '9999': 'Z'
    }
def telephone_decipher(telephone_string):
    '''
    Using the `decipher_dict` in "set_4_given.py",
    decrypt a message that was originally typed using the Telephone Keypad
    as done in the `telephone_cipher` function above.
    
    Example:
    telephone_decipher("2_22_222") -> "ABC"
    telephone_decipher("4433555_555666096667775553") -> "HELLO WORLD"
    telephone_decipher("83377778") -> "TEST"
    telephone_decipher("4466690366609996668803666") -> "HOW DO YOU DO"
    telephone_decipher("2_227772_222_232_227772") -> "ABRACADABRA"
    
    Parameters
    ----------
    message: str
        the numerical string typed in a Telephone Keypad
        with underscores demarcating characters who share the same key
    
    Returns
    -------
    str
        the equivalent text string consisting of capital letters
    '''
    #have a current character and old character again to compare with each other. if current character is different from old character . 
    #WAIT, pwede while in while, while loop for the whole range, or for, then an inside while loop "while old character == new character
    tele_list = list(telephone_string)
    decipher = ""
    character = ""
    for i in range(len(tele_list)):
        current_char = tele_list[i]
        if current_char == '_':
            continue
        if i == 0:
            character += current_char
        elif i>0:
            old_char = tele_list[i-1]
            if current_char == old_char:
                character += current_char
            if current_char != old_char:
                decipher += decipher_dict.get(character)
                character = current_char
        if i == len(tele_list) - 1:
            decipher += decipher_dict.get(character)
    return decipher


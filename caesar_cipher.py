import textwrap

def main():
    print()
    options = input("Please enter e to encode, d to decode, q to quit: ")
    options = options.lower()

    if options == "e":        
        string_from_user = input("Enter a string to be encoded: ")        
        count = 1
        while count > 0: 
            try:           
                rotation = int(input("Enter a rotation to be applied to the string: "))
                assert rotation > 0
                count =- 1
            except Exception as error:
                print("ERROR: Only Positive numbers greater than 0 required\n")           

        encrypt(string_from_user, rotation)

    elif options == "d":
        #prompts the user for a string to decode
        input_to_decode = input("Give the string to decode: ")
        count = 1
        while count > 0:
            #Try and except lets you test and handle a block of code for errors
            try:
                #gets the rotation used for the ecryption from the user
                rotation = int(input("What was the rotation: "))
                assert rotation > 0

                #gets the a key from the user.
                key_word = str(input("Give a word in the string: "))
                count = - 1

            except Exception as error:
                print("ERROR: Only Positive numbersgreater than 0 required.\n")        

        decrypt(input_to_decode, rotation, key_word)

    elif options == "q":
        quit()

    else:
        print("Invalid command")


def display_message():
    message = """
In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, 
Caesar's code or Caesar shift, is one of the simplest and most widely known encryption 
techniques. It is a type of substitution cipher in which each letter in the plaintext 
is replaced by a letter some fixed number of positions down the alphabet.

A rotation cipher is one of the simplest, plain-text ciphers, known
since at least the time of Julius Caesar. It takes in a plain-text
string, and translates it into a new string based on a rotation of the
alphabet being used. The basis is a “rotation”, a re-sequencing of an alphabet.
Plain Alphabet	ABCDEFGHIJKLMNOPQRSTUVWXYZ
Caesar Alphabet(+3)DEFGHIJKLMNOPQRSTUVWXYZABC
Crypt DCODEX with a rotation of 3.
To encrypt D, take the alphabet and look 3 letters after: G. So D is encrypted with G.
To encrypt X, loop the alphabet: after X: Y, after Y: Z, after Z: A. So X is coded A.
DCODEX is coded GFRGHA
Another way to crypt, more mathematical, note A=0, B=1, ..., Z=25, and add a constant
(the shift), then the result modulo 26 (alphabet length) is the coded text.

    """    
    message = textwrap.indent(text=message, prefix=" ")
    print(message)

def encrypt(string_from_user, rotation):
    """
    If the command is encode, then the program prompts for a string
    to encode and a rotation integer in the range of 1-25. 
    """      
    a_to_z = "abcdefghijklmnopqrstuvwxyz"    
    string_from_user = string_from_user.lower()
    while rotation > 26:
        rotation = rotation - 26
    #This basis is a “rotation”, a re-sequencing of an alphabet.
    new_a_to_z = a_to_z[rotation:] + a_to_z[:rotation]        
    
    #empty string to hold the encoded string
    encoded_string = ""

    for x in string_from_user:
        if x in a_to_z:
            new_index = a_to_z.index(x)
            encoded_string += new_a_to_z[new_index]
        else:
            encoded_string += x
    print("Your encryted text is:",encoded_string)

    return encoded_string
    
def decrypt(input_to_decode, rotation, key_word):
    """
    If the command is decode, then the program should prompt
    for a string to decode and a plain-text word that appears in
    the text (decoded string). The output should be the rotation
    needed to decode the string and the decoded string (text
    """
    a_to_z = "abcdefghijklmnopqrstuvwxyz"   

    # return lower case version of the string
    input_to_decode = input_to_decode.lower()

    
    key_word = key_word.lower() # returns lower case of the key_word
    while rotation > 26:
        rotation = rotation - 26
    new_a_to_z = a_to_z[rotation:] + a_to_z[:rotation]
    
    decoded_string = ""
    for x in input_to_decode:
        if x in new_a_to_z:
            new_index = new_a_to_z.index(x)
            decoded_string += a_to_z[new_index]
        else:
            decoded_string += x

    temp_container = decoded_string.split(" ")
    if key_word not in temp_container:
        print("couldnt find a decoding.")

    else:
        print("Your decypted text is:",decoded_string)
    
    return decoded_string

def quit():
    print("Thank you! Goodbye.")
    exit()

if __name__ == "__main__":
    display_message()
    while True:
        main()
    

"""
Assignment 1 LFSR Program
Master Program
Levi Hanny Santoso 124721
Mohammad Seyedalizadeh 124744
Mubtasim Islam Sabik 124722
"""
import sys


def starting():
    """
    Starting point, where we check the input.
    Does it satisfied the program or not
    """
    try:
        a = sys.argv[2]
        z = sys.argv[4]
        l = sys.argv[6]
        wronginput1 = sys.argv[1]
        wronginput2 = sys.argv[3]
        wronginput3 = sys.argv[5]
        howToMessage = \
            'python lfsr_124721.py -a Feedback_Coeficient -z Initial_State -l Sequence_Length'
        if wronginput1.lower() != "-a":
            print("This Application only accept this format \n")
            print(howToMessage)
        elif wronginput2.lower() != "-z":
            print("This Application only accept this format \n")
            print(howToMessage)
        elif wronginput3.lower() != "-l":
            print("This Application only accept this format \n")
            print(howToMessage)
        else:
            if a.isalpha() | z.isalpha() | l.isalpha():
                print("This Application only accept this format \n")
                print(howToMessage)
            elif isinstance(wronginput1, str) == False:
                print("This Application only accept this format \n")
                print(howToMessage)
            elif isinstance(wronginput2, str) == False:
                print("This Application only accept this format \n")
                print(howToMessage)
            elif isinstance(wronginput3, str) == False:
                print("This Application only accept this format \n")
                print(howToMessage)
            elif len(a) != len(z):
                print("Feedback Coeficient must equal to Initial State!")
            else:
                calculation(a, z, l)

    except IndexError:
        print("This Application only accept this format \n")
        print(howToMessage)


def calculation(feedbackCoeficients, initialState, sequenceLength):
    """
    Doing the XOR Calculation from the input based on the user's input
    Right now, it is only "efficient" to calculate 4Bit and 8Bit
    """
    binary = int(initialState, 2)
    result = ''
    # add a temporary pod in order to stop the looping
    temp = int(initialState, 2)
    count = 0
    print("Inital State ", "{:04b}".format(binary))
    for i in range(int(sequenceLength)):
        """
            Check in what bits are the user input
            XOR between the most right and the 2nd most right Value for 4Bit
            XOR between the 3rd and 5th from the right Value for 8Bit
            Xor between 1st, 2nd and 7th from the right Value for >8bit
        """
        # From https://www.youtube.com/watch?v=Ks1pw1X22y4
        print("Picked Bit Value= ", binary & 1, end = '')
        result += str(binary & 1)
        # For less than 8Bit
        if len(initialState) < 8:
            # From https://www.youtube.com/watch?v=Ks1pw1X22y4
            newbit = (binary ^ (binary >> 1)) & 1
        # For 8Bit
        elif len(initialState) == 8:
            newbit = (binary ^ (binary >> 3) ^ (binary >> 5)) & 1
        # For more than 8Bit
        elif len(initialState) > 8:
            newbit = (binary ^ (binary >> 1) ^ (binary >> 2) ^ (binary >> 7)) & 1
        print("\nCompared with= ", "{:04b}".format(binary >> 1))
        binary = (binary >> 1) | (newbit << len(initialState)-1)
        print("\nState= ", "{:04b}".format(binary))
        count += 1
        if temp == binary & count == int(sequenceLength):
            print("The program has stopped, because it has reached the Sequence_Length.")
            print('And it will repeat itself since the '\
                'Current_State is the same as the Initial_State.')
            print("Meanwhile the value will be the repeated as the previous step")
            print("\nResult= ", result, end='')
            break
        elif temp == binary | count != int(sequenceLength):
            print('The program has stopped, because the '\
                'Current_State is already the same as the Initial_State.')
            print("Meanwhile it will repeat itself until Sequence_Length is accomplished.")
            print("And it will have the same sequence over and over again.")
            print("\nResult= ", result, end='')
            break
        elif count == int(sequenceLength):
            print("The program has stopped, because it has reached the Sequence_Length.")
            print("\nResult= ", result, end='')
            break
        elif "{:04b}".format(binary) == feedbackCoeficients:
            print("Feedback Coeficient reached in this State!")

if __name__ == "__main__":
    starting()

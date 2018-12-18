
def solve(word):


    while word.find("*") > 0:
        print("the current word is : " + word)
        if (word.find("*")):
           word = multiplication(word)

    while word.find("/") > 0:
        print("the current word is : " + word)
        if (word.find("/")):
          word = division(word)

    while word.find("+") >0:
        print("the current word is : " + word)
        if (word.find("+")):
            word = addition(word)

    while word.find("-") >0:
        print("the current word is : " + word)
        if (word.find("-")):
            word = subtraction(word)

    print("Equation = " + word)
    return word

def subtraction(word):
    left = word.index("-") - 1
    right = word.index("-") + 1
    try:
        sum = int(word[left]) - int(word[right])
    except IndexError:
        return "***Error: There is nothing either on the right or left *** "

    word = str(word.replace( word[left:right+1],str(sum)))
    return word

def addition(word):
    left = word.index("+") - 1
    right = word.index("+") + 1
    print (left, right , word)
    try:
        sum = int(word[left]) + int(word[right])
    except IndexError:
        return "***Error: There is nothing either on the right or left *** "

    word = str(word.replace( word[left:right+1],str(sum)))
    return word


def multiplication(word):
    left = word.index("*") - 1
    right = word.index("*") + 1
    try:
        sum = int(word[left]) * int(word[right])
    except IndexError:
        return "***Error: There is nothing either on the right or left *** "

    word = str(word.replace(word[left:right + 1], str(sum)))
    return word

def division(word):
    left = word.index("/") - 1
    right = word.index("/") + 1
    try:
        try:
            sum = int(word[left]) / int(word[right])
        except IndexError:
            return "***Error: There is nothing either on the right or left *** "
    except ZeroDivisionError:
        return " Error: Cannot Divide by Zero "

    word = str(word.replace(word[left:right + 1], str(sum)))
    return word

def trigramFirst(inputStr):
    """
    First attempt Trigram subroutine that takes an input string
    splits the input string and stores each element in a list
    then outputs groups of three consecutive elements for all except the last two
    """
    splitStr = inputStr.split()
    for i in range(len(splitStr)-2):
        print(splitStr[i] + " " + splitStr[i+1] + " " + splitStr[i+2])
        

def trigram (inputStr):
    """
    Improved trigram subroutine that calls ngram with inputStr and 3 as params
    """
    ngram(inputStr, 3)


def ngram(inputStr, n: int):
    """
    n-gram subroutine that takes an input string
    splits the input string and stores each element in a list
    then for every element it concatenates n consecutive elements to the output string
    assumption: user can't enter negatives or non-ints, n value greater than number of words in n-gram would not be valid
    """
    splitStr = inputStr.split()
    if ((n <= len(splitStr)) and (n > 0)):
        for i in range(len(splitStr)-n+1):
            outStr = splitStr[i]
            for j in range(n-1):
                outStr = outStr + " " + splitStr[i+j+1]
            print(outStr)
    else:
        print("No n-grams found")
            

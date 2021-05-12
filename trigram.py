def trigram(inputStr):
    """
    Trigram subroutine that takes an input string
    splits the input string and stores each element in a list
    then outputs groups of three consecutive elements for all except the last two
    """
    splitStr = inputStr.split()
    for i in range(len(splitStr)-2):
        print(splitStr[i] + " " + splitStr[i+1] + " " + splitStr[i+2])

def ngram(inputStr, n):
    """
    n-gram subroutine that takes an input string
    splits the input string and stores each element in a list
    then for every element it concatenates n consecutive elements to the output string
    """
    splitStr = inputStr.split()
    if (n <= len(splitStr)):
        for i in range(len(splitStr)-n+1):
            outStr = ""
            for j in range(n):
                outStr = outStr + " " + splitStr[i+j]
            print(outStr)
    else:
        print("No n-grams found")
    

def main():
    trigram("Little Red Riding Hood is walking in the forest")
            

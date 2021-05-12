def trigram(inputStr):
    splitStr = inputStr.split()
    for i in range(len(splitStr)-2):
        print(splitStr[i] + " " + splitStr[i+1] + " " + splitStr[i+2])

def main():
    trigram("Little Red Riding Hood is walking in the forest")
            

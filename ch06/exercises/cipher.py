#Austin Bardsley
def cipher(filename):
    """
    reads a file and returns a string where each letter is moved forward by 
    2 in a randomized list of all letters (capital and lowercase) and numbers
    args: filename
    return: string
    """
    alphabet = "eRzkK1y0wPLvdAFlrq6xDgQc8SNtinUf7Ip2aBoYH54sVBGb3EhCJZXAMujTmWbO9aeR"
    fileref = open(filename,'r')
    coded = ""
    for i in fileref.read():    
        if i.isalnum(): 
            for j, obj in enumerate(alphabet):
                if i == obj:
                    coded += (alphabet[j+2])
                    break
        else:
            coded += i
    fileref.close
    return coded

def main():
    filename = str(input("Enter Filename: "))
    coded = "encrypted.py"
    coded = open(coded,"w")
    coded.write(cipher(filename))
    coded.close()
main()
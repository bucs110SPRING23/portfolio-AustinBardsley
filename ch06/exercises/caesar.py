#Austin Bardsley
def cipher(filename):
    """
    reads a file and returns a string where each letter is moved forward by 2 
    args: filename
    return: string
    """
    alphabet = "abcdefghijklmnopqrstuvwxyzabABCDEFGHIJKLMNOPQRSTUVWXYZAB"
    fileref = open(filename,'r')
    coded = ""
    for i in fileref.read():    
        
        if i in alphabet: 
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

    coded = (filename+".coded")
    coded = open(coded,"w")
    coded.write(cipher(filename))
    coded.close()
main()
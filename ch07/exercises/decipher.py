def main():
    encrypted = open('encrypted-#B00829653.txt','r').read()
    decrypted = ""  
    jump = abs(ord(encrypted[0])-ord("T"))
    for ch in encrypted:
        if ch.isalpha() and ch.isupper():
            decrypted += chr(((ord(ch)-ord("A")+jump)%26)+ord('A'))
        elif ch.isalpha() and ch.islower():
            decrypted += chr(((ord(ch)-ord("a")+jump)%26)+ord('a'))
        else:
            decrypted += ch
    solved = open('decrypted.txt','w')
    solved.write(decrypted)

main()
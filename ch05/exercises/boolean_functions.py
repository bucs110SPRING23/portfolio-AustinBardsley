def main():
    def numberToLetter(a=100):
        if a >= 90:
            return "A"
        elif a>= 80:
            return "B"
        elif a>= 70:
            return "C"
        elif a>= 60:
            return "D"
        else:
            return "F"

    def letterToPass(Grade):
        if Grade == "A" or Grade == "B" or Grade == "C":
            return "Pass"
        else:
            return "Fail"
    grade = int(input("Enter Grade:"))
    Letter = (numberToLetter(grade))
    pass_fail = (letterToPass(Letter))
    print(Letter)
    print(pass_fail)
    
main()

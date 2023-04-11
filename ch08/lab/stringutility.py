class StringUtility:
    def __init__(self,string):
        self.string = string
        vowels = 0
    def __str__(self):
        return self.string
    def vowels(self):
        """ counts the number of vowels in the string
        args: self
        return: str """
        vowels = 0
        for i in self.string:
            if i in "aeiou":
                vowels += 1
        if vowels >= 5:
            vowels = "many"
        return str(vowels)
    def bothEnds(self):
        """returns of string with the first two and last two letters of the string if string length > 2
        args: self
        return: str """
        if len(self.string) > 2:
            return f"{self.string[0]}{self.string[1]}{self.string[-2]}{self.string[-1]}"
        else:
            return ''
    def fixStart(self):
        """return a string where all occurrences of the first character have been changed to '*', except do not change the first
        args:self
        return: str"""
        new_string = ""
        for i in self.string:
            if i == self.string[0] and new_string != '':
                    new_string += "*"
            else:
                new_string += i
        return new_string
    def asciiSum(self):
        """return an int that contains the sum of all ascii values in the string.
        args: self
        return: str"""
        sum =0
        for i in self.string:
            sum+=(ord(i))
        return sum
    def cipher(self):
        """return an encoded string by incrementing all letters by the length of the string. non-letters unchanged
        args: self
        return: str"""
        result = ""
        for char in self.string:
            if char.isalpha():
            
                start = ord('A') if char.isupper() else ord('a')
                
                new_pos = (ord(char) - start + len(self.string)) % 26
                
                char = chr(start + new_pos)
            result += char
        return result

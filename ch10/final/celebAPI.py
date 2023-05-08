import requests

class CelebAPI:
    def __init__(self,name):
        """requests information from the API about a given person (bday, hometown, height etc.)
        args: name (str)
        return: None"""
        self.name = name
        self.url = f"https://api.api-ninjas.com/v1/celebrity?name={self.name}"
        self.celeb_info = requests.get(self.url, headers={'X-Api-Key': 'UP5njj6R6BjlEidqcEcFcA==ikOTeZT08hEb0LZ2'}).json()
    def getBirthday(self):
        """returns the birthday of the requested celebrity
        args: self
        return: string"""
        if len(self.celeb_info) > 0:
            bday = self.celeb_info[0]["birthday"]
        else:
            bday = "ERROR"
        return bday
    
    def __str__(self):
        return str(f"Celebrity: {self.name}")
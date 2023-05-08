import requests
class HistoricalAPI:
    def __init__(self,year,month):
        """requests a historical event from the given year and month from the API
        stores this information in a list
        args: year(int), month(int)
        return: None"""
        self.year = year
        self.month = month
        
        self.url = f"https://api.api-ninjas.com/v1/historicalevents?year={self.year}&month={self.month}"
        self.historical_fact = requests.get(self.url, headers={'X-Api-Key': 'UP5njj6R6BjlEidqcEcFcA==ikOTeZT08hEb0LZ2'}).json()
    def __str__(self):
        return f"Year = {self.year}, Month = {self.month}"
    
    def getFact(self):
        """returns a historical event from the requested month
        args: self
        return: string"""
        if len(self.historical_fact) > 0:
            event = self.historical_fact[0]["event"]
        else:
            event = "ERROR"
        return event
    def changeDate(self,new_year,new_month):
        """changes the year and month parameters of the request and gets a new url and request to be used by get_fact
        args: new_year(int), new_month(int)
        return: None """
        self.url = f"https://api.api-ninjas.com/v1/historicalevents?year={new_year}&month={new_month}"
        self.historical_fact = requests.get(self.url, headers={'X-Api-Key': 'UP5njj6R6BjlEidqcEcFcA==ikOTeZT08hEb0LZ2'}).json()


    


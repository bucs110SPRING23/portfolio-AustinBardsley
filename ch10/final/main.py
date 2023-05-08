import celebAPI
import historicalAPI
import random
def main():
    again = "yes"
    while again == "yes":
        Name = input("Enter Celebrity Name: ")
        celeb_info = celebAPI.CelebAPI(Name)
        bday = celeb_info.getBirthday()
        if bday == "ERROR":
            print("Sorry, the API doesn't know this person.")
            again = input("If you'd like to try a different name, type yes: ")
        else:
            year = str(bday[0:4])
            month = str(bday[5:7])
            print(f"{Name} was born on: {bday}")
            historical_info = historicalAPI.HistoricalAPI(year,month)
            facts = {"fact0" : historical_info.getFact()}
            if facts["fact0"] == "ERROR":
                print("Unfortunately, the API doesn't have a fact from this month.")
                again = input("If you'd like to try a different name, type yes: ")
            else:
                for i in range(3):
                    while 1:
                        random_year = random.randint(0,90)
                        random_month = random.randint(0,12)
                        historical_info.changeDate((1930+random_year),(1+random_month))
                        new_fact = historical_info.getFact()
                        if new_fact != "ERROR":
                            facts[f"fact{i+1}"] = new_fact
                            break
                shuffle_num = random.randint(1,4)
                print("Which one of these events happened during that month:")
                print("1)")
                print(facts[f"fact{(shuffle_num)%4}"])
                print("2)")
                print(facts[f"fact{((shuffle_num+1)%4)}"])
                print("3)")
                print(facts[f"fact{((shuffle_num+2)%4)}"])
                print("4)")
                print(facts[f"fact{((shuffle_num+3)%4)}"])
                ans = input("Enter your guess (1,2,3,4): ")
                if int(ans) == (5-shuffle_num):
                    print("You Are Correct")
                else:
                    print(f"Unfortuneately, the correct answer was {5-shuffle_num}")

                again = input("If you would like to go again, type yes: ")
                
main()

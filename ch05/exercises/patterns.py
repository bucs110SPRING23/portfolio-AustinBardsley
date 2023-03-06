def star_pyramid():
    rows = int(input("Enter Number of Rows:"))
    for i in range(rows):
        print((i+1)*"*")

def rstar_pyramid():
    rows = int(input("Enter Number of Rows:"))
    for i in range(rows):
        print((rows-i)*"*")

rstar_pyramid()

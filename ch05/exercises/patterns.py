def main():    
    def star_pyramid(rows):
        for i in range(rows):
            print((i+1)*"*")

    def rstar_pyramid(rows):
        for i in range(rows):
            print((rows-i)*"*")

    rows = int(input("Enter Number of Rows:"))
    star_pyramid(rows)
    rstar_pyramid(rows)
main()
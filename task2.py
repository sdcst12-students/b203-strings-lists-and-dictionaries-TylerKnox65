#!python3

'''
use a for loop to iterate through all possible integers to find the factors of 24
'''
def main():
    factors = []
    myNumber = 24
    for i in range(myNumber):
        
        if (myNumber) % (i+1) == 0:
            print(i+1)

if __name__ == "__main__":
    main()
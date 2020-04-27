#A function to find square of number

def square(x):
    return x * x

def main(): #this helps when we are calling this function and we dont want all the codes
    for i in range(5):
        print("{} squared is {}".format(i, square(i)))
#format is plugging in number i is value of i and square will store in another braces

#this helps to run the main function when calling this file
if __name__ == "__main__": 
# It means if I am running this file then run the main function so it wont run when
# this function is called by another function
    main()
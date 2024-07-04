import sys
import statistics

def main():
    filename = input("Enter filename: ")
    array = []
    flag = True

    try:
        with open(filename, "r") as file:
        # Read each line in the file
            for line in file:
                # Convert line from string to integer
                number = int(line.strip())  # strip the spaces at the end of the lines
                array.append(number)  # Append the number to the list

    except:
        flag = False
        print("Error: incorrect input text")
        print("Usage: \"filename.txt\"")

    if len(array) < 1:
        flag = False
        print("File is empty")

    if flag:
        print("Average: ", average(array))
        print("Median: ", median(array))
        print("Variance: ", var(array)) 
    #   std = standard_dev(filename)
    # else:                               needs fix, exit the function if error
        # SystemExit



def average(array): #finds the average of the numbers in the array
    
    total = sum(array)   #finds the sum of the numbers in the array
    length = len(array)  #finds the length of the numbers in the array

    result = total // length #finds the average of the numbers and returns a whole number
    return result

def median(array): #finds the median of the numbers in the array

    array.sort()
    length = len(array)

    if length % 2 != 0: #if umber of values are odd
        med = length // 2 #find median position in the array
        result = array[med] #find the median value in given position
    else:
        mid1 = (length // 2) - 1
        mid2 = (length // 2)
        result = array[(mid1 + mid2)//2]
    
    return result

def var(array): #finds the median of the numbers in the array

    result = statistics.variance(array)
    return result


if __name__ == "__main__":
    main()

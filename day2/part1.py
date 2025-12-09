
from functools import reduce 
# Load in test and input 
with open("test.txt", "r", encoding="utf-8") as f:
    test = [x.strip() for x in f.read().split(',')]

with open("input.txt", "r", encoding="utf-8") as f:
    input = [x.strip() for x in f.read().split(',')]

# Code
def normalize_range(rangeString): 


    #input '11-22', output 11, 22 (integers)
    #input '552-1005', output 1000, 1005 (integers)
    #inut '414256-608125', output 414256, 608125 

    split_arr = rangeString.split('-')

    bottom_length = len(split_arr[0])
    top_length = len(split_arr[1])

    bottom = split_arr[0]
    top = split_arr[1]
    #handle if they are odd 
    if bottom_length % 2 != 0:
        bottom = '1' + ('0' * bottom_length)

    if top_length % 2 != 0: 
        top = '9' * (top_length - 1)

    return bottom, top

def validSRange(bottom, top): #should detect if there are no valid numbers. 
    
    #takes in input of a valid range where both numbers have the same even length e.g. '6985', '9999'
    #outputs the valid range of S such that numbers are of the form SS, e.g 70-99 [7070, 7171, ... 9999]

    bottomlen = len(bottom) #even
    toplen = len(top) #even
    if(toplen != bottomlen): return 'Error, top and bottom aret the same' + top + bottom

    #Find minimum valid S from bottom
    min_valid_s = int(bottom[ : (bottomlen // 2)]) #first n/2 characters
    currentValue = min_valid_s * (10 ** (bottomlen // 2)) + min_valid_s

    #print(min_valid_s)
    while(currentValue < int(top)):

        currentValue = min_valid_s * (10 ** (bottomlen // 2)) + min_valid_s
        #print(currentValue)

        if currentValue >= int(bottom) and currentValue <= int(top):
            break 

        min_valid_s += 1 

    #Find maximum valid S from top 
    max_valid_s = int(top[ : (toplen // 2)]) #first n/2 characters
    currentValue = max_valid_s * (10 ** (bottomlen // 2)) + max_valid_s

    while(currentValue > int(bottom)):

        currentValue = max_valid_s * (10 ** (toplen // 2)) + max_valid_s
        
        #print(currentValue, "hey")

        if currentValue >= int(bottom) and currentValue <= int(top):
            #print(currentValue, "hey")
            break 

        max_valid_s -=1
    
    return min_valid_s, max_valid_s

def rangeToArr(bottom, top):

    if(len(str(bottom)) != len(str(top))):
        return "Error in rangeToArr"

    n = len(str(bottom))
    output = [] 

    for val in range(bottom, top+1):
        
        number = val * (10 ** n) + val 
        output.append(number)

    return output

def driver(arr):

    total = 0
    #iterate through array 
    for idRange in arr:  #'123-156' 
        
        print("id range", idRange)
        bottom, top = normalize_range(idRange)

        if(int(bottom) > int(top)):
            continue

        min_valid_s, max_valid_s = validSRange(bottom, top)

        if(min_valid_s > max_valid_s):
            continue

        arrOfInvalids = rangeToArr(min_valid_s, max_valid_s)
        total += reduce(lambda x, y: x+y, arrOfInvalids)

    return total 
#Tests
print("########## Tests ##########")
print(driver(input))
print("########## Tests ##########")

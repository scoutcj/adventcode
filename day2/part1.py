
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

    print(top_length - bottom_length)

    bottom = split_arr[0]
    top = split_arr[1]
    #handle if they are odd 
    if bottom_length % 2 != 0:
        bottom = '1' + ('0' * bottom_length)

    if top_length % 2 != 0: 
        top = '9' * (top_length - 1)

    return bottom, top

def validSRange(bottom, top): 
    
    #takes in input of a valid range where both numbers have the same even length e.g. '6985', '9999'
    #outputs the valid range of S such that numbers are of the form SS, e.g 70-99 [7070, 7171, ... 9999]

    bottomlen = len(bottom) #even
    toplen = len(top) #even

    #Find minimum valid S from bottom
    min_valid_s = int(bottom[ : (bottomlen // 2)]) #first n/2 characters
    bottom = int(bottom)
    top = int(top)

    while(True):

        currentValue = min_valid_s * (10 ** (bottomlen // 2))

        if currentValue >= bottom and currentValue <= top:
            break 

        min_valid_s += 1 

    return min_valid_s



    #Find maximum valid S from top 
    



# Testing 
#print(test)
#print(normalize_range('6985-10895'))
print(validSRange('6985', '9999'))

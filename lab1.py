def fun3(num, mult):
    multLst = []
    for i in range(0, num):
        if (i % mult == 0):
            multLst.append(mult)
    return multLst
#print(fun3(16,3))

def fun4(intLst):
    returnLst = intLst.copy()
    for elem in range(0,len(intLst)):
        if (intLst[elem] % 2 == 0):
            returnLst.pop(elem)
    return returnLst
def syl(word):
    output=word.split('-')
    return len(output)

def alternate_strings(str1,str2):
    str1_length = len(str1)
    str2_length = len(str2)
    combined_length = str1_length + str2_length
    new_string=""
    for i in range(combined_length):
        if i < str1_length:
            new_string = new_string + str1[i]
        if i < str2_length:
            new_string = new_string + str2[i]
    print(new_string)
#alternate_strings(str1,str2)
#print(syl('fun')) 
#print(fun4([1,3,5,8,10,13]))
def completely_odd(num):
    num=f'{num}'
    print(num)
    for digit in num:
            if int(digit)%2==0:
                return False
            else:
                continue
    return True
#print(completely_odd(9359))
nums=[1,3,4,10,15]
def first_divisible(nums):
    for num in nums:
        if num % 2 == 0:
            return nums.index(num)
    return None
#print(first_divisible(nums))


def count_dummy(lst):
    counter = 0
    for item in lst:
        if item == 'dummy':
            counter = counter + 1
    return counter

def elim_dummy(lst):
    result_lst = []
    for item in lst:
        if not(item == 'dummy'):
            result_lst.append(item)
    return result_lst

def contains(low,high,key):
    if key >= low and key<=high:
        return True
    else:
        return False
    

#print(contains(14,26,26))
#print(elim_dummy(['H','dummy','','e','l','e','l','dummy']))
def pastry_boxes(day, pastries):
    if day in ['Sat','Sun']:
        return pastries
    elif pastries % 7 == 0:
        return pastries / 7
    else:
        return int(pastries/7) + 1

def word_match(word, wordLst):
        for i in range(len(wordLst)):
                if wordLst[i]==word:
                        return word
                if wordLst[i][1:] == word or wordLst[i][:-1] == word:
                        return wordLst[i]
                else:
                    mismatch=0
                    for j in range(len(word)):
                        print(j)
                        if word[j]!=wordLst[i][j]:
                            mistmatch = mismatch + 1
                    if mistmatch < 2:
                        return wordLst[i]
                    else:
                        return None
                        
print(word_match('rock',['something','word','rack','cafe']))

def aritmetic(list):
    jami = sum(list)
    sigrze = len(list)
    return jami / sigrze

list = [1,2,3,4,5,6,7,8,9,10]
print(aritmetic(list))




def reverse(text):
    if text[1::] == text:
        return "es ricxvi palindromia "
    else:
        return "es ricxvi ar aris palindromi"
    
level = "level"
print(reverse(level))




def space(text):
    return text.replace("","")
print(space("h e l l o"))


def negative_positive(nums):
    sum_of_positives = 0
    for i in nums:
        if i < 0:
            lenght_of_negative += 1
        elif i > 0:
            sum_of_positives += i
            return  sum_of_positives,lenght_of_negative
    list = [1,-2,3,-4,5,-6,7,-8,9,10]
    print(negative_positive(list))
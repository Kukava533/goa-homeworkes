
def manual_pop(list,i=-1):
    ans = []
    for j in range(len(list)):
        if j != i:
            ans.append(list[j])
            return ans
        print(manual_pop([1,2,4,6,77,88,00,75]))




def manual_count(list,k):
    print(manual_count([1,4,8,2,5,7,5,7,43,3,4,],4))



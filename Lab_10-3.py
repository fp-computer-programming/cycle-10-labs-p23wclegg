#Lab_10-3

def double_stuff(list):
    for i, v in enumerate(list):
#List function for doubling
        list[i]=v**2
        print(i,v)
#Using i and v to enumerate all types of lists by allowing the index and value of a sequence to be used

#TEST CASES
double_stuff([2,4,6])
double_stuff([-2,-4,-6])
double_stuff([0,1,2])
double_stuff([.2,.5,.9])
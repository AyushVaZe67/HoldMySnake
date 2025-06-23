def avg(a=1,b=3):
    print((a+b)/2)

def name(fname='Ayush',sname='VaZe'):
    print(fname + ' '  + sname)

def average(*nums):
    sum = 0
    for i in nums:
        sum = sum + i
    return sum/len(nums)

print(average(10,30))



# name('Ayush')
# avg(14,12)
# name('Mia')



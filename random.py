
# number = int(input("Pick a three digit number: "))

# while True:
#     print(f"Your number is{number}")
#     number = number * 7
#     print(f'After multiplying with 7{number}')
#     number = number * 11
#     print(f'After multiplying with 11 {number}')
#     number = number * 13
#     print(f'After multiplying with 13 {number}')

def sum_all(*nums): 
    sum = 0
    for x in nums:
        sum += x
    return sum
    
    
    

answer = sum_all(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)
print(answer)


def recursion(list):
    try:
        num = list.pop()
    except:
        return 0
    return num + recursion(list)

    
print(recursion([1,2,3,4,5,6,7,8,9,10]))
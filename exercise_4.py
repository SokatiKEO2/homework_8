
def chunking_by(numbers, chunk):
    number_of_chunk = len(numbers) // chunk #how many sublist that has the wanted chunk len
    result = []
    #iterate thru the number of sublist(s) starts from 0 
    for i in range(number_of_chunk):
        temp_list = []
        for j in range(chunk): #count the chunk starts from 0 
            #append the first number in the list to a new list as well as remove it out of the list
            temp_list.append(numbers.pop(0))
#numbers.pop(0) will remove the first number from the list and show that number so that append can add it to the temp_list
        result.append(temp_list)

    if numbers:  # to check if there is remaining element in numbers / python will return true if there is
        result.append(numbers)

    return result


print("Welcome to the chunking assistace")
print("Directions on how to use this: ")
print("1. enter as many number you want and type \"done\" when you finish.")
print("2. Type in the size you want your list to be chunk into e.g 3")
user_list = []
while True:
    user = input("Enter number: ")
    if user.lower() == "done":
        break
    user_list.append(int(user))

user_chunk = int(input("Chunk size: "))
print(chunking_by(user_list, user_chunk))
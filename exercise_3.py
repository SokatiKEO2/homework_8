def remove_all_after(numbers, n):
    new_nums = []
    for num in numbers:
        new_nums.append(num)
        if num == n:
            break
    return new_nums

print("<Remove all numbers after>")
print("1. Enter a series of number separated by commas eg: 2,5,6,7")
print("2. Enter a number you want to remove after eg: 5")
print("3. Output would be [2, 5]\n\n")
while True:
    try:
        user_input = input("Enter numbers separated by commas: ")
        numbers = user_input.split(',')
        numbers = [int(num) for num in numbers]

        num_to_remove = int(input("What number do you wantthe list to remove after?: "))
        result = remove_all_after(numbers, num_to_remove)
        
        print(f'All numbers: {numbers}\nRemove after {num_to_remove}\nResult: {result}')
        again = input('Again? Y|N\n').lower()
        if again != "y":
            break
    except ValueError:
        print("please input a valid value")
def reverse_ascending(numbers):
    result = []
    start = 0

    for i in range(1, len(numbers)):
        if numbers[i] <= numbers[i - 1]:
            # Here we reverse the elements of the ascending subsequence and add them to result
            result.extend(reversed(numbers[start:i]))
            start = i
    # here we add the last ascending subsequence (if any) to the result list
    result.extend(reversed(numbers[start:]))

    return result
    
def main():
    user_input = input("\033[93mEnter a list of integers separated by commas: \033[0m")

    items = list(map(int, user_input.split(',')))
    result = reverse_ascending(items)
    result_str = str(result)
    # Create the box border
    box_width = max(len(result_str) + 4, 20) 
    border = "\033[95m┌" + "─" * (box_width - 2) + "┐\033[0m"
    middle_line = "\033[95m│" + result_str.center(box_width - 2) + "│\033[0m"
    bottom_border = "\033[95m└" + "─" * (box_width - 2) + "┘\033[0m"

   # display result
    print("\033[95mThis is the result: \033[0m")
    print(border)
    print(middle_line)
    print(bottom_border)

if __name__ == "__main__":
    main()




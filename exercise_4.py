def chunking_by(numbers, chunck):
    new_chunk = []
    for i in range(0, len(numbers), chunck):
        new_chunk.append(numbers[i:i+chunck])

    return new_chunk

#UI

while True:
    try:
        num = input("Please input the number serparated by commas: ")
        num_list = num.split(',')
        num_list = [int(num) for num in num_list]
        
        chunck = int(input('How much do you want to chunk by?: '))
        result = chunking_by(num_list, chunck)
        
        print(f'List: {num_list}\nChunck by: {chunck}\nResult: {result}')
        again = input("Again? Y|N ").lower()
        if again != "y":
            break
        
    except ValueError:
        print("Please enter a valid input")
        break
from colorama import Fore, Style

def index_power(numbers, n):       
    n = int(n)    
    if n < len(numbers):
        square = numbers[n] ** n
        return square
    return -1
 

print(f"""
                                   
                                   
{Fore.LIGHTYELLOW_EX}            _____           _               ___                       
            \_   \_ __   __| | _____  __   / _ \_____      _____ _ __ 
             / /\/ '_ \ / _` |/ _ \ \/ /  / /_)/ _ \ \ /\ / / _ \ '__|
          /\/ /_ | | | | (_| |  __/>  <  / ___/ (_) \ V  V /  __/ |   
          \____/ |_| |_|\__,_|\___/_/\_\ \/    \___/ \_/\_/ \___|_|   {Style.RESET_ALL}
                  \ \                                 / /   
                    \ \                             / /
                      \ \                         / /  
                        \ \                     / /   
                          \ \                 / /   
                            \ \             / / 
                     __...--~~\ \-._   _.-/ /~~--...__   
                  / /           \ \ `V' / /           \ \    
                 / /              \  |  /              \ \    
                / /__...--~~~~~~-._  |  _.-~~~~~~--...__\ \ 
               / /__.....----~~~~._\ | /_.~~~~----.....__\ \ 
              ===================== \|/ ======================
                                   `---`
""")
while True: 
    print("        ✨Follow the instruction 1️⃣ and 2️⃣ to get the result")
    print(f"{Fore.LIGHTMAGENTA_EX}     -------------------------------------------------------------{Style.RESET_ALL}")
    numberInput= input("        Enter a list of numbers (commas-separated): ")
    print(f"{Fore.LIGHTMAGENTA_EX}     -------------------------------------------------------------{Style.RESET_ALL}")
    n = input("        Enter an index: ")

    numbers = [int(num.strip()) for num in numberInput.split(',')]
    #Split the numbers from user input into individual substring 
    # and convert the each substring from 'string' to 'integer'
    # and store them in variable 'numbers'


    print(f"""   
                    .___________________.
                    |.-----------------.|
                    ||                 ||
                    || {Fore.RED}The result{Style.RESET_ALL}      ||
                    || {Fore.RED}is{Style.RESET_ALL}              ||
                    || {Fore.CYAN}{index_power(numbers, n)}{Style.RESET_ALL}           
                    ||                 ||
                    ||_________________||
                     /.-.-.-.-.-.-.-.-.\ 
                    /.-.-.-.-.-.-.-.-.-.\ 
                   /.-.-.-.-.-.-.-.-.-.-.\ 
                  /______/__________\___o_\ 
                  \_______________________/
    """)
    print(f"{Fore.LIGHTMAGENTA_EX}     -------------------------------------------------------------{Style.RESET_ALL}")
    con = input("       Do you want to continue? (Y?N): ")
    print(f"{Fore.LIGHTMAGENTA_EX}     -------------------------------------------------------------{Style.RESET_ALL}")
    if con.lower() == 'n':
        print(f"""
               ____
            .-" +' "-.      
           /.'.'A_'*`.\     
          |:.*'/\-\. ':|    {Fore.YELLOW}Thank you!{Style.RESET_ALL}
          |:.'.||"|.'*:|    
           \:~^~^~^~^:/     {Fore.YELLOW}Hope you have a great day ^^{Style.RESET_ALL}
    {Fore.LIGHTGREEN_EX}        /`-....-'\     
           /          \     
           `-.,____,.-'

""")
        break




 
def collatz(number):
    if number % 2 ==0:
        return number / 2
    elif number % 2 == 1:
        return number * 3 + 1
    
print('Please enter a number:')
number = input()
number = int(number)
try:
    while number != 1:
        number=collatz(number)
        print(number)
except ValueError:
    print("Please enter an integal number:")
          
    

import random

def generate_random_integers_file(filename, num_integers, min_value, max_value):
    with open(filename, 'w') as file:
        numbers = [str(random.randint(min_value, max_value)) for _ in range(num_integers)]
        file.write(' '.join(numbers))

generate_random_integers_file('15000.txt', 15000, 1, 15000)




"""

numbers = list(range(1, 15001))  
def generate_shuffled_numbers_file(filename):
    numbers = numbers.reverse()

    with open(filename, 'w') as file:
        for number in numbers:
            file.write(f"{number} ") 

generate_shuffled_numbers_file('sh'+ str(len(numbers))+'.txt')

"""



numbers = list(range(500, 0, -1))
def generate_reversed_numbers_file(filename):
    with open(filename, 'w') as file:
        for number in numbers:  
            file.write(f"{number} ")  

generate_reversed_numbers_file('r'+ str(len(numbers))+'.txt')

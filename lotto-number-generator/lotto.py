import random

def generate_lotto_numbers():
    numbers = list(range(1, 46))
    random.shuffle(numbers)
    selected_numbers = numbers[:6]
    selected_numbers.sort()
    return selected_numbers

lotto_numbers = generate_lotto_numbers()
print("로또 번호:", lotto_numbers)

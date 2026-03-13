from typing     import List
import numpy as np

# these functions are a load of nothing
# just want to test github actions


def return_greeting(
        name: str, greeting: str = 'Hi'):
    print(f"{greeting} {name}")


def return_even_numbers(nums: List[str]):
    
    evens = []
    for num in nums:
        r= num % 2

        if r ==0:
            evens.append(r)
    return evens
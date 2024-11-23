import random
import time
import os

def coin_flip():
    time.sleep(0.5)
    result = random.choice(['Heads', 'Tails'])
    print(f'   Result: {result}')

if __name__ == "__main__":
    coin_flip()

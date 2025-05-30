import string
import random
def status_generator(size=6,chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))
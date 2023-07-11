import random
import string
from model.group import Group


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data = [Group(name="", logo="", comment="")] + [
    Group(name=random_string("name", 10), logo=random_string("logo", 10), comment=random_string("comment1", 10))
    for i in range(5)
]

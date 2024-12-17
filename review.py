# Review 1

def add_to_list(value, my_list=[]):
    my_list.append(value)

    return my_list

# the [] cannot used as a default value, since [] is a mutable object.
# Everytime the fuction is called, the return value will share the same object.
# if we call res1 = add_to_list(1), res2 = add_to_list(2), the res1 is [1] and the res2 is [1, 2]
# Therefore, we should avoid setting the mutable object, list, as a default value.
# The fixed solution is below.

def add_to_list_fixed(value, my_list = None):
    if not my_list:
        my_list = list()
    my_list.append(value)
    return my_list


# Review 2

def format_greeting(name, age):
    return "Hello, my name is {name} and I am {age} years old."

# The name and age argument are not really formatted and used in the return statement when we call it,
# since it does not use f-str or str.format() method here. If we call the function and print returned
# value of format_greeting('Chen', 16), the 'Chen' and 16 will not be in the sentence.
# The fixed solution by using f-str is shown below

def format_greeting_fixed(name, age):
    return f"Hello, my name is {name} and I am {age} years old."

# Review 3

class Counter:
    count = 0

    def __init__(self):
        self.count += 1

    def get_count(self):
        return self.count

# There are two types of attributes here. One is Counter.count, a class attribute,
# defined outside the __init__ method. The other one is self.count, an instance attribute,
# is not initialized but share the same name as class attribute inside the __init__method.
# Everytime we create an instance of Counter class, the get_count() method will return 1.
# The incrementing behavior does not actually work. Thus, we can change self.count to Counter.count,
# incrementing the class attribute. And all instances of the class will share the same class attribute.
# Everytime a new instance is created, Counter.count is incremented by 1.
# The fixed solution is below.

class Counter_Fixed:
    count = 0

    def __init__(self):
        Counter.count += 1

    def get_count(self):
        return Counter.count


# Review 4

import threading


class SafeCounter:

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1


def worker(counter):
    for _ in range(1000):
        counter.increment()


counter = SafeCounter()

threads = []

for _ in range(10):
    t = threading.Thread(target=worker, args=(counter,))

    t.start()

    threads.append(t)

for t in threads:
    t.join()

# The shared variable self.count is not locked, and may cause
# multiple threads to change the self.count at the same time.
# If thread1 and thread2 both change self.count by adding 1.
# We may expect self.count becoming 2, but it actually may only
# increment by 1. Therefore, it will be better if the function
# used lock on self.count. The fixed solution is below.

class SafeCounter2:

    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            self.count += 1


def worker2(counter):
    for _ in range(1000):
        counter.increment()


counter2 = SafeCounter2()

threads = []

for _ in range(10):
    t = threading.Thread(target=worker2, args=(counter2,))

    t.start()

    threads.append(t)

for t in threads:
    t.join()

print("fixed count:" , counter2.count)


# Review 5

def count_occurrences(lst):
    counts = {}

    for item in lst:

        if item in counts:

            counts[item] = + 1

        else:

            counts[item] = 1

    return counts

# counts[item] =+ 1 is an incorrect expression. If the function wants to track the frequency
# of items in a list. The correct expression should be counts[item] += 1, which also means
# counts[item] = counts[item] + 1. The fixed solution is shown below.

def count_occurrences_fixed(lst):
    counts = {}

    for item in lst:

        if item in counts:

            counts[item] += 1

        else:

            counts[item] = 1

    return counts



if __name__ == "__main__":
    print(format_greeting_fixed('Chen', 16))
    c1 = Counter_Fixed()
    print(c1.get_count())
    c2 = Counter_Fixed()
    print(c2.get_count())
    print(count_occurrences_fixed([1, 2, 1, 3]))




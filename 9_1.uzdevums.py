import random


def random_generate(list):
    for i in range(random.randint(5,25)):
        n = random.randint(0,20)
        list.append(n)


def max_list_value(list1,list2):
    max_value = max(max(list1), max(list2))
    print(f"Maksimālā vērtība no abiem listiem ir {max_value}")


randomlist1 = []
randomlist2 = []
random_generate(randomlist1)
random_generate(randomlist2)

max_list_value(randomlist1,randomlist2)



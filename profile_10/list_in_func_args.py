def append_to(element, to=None):
    to = to or []
    to.append(element)
    return to


my_list = append_to(12)
print(my_list)

my_another_list = append_to(42)
print(my_another_list)

# LIST DATA TYPE PRACTICE
def create_list():
    return ['PlayStation','Xbox','Stream','iOS','Google Play']
def get_info(my_list):
    return tuple (my_list [0::3]),len(my_list)
def get_partial(my_list):
    return (my_list[1:4:1])
def get_last_three(my_list):
    return my_list[-1:-4:-1]
def double_list(my_list):
    first_element = my_list[1:1:1]
    return my_list + first_element
def amend(my_list):
    my_list[1]= 'None'
    my_list.append('Bye')
    return my_list
if __name__ == "__main__":
    test_list = create_list()
    print(test_list)
    print(get_info(test_list))
    print(get_partial(test_list))
    print(get_last_three(test_list))
    print(double_list(test_list))
    print(amend(test_list))

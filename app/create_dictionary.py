def create_dictionary(*args):
    new_dict = {}
    # write your code here
    for num, elem in enumerate(args):
        # print((elem))
        if isinstance(elem, list) or isinstance(elem, set) or isinstance(elem, dict):
            print(f"Cannot add {elem} to the dict!")
        else:
            print((elem))
            new_dict[elem] = num
    print(new_dict)

create_dictionary(3, [1, 2], 5)
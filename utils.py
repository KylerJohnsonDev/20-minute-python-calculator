def get_num_list_from_raw_input(raw_input):
    string_list = raw_input.split(",")
    num_list = []
    for i in string_list:
        # trim white space
        num_string = i.strip()
        num_list.append(int(num_string))
    return num_list
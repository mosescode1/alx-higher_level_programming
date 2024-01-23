def safe_print_list(my_list=[], x=0):
    listing = []
    i = 0
    try:
        for index, item in enumerate(my_list[:x]):
            i += 1
            listing.append(item)
    except IndexError:
        pass
    
    print("".join(map(str,listing)))
    return i

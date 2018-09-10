def get_even_list(l):
    for i in l:
        if i % 2 != 0:
            l.remove(i)
    return(l)
def PrettyLog(M : dict, l: str = ''):
    for key in M:
        val = M[key]
        val_type = type(val)
        # print(key, val_type)
        if type(val) == str or type(val) == int or type(val) == float:
            print(l+str(key), ' : ', val)
        elif type(val) == set or type(val) == list:
            print(l+str(key), f' : \n{l}\t', end='')
            print(*val, sep=f'\n{l}\t')
        elif type(val) == dict:
            print(l+str(key), f' : \n{l}\t', end='')
            PrettyLog(val, l+'\t')
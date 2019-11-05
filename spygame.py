def spy_game(arglist):
    '''
        SpyGame Function
    '''
    spystring = ''
    for item in arglist:
        if item == 0 or item == 7:
            spystring += str(item)
    print(spystring)
    return "007" in spystring

print(spy_game([1,7,4,0,0,2,5]))

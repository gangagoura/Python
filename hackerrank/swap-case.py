def swap_case(s):
    x = ""
    for let in s:
        if let.isupper() == True:
            x+=(let.lower())
        else:
            x+=(let.upper())
    return x
    

if __name__ == '__main__':

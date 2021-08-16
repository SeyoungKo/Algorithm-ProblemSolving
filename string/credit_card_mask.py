# Credit Card Mask

def maskify(cc):
    if len(cc) >= 4:
        masking_word = cc.replace(cc[:-4], len(cc[:-4]) *'#')
    else:
        masking_word = cc
    return masking_word

if __name__ == '__main__':
    print(maskify("Nananananananananananananananana Batman!"))

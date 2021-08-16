# Stop Spinning My Words!

def spin_words(sentence):
    words = sentence.split(' ')[:]
    for i, target in enumerate(words):
        if len(target) >= 5:
            words[i] = ''.join(target[::-1])

    return ' '.join(words)

def spin_words2(sentence):
    return ' '.join([word[::-1] if len(word) >= 5 else word for word in sentence.split(' ')])

if __name__ == '__main__':
    print(spin_words('Hey fellow warriors'))
    print(spin_words2('Welcome'))
# Vowel Count

def get_count(sentence):
    vowel = ['a', 'e', 'i', 'o', 'u']
    cnt = 0

    sentence_list = list(sentence)
    for word in sentence_list:
        if word in vowel:
            cnt += 1
    return cnt

if __name__ == '__main__':
    sentence = 'bcdfghjklmnpqrstvwxz y'
    print(get_count(sentence))
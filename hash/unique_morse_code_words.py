# Unique Morse Code Words (804)
from string import ascii_lowercase

class Solution:
    def uniqueMorseRepresentation(self, words):
        '''
        :param words: list
        :return: integer
        '''
        alpha_list = list(ascii_lowercase)
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alpha_morse = {alpha: morse[i] for i, alpha in enumerate(alpha_list)}
        morse_list = ['' for _ in range(len(words))]

        for idx, word in enumerate(words):
            for letter in word:
                morse_list[idx] += alpha_morse[letter]

        return len(set(morse_list))

if __name__ == '__main__':
    words = ["gin","zen","gig","msg"]

    s = Solution()
    print(s.uniqueMorseRepresentation(words))
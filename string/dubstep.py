# Dubstep
import re

class Solution:
    def song_decoder(self, song):
        '''
        :param song: str
        :return: str
        '''
        # (문자열)+ : 특정 문자열 패턴 n번 반복
        return re.sub(r'(WUB)+', ' ', song).strip()

if __name__ == '__main__':
    strs = 'WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB'
    s = Solution()
    print(s.song_decoder(strs)) 
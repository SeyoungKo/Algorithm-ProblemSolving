if __name__ == '__main__':

# 1. 주소는 lowercase + hypen x
# 2. 같은 이메일 사용자가 있으면 숫자 추가(2부터)
# 3. last_first@company.com 형식
# 4. s: ; 로 구분된 이름 각각
# 5. c: 회사의 이름 리스트

    s = 'John Doe; Peter Benjamin Parker; John Doe; Mary Jane Watson-Parker; John Doe; Peter Brian Parker'
    c = 'example'

    names = []
    names = s.split('; ')
    upper = [n.casefold() for n in names]

    # 이름 위치 앞뒤 변경 + _추가
    rev_name = [n.split(' ')[-1] + '_' + n.split(' ')[0] for n in upper]
    drop_duplicate = list(set(upper))
    print(upper)
    print(drop_duplicate)

    dup = []
    # 각 요소 카운팅
    for i, n in enumerate(rev_name):
        dup.append(rev_name.count(rev_name[i]))

    # 딕셔너리에 중복 요소만 담기
    dup_dict = {}
    for i in range(len(dup)):
        if dup[i] >= 2:
            dup_dict[rev_name[i]] = dup[i]
    print(dup_dict)

    tmp = {d : 1 for d in dup_dict}
    rev2_name = rev_name.copy()
    print(f'revname: {rev_name}')
    # 중복 이름에 숫자 추가
    for dup in dup_dict:
        for j in range(1, dup_dict[dup]):
            print(f'j:{j}')
            cnt = 2
            for i in range(len(rev_name)):
                if rev_name[i] in dup_dict:
                    rev2_name[i] = rev2_name[i] + str(tmp[rev_name[i]] + 1)
                    tmp[rev_name[i]] += 1
                else:
                    continue

    print(rev2_name)

    #회사 이메일 + 이름
    res = ''
    colon = '; '
    for i, n in enumerate(rev_name):
        res += names[i] + ' <'
        res += rev_name[i] + '@' + c.casefold() + '.com>'

        if i != len(rev_name) -1:
            res += colon
    print(res)
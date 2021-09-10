# Hash Table
hash_table = [0 for i in range(8)]

# Key값 정의
def get_key(data):
    return hash(data)

# Hash 함수 정의
def hash_function(key):
    return key % 8

# Hash Table에 값 저장
def save_data(data, value):
    hash_key = get_key(data)
    hash_addr = hash_function(get_key(data))

    # 해시 충돌 검사 - chaining 방법

    # 특정 해시 공간에 이미 값이 저장되어 있으면
    if hash_table[hash_addr] != 0:
        # 특정 해시 공간에 이미 값이 저장되어 있으면 몇개 저장되어 있는지 확인
        for idx_key in range(len(hash_table[hash_addr])):
            # 특정 해시 공간의 링크드리스트 값들을 순회하고 일치하는 key가 있으면 value에 값을 덮어쓴다
            if hash_table[hash_addr][idx_key][0] == hash_key:
                hash_table[hash_addr][idx_key][1] = value
                return
        # 저장하려는 특정 해시 공간의 링크드리스트에 일치하는 key값이 없으면 리스트에 key, value를 추가한다
        hash_table[hash_addr].append([idx_key, value])
    # 해시 공간에 값이 저장되어 있지 않으면
    else:
        # [hash_key, value] 형태로 저장
        hash_table[hash_addr] = [[hash_key, value]]

# Key로 값 읽기
def read_data(data):
    hash_key = get_key(data)
    hash_addr = hash_function(get_key(data))

    # Hash Table에 한개 이상 값이 저장되어 있을 경우
    if hash_table[hash_addr] != 0:
        # 링크드리스트로 되어 있는 특정 해시 주소의 값을 가져온다
        for idx_key in range(len(hash_table[hash_addr])):
            # 일치하는 주소가 있으면 value값을 가져온다
            if hash_table[hash_addr][idx_key][0] == hash_key:
                return hash_table[hash_addr][idx_key][1]
        # 조회되는 값이 없으면
        return None
    else:
        return None


if __name__ == '__main__':
    # save_data('Dave', '01011112222')
    # save_data('Andy', '01033334444')

    # 동일한 해시 공간에 저장되도록 테스트 (해시 충돌 테스트)
    save_data('Dd', '1201023010')
    save_data('Data', '3301023010')

    print(read_data('Dd'))
    print(read_data('Test'))
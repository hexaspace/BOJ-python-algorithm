import math
def solution(s):
    answer = 0
    s_len = len(s)
    min_len = s_len # 일단 원본 길이
    print(int(s_len/2))
    for slice_size in range(1, int(s_len/2)+1): # 전체 길이 절반까지가 슬라이스 최대 길이, 즉 2번 반복이 최대
        this_len = 0
        retry = s[0:slice_size]
        retry_num=1
        result_str = ""
        for i in range(1, math.floor(s_len/slice_size)):    # 자투리는 항상 반복 불가이므로, 그 직전까지 함
            this_slice = s[slice_size*i:slice_size*(i+1)]
            if(retry == this_slice):
                retry_num += 1
            else:
                if(retry_num == 1):
                    result_str += retry
                else:
                    result_str += str(retry_num)+retry  # 숫자 자리수를 계산하기보다, 일단 문자열로 합쳐놓기
                retry_num=1
                retry = this_slice
        # 마지막 누적된거 더하기
        if(retry_num == 1):
            result_str += retry
        else:
            result_str += str(retry_num)+retry
        # 나머지 문자열 더해야함
        this_len = len(result_str) + (s_len-slice_size*(i+1))  # 자투리 문자를 추가하기보다, 그냥 숫자로 계산하는게 더 빠를것같음
        if(min_len > this_len):
            min_len = this_len
    answer = min_len
    return answer
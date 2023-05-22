def solution(p):
    if p == '' :
        return ''
    answer = repeat(p)
    return answer

def is_correct(sent):   # 올바른인지 확인
    middle_line = 0
    for s in sent:
        if s == "(":
            middle_line += 1
        else:
            middle_line -= 1
        if middle_line < 0: #  )가 더 많아진 순간 이상해짐
            return False
    if middle_line != 0:
        return False    # 그럴리 없겠지만 균형이 아닐때
    return True
def is_ballance(sent):   # 균형인지 확인
    middle_line = 0
    for s in sent:
        if s == "(":
            middle_line += 1
        else:
            middle_line -= 1
    if middle_line != 0:
        return False    #균형이 아닐때
    return True
def cut_min_ballance(sent):   # 왼쪽을 최소 균형으로 자름
    middle_line = 0
    for i in range(len(sent)):
        if sent[i] == "(":
            middle_line += 1
        else:
            middle_line -= 1
        if middle_line == 0:    # 첫번째 균형이 맞았을때
            return sent[:i+1], sent[i+1:]
    return sent, ''    # 못찾으면 전체 길이 앞부분이 최소
def slice_and_reverse_u(sent):
    slice_sent = sent[1:len(sent)-1]
    reverse_sent = ""
    for s in slice_sent:
        if s == "(":
            reverse_sent += ")"
        else:
            reverse_sent += "("
    return reverse_sent


def repeat(sent):
    if sent == '':  # 1번
        return ''
    # 2번, uv로 분리
    u, v = cut_min_ballance(sent)
    if is_correct(u) == True:   # 3번
        return u + repeat(v)
    else:
        result_sent = "("
        result_sent += repeat(v)
        result_sent += ")"
        result_sent += slice_and_reverse_u(u)
        return result_sent
        
        

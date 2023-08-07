def cut_four(line_num, r, c):
    if line_num == 0:
        return 0
    line_mid = 2 ** (line_num-1)

    # (0,0), (0,1), (1,0), (1,1)
    r_index = 1
    c_index = 1
    if r < line_mid:
        r_index = 0
    if c < line_mid:
        c_index = 0

    four_index = r_index * 2 + c_index    # (0) -> (1) ->. (2) -> (3)
    before_me_sum = line_mid*line_mid * four_index
    return before_me_sum + cut_four(line_num-1, r - (r_index * line_mid), c - (c_index * line_mid))




if __name__ == "__main__":
    n, r, c = map(int, input().split())
    result = cut_four(n, r, c)
    print(result)
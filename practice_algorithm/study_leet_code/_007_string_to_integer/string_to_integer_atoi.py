# https://leetcode.com/problems/string-to-integer-atoi/
# 미완성

class Solution:
    def __init__(self, s: str):
        self.data = s

    def string_to_integer_atoi(self) -> int:
        s = self.data
        data = s.lstrip().split()[0]

        if data.isalpha():
            return 0

        is_float = data.split(".")[0]
        is_negative = data.startswith("-")

        if is_float.isdigit():
            data = int(is_float)

        if is_negative and data[1:].isdigit():
            data = -int(data[1:])

        data = int(data)

        max_num = 2 ** 31
        if -max_num > data:
            return -max_num
        elif max_num - 1 < data:
            return max_num - 1
        else:
            return data

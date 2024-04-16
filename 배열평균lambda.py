# 배열평균 구하기
from functools import reduce # python3의 경우 필수

def solution(numbers):
    return reduce(lambda x, y: x + y,numbers)/len(numbers)

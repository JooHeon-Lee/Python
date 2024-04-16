#01. 최빈값
def update_frequency(dictionary, num):
    if num in dictionary:
        dictionary[num] += 1
    else:
        dictionary[num] = 1
    return dictionary

def solution(array):
    frequency = {}
    if len(array) == 1:
        return array[0]
    else:
        for num in array:
            frequency = update_frequency(frequency, num)
        
        # 가장 빈도가 높은 요소 찾기
        max_frequency = max(frequency.values())
        max_elements = [key for key, value in frequency.items() if value == max_frequency]
        
        # 최빈값이 여러 개인지 확인
        if len(max_elements) > 1:
            return -1
        else:
            return max_elements[0]

def solution(array):    
    frequency = {}
    for num in array:

        frequency = update_frequency(frequency, num)
    
    max_frequency = max(frequency.values())
    max_elements = [key for key, value in frequency.items() if value == max_frequency]
    
    if len(max_elements) > 1:
        return -1
    else:
        return max_elements[0]

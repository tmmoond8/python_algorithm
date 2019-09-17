# 2744 대소문자 바꾸기

[2744번: 대소문자 바꾸기](https://www.acmicpc.net/problem/2744)

### Solution

    import sys
    
    def switch_case(str):
        originStr = list(str)
        switched = []
        for i in range(0, len(originStr)):
            if originStr[i].islower():
                switched.append(originStr[i].upper())
            else:
                switched.append(originStr[i].lower())
        return ''.join(switched)
    
    str = sys.stdin.readline().strip()
    
    print(switch_case(str))

## 문제

영어 소문자와 대문자로 이루어진 단어를 입력받은 뒤, 대문자는 소문자로, 소문자는 대문자로 바꾸어 출력하는 프로그램을 작성하시오.

## 입력

첫째 줄에 영어 소문자와 대문자로만 이루어진 단어가 주어진다. 단어의 길이는 최대 100이다.

## 출력

첫째 줄에 입력으로 주어진 단어에서 대문자는 소문자로, 소문자는 대문자로 바꾼 단어를 출력한다.

## 예제 입력 1

    WrongAnswer

## 예제 출력 1

    wRONGaNSWER
# 2966 찍기

[2966번: 찍기](https://www.acmicpc.net/problem/2966)

## Solution

---

    import sys
    
    def adrian(arr):
        SHEET = ['A', 'B', 'C']
        SHEET_SIZE = len(SHEET)
        sum = 0
        for i in range(len(arr)):
            if arr[i] == SHEET[i % SHEET_SIZE]:
                sum += 1
        return sum
    
    def bruno(arr):
        SHEET = ['B', 'A', 'B', 'C']
        SHEET_SIZE = len(SHEET)
        sum = 0
        for i in range(len(arr)):
            if arr[i] == SHEET[i % SHEET_SIZE]:
                sum += 1
        return sum
    
    def goran(arr):
        SHEET = ['C', 'C', 'A', 'A', 'B', 'B']
        SHEET_SIZE = len(SHEET)
        sum = 0
        for i in range(len(arr)):
            if arr[i] == SHEET[i % SHEET_SIZE]:
                sum += 1
        return sum
    
    N = int(sys.stdin.readline().strip())
    ARR = sys.stdin.readline().strip()
    
    # Adrian
    # Bruno
    # Goran
    
    A = adrian(ARR)
    B = bruno(ARR)
    G = goran(ARR)
    
    MAX = max(A, max(B, G))
    print(MAX)
    if MAX == A:
        print('Adrian')
    if MAX == B:
        print('Bruno')
    if MAX == G:
        print('Goran')

## 문제

상근이, 창영이, 현진이는 역사와 전통을 자랑하는 Sogang ACM-ICPC Team에 가입하려고 한다. 하지만, 가입하려고 하는 모든 지원자는 C언어 필기시험을 통과해야 한다. 이들은 C언어를 할 줄 모른다. 따라서, 필기시험을 모두 찍으려고 한다.

상근이는 A, B, C, A, B, C, A, B, C, A, B, C, ...와 같이 찍어야 통과할 수 있다고 생각한다.

하지만, 창영이는 B, A, B, C, B, A, B, C, B, A, B, C, ...와 같이 찍는 방법이 만점의 지름길이라고 생각한다.

마지막으로, 현진이는 상근이와 창영이를 비웃으면서 C, C, A, A, B, B, C, C, A, A, B, B, ...와 같이 찍어야 통과한다고 말했다.

필기시험의 정답이 주어졌을 때, 상근이, 창영이, 현진이 중에서 가장 많은 문제를 맞힌 사람이 누구인지 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 필기시험의 문제의 수 N이 주어진다. (1 ≤ N ≤ 100)

둘째 줄에는 시험의 정답이 주어진다.

## 출력

첫째 줄에 가장 많은 문제를 맞춘 사람이 몇 문제를 맞혔는지 출력한다.

다음 줄에는 가장 많은 문제를 맞힌 사람의 아이디를 출력한다. 상근이의 아이디는 Adrian, 창영이의 아이디는 Bruno, 현진이의 아이디는 Goran이다. 아이디 여러 개를 출력하는 경우에는 상근이, 창영이, 현진이 순서로 출력하고, 한 줄에 하나씩 출력한다.

## 예제 입력 1

    5
    BAACC

## 예제 출력 1

    3
    Bruno

## 예제 입력 2

    9
    AAAABBBBB

## 예제 출력 2

    4
    Adrian
    Bruno
    Goran
# 2355 시그마

[2355번: 시그마](https://www.acmicpc.net/problem/2355)

## Solution

---

    import sys, math
    
    A, B = map(int, sys.stdin.readline().strip().split(' '))
    
    
    def sum(a, b):
        return math.floor((a + b) * (b - a + 1) / 2)
    
    print(sum(min(A, B), max(A, B)))

## 문제

두 정수 A와 B가 주어졌을 때, 두 정수 사이에 있는 수의 합을 구하는 프로그램을 작성하시오. 사이에 있는 수들은 A와 B도 포함한다.

## 입력

첫째 줄에 두 정수 A, B가 주어진다. (-2,147,483,648 ≤ A, B ≤ 2,147,483,647)

## 출력

첫째 줄에 답을 출력한다. (-2,147,483,648 ≤ 답 ≤ 2,147,483,647)

## 예제 입력 1

    1 2

## 예제 출력 1

    3
# https://thebook.io/006935/part03/ch07/02-01/
# 7-3 다음과 같이 학생 번호와 이름이 리스트로 주어졌을 때 학생 번호를 입력하면 학생 번호에 해당하는 이름을 순차 탐색으로 찾아 돌려주는 함수를 만들어 보세요.
# 해당하는 학생 번호가 없으면 물음표(?)를 돌려줍니다. 참고로 학생 번호가 39번이면 “Justin”, 14번이면 “John”을 돌려줍니다.


def search_student(num):
    stu_no = [39, 14, 67, 105]
    stu_name = ["justin", "john", "mike", "summer"]
    for i in range(0, len(stu_no)):
        if(num == stu_no[i]):
            return stu_name[i]


print(search_student(14))
print(search_student(39))
print(search_student(67))

# 입출력 연습문제 p.185
# 1. 홀수, 짝수 판별 - 주어진 자연수가 홀수인지 짝수인지 판별하는 함수 작성
# def is_odd(num):
#   if num % 2 == 0:
#     print(True)
#   else:
#     print(False)
# is_odd(10) # True

# 2. 모든 입력의 평균값 구하기 - 입력으로 들어오는 모든 수의 평균값을 계싼하는 함수 작성
# def avg_numbers(*args):
#   result = 0
#   for i in args:
#     result += i
#   print(result / len(args))
# avg_numbers(1, 2)          # 1.5
# avg_numbers(1, 2, 3, 4, 5) # 3.0

# 3. 프로그램 오류 수정1 - 다음 프로그램의 오류를 수정하라
# input1 = input("첫 번째 숫자를 입력하세요: ")
# input2 = input("두 번째 숫자를 입력하세요: ")

# 원인 : input1 = 3, input2 = 6일 때, 결과값이 36이되는 이유는 input 함수가 입력값을 문자열로 저장하기 때문.
# total = input1 + input2
# print("두 수의 합은 %s입니다." % total)

# 해결 : 변수 input1, input2를 정수형으로 변환
# total = int(input1) + int(input2)
# print("두 수의 합은 %d입니다." % total)

# 4. 출력 결과가 다른 것은?
# - 1. print("you" "need" "python")
# - 2. print("you" + "need" + "python")
# - 3. print("you", "need", "python")
# - 4. print("".join(["you", "need", "python"]))

# 정답 3번. 쉼표는 띄어쓰기.

# 5. 프로그램 오류 수정2 - 다음 프로그램의 오류를 수정하라
# f1 = open("test.txt", 'w')
# f1.write("Life is too short")

# f2 = open("test.txt", 'r')
# print(f2.read())

# 원인 : f1 파일 객체를 닫지 않고 f2에서 다시 열려고 시도함.
# 해결 : f1 파일 쓰기 이후 파일 닫기.

# f1 = open("test.txt", 'w')
# f1.write("Life is too short")
# f1.close()

# f2 = open("test.txt", 'r')
# print(f2.read()) # Life is too short

# 6. 사용자 입력 저장하기 - 사용자의 입력을 파일에 저장하는 프로그램 작성. 재실행 시 새로 입력한 내용을 추가
# user_input = input("저장할 내용을 입력하세요: ")
# f = open("test.txt", 'a')
# f.write(user_input)
# f.write('\n')
# f.close()

# 7. 파일의 문자열 바꾸기 - 파일 내용 중 "java"를 "python"으로 변경
# f = open("test.txt", 'r')
# body = f.read()
# f.close()
# body = body.replace("java", "python")
# f = open("test.txt", "w")
# f.write(body)
# f.close()

# 8. 입력값을 모두 더해 출력하기 - 다음과 같이 실행할 때 입력값을 모두 더해 출력하는 스크립트 작성
# > python myargv.py 1 2 3 4 5 6 7 8 9 10
# import sys

# args = sys.argv[1:]
# total = 0
# for i in args:
#   total += int(i)
# print(total)
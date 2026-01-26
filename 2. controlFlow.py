# 제어문 연습 문제 p.149
# 1. 조건문의 참과 거짓 - 다음 코드의 결과갑은?
# a = "Life is too short, you need python"

# if "while" in a: print("while")
# elif "python" in a and "you" not in a: print("python")
# elif "shirt" not in a: print("shirt")
# elif "need" in a: print("need")
# else: print("none")
# -> "shirt"

# 2. 3의 배수의 합 구하기 - while 문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구하라
# num = 0
# result = 0
# while num <= 1000:
#   num += 1
#   if num % 3 == 0: result += num
# print(result) # 166833

# 3. 별 표시하기 - while 문을 사용하여 별을 표시하는 프로그램을 작성하라
# i = 0
# while i <= 5:
#   i += 1
#   if i > 5: break
#   print("*"*i)

# 4. 1부터 100까지 출력하기 - for 문을 사용해 1부터 100까지 출력
# for i in range(1, 101):
#   print(i)

# 5. 평균 점수 구하기 - for 문을 사용하여 평균 점수 구하기
# A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# total = 0
# for i in A:
#   total += i
# average = total / len(A)
# print(average) # 79

# 6. 리스트 컴프리헨션 사용하기 - 다음 코드를 리스트 컴프리헨션으로 표현하라
# numbers = [1, 2, 3, 4, 5]
# result = []
# for n in numbers:
#   if n % 2 == 1:
#     result.append(n * 2)
# [2, 6, 10]

# result = [n * 2 for n in numbers if n % 2 == 1]
# [2, 6, 10]
# print(result)
# hello.py
# print("Hello World")

# print("=" * 50)
# print("My Program")
# print("=" * 50)

# 자료형 연습 문제 116.p
# 1. 평균 점수 구하기
# score = {"korea" : 80, "english" : 75, "math" : 55}
# avg = (score["korea"] + score["english"] + score["math"]) / len(score)
# print(avg) # 70

# 2. 홀수, 짝수 판별하기
# if 13 % 2 == 0 :
#     print("짝수")
# else :
#     print("홀수")
# 홀수

# 3. 주민등록번호 나누기
# pin = "881120-1068234"
# yymmdd = pin[:6]
# num = pin[7:]
# print(yymmdd) # 881120
# print(num)    # 1068234

# 4. 주민등록번호 인덱싱 -> 성별을 나타내는 숫자 출력
# pin = "881120-1068234"
# print(pin[7]) # 1

# 5. 문자열 바꾸기 -> a#b#c#d로 변경
# a = "a:b:c:d"
# b = a.replace(":", "#")
# print(b) # a#b#c#d

# 6. 리스트 역순 정렬
# a = [1, 3, 5, 4, 2]
# a.sort()
# a.reverse()
# print(a) # [5, 4, 3, 2, 1]

# 7. 리스트를 문자열로 만들기
# a = ["Life", "is", "too", "short"]
# result = a[0] + " " + a[1] + " " + a[2] + " " + a[3]
# result = " ".join(a) # 정석 패턴
# print(result) # Life is too short

# 8. 튜플 더하기
# a = (1, 2, 3)
# a = a + (4,)
# print(a) # (1, 2, 3, 4)

# 9. 딕셔너리의 키
# 다음 딕셔너리에서 오류가 발생하는 경우를 고르고, 그 이유를 설명하라
# a = dict()

# a['name'] = 'python'
# a[('a',)] = 'python'
# a[[1]] = 'python'
# a[250] = 'python'

# 정답은 3번. 딕셔너리의 키값으로 리스트를 사용할 수 없기 때문.

# 10. 딕셔너리 값 추출하기
# 다음 딕셔너리에서 'B'에 해당하는 값 추출
# a = {'A': 90, 'B': 80, 'C': 70}
# result = a.pop('B')
# print(a)      # {'A': 90, 'C': 70}
# print(result) # 80

# 11. 리스트에서 중복 제거하기
# a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
# aSet = set(a)  # 리스트를 집합으로 변환
# b = list(aSet) # 집합을 다시 리스트로 변환
# print(b)       # [1, 2, 3, 4, 5]

# 12. 파이썬 변수
# 다음처럼 동일한 값에 여러 개의 변수를 선언했을 때, a의 두 번째 요소를 변경하면 b  값은 어떻게 될까? 그 이유도 설명하라
# a = b = [1, 2, 3]
# a[1] = 4
# print(b) # [1, 4, 3]
# 변수 a와 b는 동일한 객체를 참조하고 있으므로 a의 값을 변경하면 b도 같이 변경된다.
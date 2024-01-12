
# 조건문을 사용해서 컴퓨터와 가위바위보 게임 해보기

# 사용자의 입력을 input() 으로 받은 다음에
# 컴퓨터가 무엇을 낼지 random 모듈을 사용해서 임의로 정하기

# 사용자가 입력한 손(패)와 컴퓨터가 임의로 정한 손을 비교해서
# 누가 무엇을 내고 이겼는지, 누가 무엇을 내고 졌는지 출력
# ex) 나 : 가위 / 컴퓨터 : 바위
# 패배~~! ㅠㅠ

# 비교 연산자 활용
# print(1 == 1 & 2 == 2 )

import random
while True:

    user = input() # 입력이 무조건 문자열로 들어온다.

    print(f"사용자가 {user}를 냈습니다.")


    lst = ["가위", "바위", "보"]
    com = random.choice(lst)

    print(f"컴퓨터가 {com}를 냈습니다.")

    if user == com :
        print("비겼습니다!")
    elif user == "가위" and com == "바위" or user == "바위" and com == "보" or user == "보" and com == "가위":
        print("패배하였습니다ㅠㅠ")
    elif user == "가위" and com == "보" or user == "바위" and com == "가위" or user == "보" and com == "바위":
         print("승리하였습니다!")
    else:
        print("잘못된 입력입니다.")
# 계산기 프로그램

# 사용할 수 있는 연산자
# + - * /

# 두 개의 숫자를 입력받는다 => 두번째로 입력받은 숫자가 0이면 나눗셈x
# 그 뒤에 연산자를 입력받는다 => 나눗셈 연산자를 입력받았다면 => 두번째로 입력받은 숫자가 0이면 => 계산 X
# 결과를 출력

# 주의해야 할 점 : 나눗셈은 0으로 나누기가 불가능

# 한번 계산이 끝나고 또 계산을 이어 나갈 수 있도록 반복문을 사용해서 만들어 봅시다

# 두 숫자 모두 0을 입력받으면 종료

while True:
    print("======calculator======")
    num1 = int(input("n1 : "))
    num2 = int(input("n2 : "))
    if num1 == 0 and num2 ==0 :
        print("계산기를 종료합니다.")
        break
    cal = input("연산자 : ")
    t = 0

    if num2 == 0 and cal == "/":
        print("0으로는 나누기를 할 수 없습니다. 다른 연산자를 입력해주세요.")
        cal = input("연산자 : ")

    else :
        if cal == "+":
            t = num1 + num2
        elif cal == "-":
            t = num1 - num2
        elif cal == "*":
            t = num1 * num2
        elif cal == "/":
            t = num1 //num2
    print(f"정답은 {t}입니다!")
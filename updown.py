import random

target_num = random.randrange(1, 101)  # 1~100 사이의 랜덤 숫자 생성
get_num = 0  # 입력받을 값 초기화
count = 0  # 시도 횟수
count_list = []  # 각 게임마다 시도 횟수를 저장
print(target_num)
while (True):  # while 1: 무한루프

    while target_num != get_num:

        # Try-except를 통해 정수가 아닌 값을 입력받을 때 에러 메시지 출력
        try:
            get_num = int(input("숫자를 입력하세요: "))
        except ValueError:
            print("정수가 아닙니다.")

        if 1 <= get_num <= 100:

            count += 1  # 시도 횟수 +1

            if target_num > get_num:
                print("업")

            elif target_num < get_num:
                print("다운")

            else:
                print("정답입니다.")
                print(f'시도한 횟수: {count}')

        else:
            print("유효한 범위 내의 숫자를 입력하세요.")  # 추가 과제1

    count_list.append(count)  # 각 게임마다 시도 횟수를 저장
    max_count = max(count_list)  # 이전 플레이어의 최대 시도 횟수를 구함.

    retry = input("다시 하시겠습니까? (y/n): ")  # 추가 과제2
    if retry == 'y':
        target_num = random.randrange(1, 101)  # 새로운 target_num 생성
        print(target_num)
        get_num = 0  # get_num을 0으로 초기화하여 2번째 while문을 재가동
        print(f'이전 게임 플레이어 최고 시도 횟수: {max_count}')  # 추가 과제3
        count = 0  # 카운트 초기화
    elif retry == 'n':
        print("게임을 종료합니다.")
        break
    else:
        print("y 또는 n을 입력해주세요.")

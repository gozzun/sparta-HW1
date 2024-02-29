import random
win=0 #승
lose=0 #패
draw=0 #무승부
cpu='' #컴퓨터 초기화
retry='y' #2번째 while문을 처음으로 통과하게 해줌

while(True):

    while((retry=='y') or (retry=='Y')):
        
        player=input("가위, 바위, 보 중 하나를 선택하세요: ")

        if (player == '가위') or (player == '바위') or (player == '보'): #가위/바위/보를 받지 못하면 아래 while문 돌입 불가
            pass
        else: 
            print("유효한 입력이 아닙니다.") #가위/바위/보를 받을 때까지 유효 입력이 아니라는 문구 출력

        while((player == '가위') or (player == '바위') or (player == '보')): 

            random_num = random.randrange(1,4) #1~3까지 숫자 생성하여 각각 가위/바위/보 배정시켜줌.
        
            if random_num == 1:
                cpu='가위'
            elif random_num == 2:
                cpu='바위'
            elif random_num == 3:
                cpu='보'

            print(f'사용자: {player}, 컴퓨터: {cpu}')

            if (player=='가위' and cpu=='바위') or (player=='바위' and cpu=='보') or (player=='보' and cpu=='가위'): #컴퓨터 승
                lose += 1
                print("컴퓨터 승리!")
            elif (player=='바위' and cpu=='가위') or (player=='가위' and cpu=='보') or (player=='보' and cpu=='바위'): #플레이어 승
                win += 1
                print("사용자 승리!")
            elif player == cpu: #비김
                draw += 1
                print("비겼습니다.")

            player='' #플레이어 초기화하여 무한루프 탈출
            retry=''  #retry 초기화 시켜 2번째 while문 탈출
        
    retry = input("다시 하시겠습니까? (y/n): ") #1번째 while문에 포함되어 y/Y/n/N 중 입력이 없다면 올바른 입력을 받을때까지 출력

    if (retry == 'y') or (retry == 'Y'): #y/Y를 받으면 그냥 지나가서 다시 2번째 while문 돌입
        pass
    elif (retry == 'n') or (retry == 'N'): #추가 과제1,2,3
        print("게임을 종료합니다.")
        print(f'승: {win}, 패: {lose}, 무승부: {draw}')
        break    
    else: print("y/Y 또는 n/N을 입력해주세요.") #1번째 while문에 포함되어 y/Y/n/N 중 입력이 없다면 계속하여 반복 출력
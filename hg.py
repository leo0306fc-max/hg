import random

print("안녕하세요!")
print("여기는 할리갈리 게임 속 세상이에요.")


def hg():

    #사람_숫자=int(input("게임 인원을 정해주세요.2~4"))
    #바나나,사과,딸기,포도 숫자:1~5

    cards = ['바나나1','바나나2','바나나3','바나나4','바나나5','사과1','사과2','사과3','사과4','사과5','딸기1','딸기2','딸기3','딸기4','딸기5','포도1','포도2','포도3','포도4','포도5'] *3


    random.shuffle(cards)


    a = cards[:len(cards)/3]
    b = cards[len(cards)/3:len(cards)/3*2]
    c = cards[len(cards)/3*2:]

    a_card = ""
    b_card = ""
    c_card = ""

    turn =1
    
    while True:
        if turn % 3 == 1:
            print("a가 카드를 내려놓았습니다.")

            a_card = random.choice(a)
            
            print("a가 놓은 카드:", a_card)

            if a_card



while True:
    print("1. 게임속으로 들어간다. 2. 아직은..."  )

    할리갈리=input()

    if 할리갈리=='1' or 할리갈리=='1. 게임속으로 들어간다.' or 할리갈리=='게임속으로 들어간다.':
        hg()
    elif 할리갈리=='2' or 할리갈리=='2. 아직은...' or 할리갈리=='아직은...':
        print("나가 임마")
        break
    else :
        print("다시 입력하세요.")

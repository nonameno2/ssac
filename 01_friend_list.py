friends = []
select = 0

while select != 9:
    print("1. 친구 리스트 출력")
    print("2. 친구추가")
    print("3. 친구삭제")
    print("4. 이름변경")
    print("9. 종료")
    print()
    select = int(input("메뉴를 선택하세요: "))

    if select == 1:
        print("친구 리스트: ", friends)
        print()
    elif select == 2:
        add_name = input("추가할 이름을 입력하세요: ")
        friends.append(add_name)
    elif select == 3:
        del_name = input("삭제할 이름을 입력하세요: ")
        if del_name in friends:
            friends.remove(del_name)
        else:
            print("해당 이름이 존재하지 않습니다.")
            print()
    elif select == 4:
        old_name = input("변경할 이름을 입력하세요: ")
        if old_name in friends:
            index = friends.index(old_name)
            new_name = input("새로운 이름을 입력하세요: ")
        else:
            print("해당 이름이 존재하지 않습니다.")
            print()

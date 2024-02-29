import hashlib
import getpass

# ----- 클래스 정의 ------
class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print(f'이름: {self.name}')
        print(f'아이디: {self.username}')


class Post(Member):
    def __init__(self, title, content, author):
        super().__init__(title, content, author)
        self.title = title
        self.content = content
        self.author = author

# ------ 함수 정의 ------

# 1. 회원 추가 함수
# getpass와 hashlib을 이용하여 비밀번호를 해쉬화하여 저장하며 입력할 때 비밀번호가 보이지 않도록 하였음. 
def add_member():
    name = input("회원의 이름을 입력해주세요: ")
    username = input("회원의 아이디를 입력해주세요: ")
    password = getpass.getpass("회원의 비밀번호를 입력해주세요: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    member = Member(name, username, hashed_password)
    members.append([member.name, member.username, member.password])
    print("회원이 추가되었습니다.")

# 2. 게시글 추가 함수
def add_post():
    username = input("게시글을 작성할 회원의 아이디를 입력해주세요: ")
    for member in members:
        if member[1] == username:  # 입력한 아이디와 일치하는 회원을 찾음
            title = input("게시글의 제목을 입력해주세요: ")
            content = input("게시글의 내용을 입력해주세요: ")
            post = Post(title, content, username)
            posts.append([post.title, post.content, post.author])
            print("게시글이 추가되었습니다.")
            return
    print("해당 아이디의 회원이 존재하지 않습니다.")


# 3. 게시글 수정 함수
def edit_post():
    username = input("게시글을 작성한 회원의 아이디를 입력하세요: ")
    password = getpass.getpass("게시글을 작성한 회원의 비밀번호를 입력하세요: ")
    
    # 아이디로 작성한 게시글 찾기
    user_posts = [(i, post) for i, post in enumerate(posts, 1) if post[2] == username]
    
    if not user_posts:
        print("작성한 게시글이 없습니다.")
        return
    
    print("수정할 게시글 목록:")
    for i, post in user_posts:
        print(f"{i}. {post[0]}")
    
    # 수정할 게시글 선택
    selected_post_index = input("수정할 게시글의 번호를 입력하세요: ")
    try:
        selected_post_index = int(selected_post_index)
        if 1 <= selected_post_index <= len(user_posts):
            selected_post_index -= 1  # 리스트 인덱스로 변환
            selected_post = user_posts[selected_post_index][1]
            
            # 게시글 내용 출력
            print(f"\n게시글 내용: {selected_post[1]}")
            
            # 비밀번호 확인
            input_password = getpass.getpass("비밀번호를 입력하세요: ")
            if input_password == password:
                # 새로운 내용 입력
                new_content = input("새로운 내용을 입력하세요: ")
                posts[selected_post_index] = (selected_post[0], new_content, selected_post[2])
                print("게시글이 성공적으로 수정되었습니다.")
            else:
                print("비밀번호가 올바르지 않습니다.")
        else:
            print("올바른 번호를 입력하세요.")
    except ValueError:
        print("올바른 번호를 입력하세요.")


# 4. 게시글 삭제 함수
def delete_post():
    title = input("삭제할 게시글의 제목을 입력해주세요: ")
    matching_posts = []  # 입력한 제목과 일치하는 모든 게시글을 저장할 리스트
    for post in posts:
        if post[0] == title:  # 입력한 제목과 일치하는 게시글을 찾음
            matching_posts.append(post)
    
    if not matching_posts:  # 입력한 제목과 일치하는 게시글이 없는 경우
        print("해당 제목의 게시글이 존재하지 않습니다.")
        return
    
    print("입력한 제목과 일치하는 게시글을 찾았습니다. 삭제할 게시글을 선택해주세요:")
    for i, post in enumerate(matching_posts, start=1):
        print(f"{i}. 제목: {post[0]}, 작성자: {post[2]}")
    
    while True:
        choice = input("삭제할 게시글의 번호를 입력하세요 (취소: 0): ")
        if choice == "0":
            print("게시글 삭제를 취소합니다.")
            return
        elif choice.isdigit() and 0 < int(choice) <= len(matching_posts):
            chosen_post = matching_posts[int(choice) - 1]
            posts.remove(chosen_post)
            print("게시글이 삭제되었습니다.")
            return
        else:
            print("잘못된 입력입니다. 다시 입력해주세요.")


# 5. 특정 유저가 작성한 게시글을 출력하는 함수
def print_user_posts(username, posts):
    user_posts = []  
    for index, post in enumerate(posts, 1):  
        if post[2] == username:  
            user_posts.append((index, post[0]))  
    if user_posts:
        print(f"{username} 님이 작성한 게시글의 제목:")
        for index, title in user_posts:
            print(f"{index}. {title}")
        
        selected_post = input("확인할 게시글의 번호를 입력하세요 (취소: 'q'): ")
        if selected_post.lower() == "q":
            return
        try:
            selected_post_index = int(selected_post)
            if 1 <= selected_post_index <= len(user_posts):
                post_title = user_posts[selected_post_index - 1][1]
                for post in posts:
                    if post[0] == post_title:
                        print(f"{post_title}의 내용: {post[1]}")
                        return
        except ValueError:
            pass
        print("올바른 번호를 입력하세요.")
    else:
        print(f"{username} 님이 작성한 게시글이 없습니다.")


# 6. 특정 단어가 포함된 게시글을 출력하는 함수
def print_posts_with_keyword(keyword, posts):
    matching_posts = []  
    for post in posts:
        if keyword in post[1]:  
            matching_posts.append((post[0], post[2]))  
    if matching_posts:  
        print(f"'{keyword}'를 포함하는 게시글의 제목:")
        for i, (title, author) in enumerate(matching_posts, 1):
            print(f"{i}. {title} (작성자: {author})")
        
        selected_post = input("확인할 게시글의 번호를 입력하세요 (취소: 'q'): ")
        if selected_post.lower() == "q":
            return
        try:
            selected_post_index = int(selected_post)
            if 1 <= selected_post_index <= len(matching_posts):
                selected_post_title, selected_post_author = matching_posts[selected_post_index - 1]
                for post_title, content, author in posts:
                    if post_title == selected_post_title and author == selected_post_author:
                        print(f"{selected_post_title}의 내용: {content}")
                        return
        except ValueError:
            pass
        print("올바른 번호를 입력하세요.")
    else:
        print(f"'{keyword}'를 포함하는 게시글이 없습니다.")


# 7. 등록된 모든 회원의 이름을 출력하는 함수
def print_all_members():
    print("현재까지 등록된 모든 회원의 이름:")
    for member in members:
        print(member[0])


# 8. 회원 비밀번호 변경 함수
def change_password():
    username = input("비밀번호를 변경할 회원의 아이디를 입력하세요: ")
    name = input("비밀번호를 변경할 회원의 이름을 입력하세요: ")
    for member in members:
        if member[1] == username and member[0] == name:  # 입력한 아이디와 이름이 일치하는 회원을 찾음
            old_password = getpass.getpass("현재 비밀번호를 입력하세요: ")
            hashed_old_password = hashlib.sha256(old_password.encode()).hexdigest()
            if member[2] == hashed_old_password:  # 입력한 비밀번호와 저장된 해시화된 비밀번호가 일치하는지 확인
                new_password = getpass.getpass("새로운 비밀번호를 입력하세요: ")
                if old_password == new_password:  # 변경 전과 변경 후의 비밀번호가 같은지 확인
                    print("새로운 비밀번호는 이전과 동일합니다. 다른 비밀번호를 입력하세요.")
                    return
                hashed_new_password = hashlib.sha256(new_password.encode()).hexdigest()
                member[2] = hashed_new_password
                print("비밀번호가 성공적으로 변경되었습니다.")
                return
            else:
                print("비밀번호가 일치하지 않습니다.")
                return
    print("해당 아이디 또는 이름의 회원이 존재하지 않습니다.")


# 9. 회원 탈퇴 함수 
def remove_member():
    username = input("회원의 아이디를 입력하세요: ")
    name = input("회원의 이름을 입력하세요: ")
    password = getpass.getpass("회원의 비밀번호를 입력하세요: ")
    for member in members:
        if member[1] == username and member[0] == name:  # 입력한 아이디와 이름이 일치하는 회원을 찾음
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            if member[2] == hashed_password:  # 입력한 비밀번호와 저장된 해시화된 비밀번호가 일치하는지 확인
                confirmation = input("정말 탈퇴하시겠습니까? 탈퇴하시려면 '회원 탈퇴'를 입력해주세요. (n/N으로 취소): ")
                if confirmation.lower() == "회원 탈퇴":
                    # 해당 회원이 작성한 게시글 모두 삭제
                    for post in posts[:]:  # 리스트를 복사하여 순회하면서 삭제
                        if post[2] == username:
                            posts.remove(post)
                    members.remove(member)
                    print("회원이 성공적으로 탈퇴되었습니다.")
                    return
                elif confirmation.lower() == "n":
                    print("회원 탈퇴가 취소되었습니다.")
                    return
            else:
                print("비밀번호가 일치하지 않습니다.")
                return
    print("해당 아이디 또는 이름의 회원이 존재하지 않습니다.")

# ----- 코드 실행 ------

members = []
posts = []

while True:
    print("\n")
    print("<회원 관리 프로그램>")
    print("1. 회원 추가")
    print("2. 게시글 추가")
    print("3. 게시글 수정")
    print("4. 게시글 삭제")
    print("5. 특정 유저가 작성한 게시글 목록")
    print("6. 특정 단어가 포함된 게시글 목록")
    print("7. 현재까지 등록된 모든 회원의 이름 출력")
    print("8. 비밀번호 변경")
    print("9. 회원 탈퇴")
    print("0. 종료")
    print("\n")


    choice = input("메뉴를 선택하세요: ")

    if choice == "1":
        add_member()
    elif choice == "2":
        add_post()
    elif choice == "3":
        edit_post()
    elif choice == "4":
        delete_post()
    elif choice == "5":
        search_username = input("검색하고자 하는 유저의 아이디를 입력하세요: ")
        print_user_posts(search_username, posts)
    elif choice == "6":
        search_keyword = input("검색하고자 하는 특정 단어를 입력하세요: ")
        print_posts_with_keyword(search_keyword, posts)
    elif choice == "7":
        print_all_members()
    elif choice == "8":
        change_password()
    elif choice == "9":
        remove_member()
    elif choice == "0":
        print("프로그램이 종료됩니다.")
        break
    else:
        print("잘못된 입력입니다. 다시 입력해주세요.")

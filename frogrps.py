import random
import threading

class FrogRPS:
    def __init__(self):
        self.choices = ['가위', '바위', '보']
        self.frog_choices = ['바위', '보', '가위']
        self.user_choice = None

    def get_user_choice(self):
        self.user_choice = input("가위, 바위, 보 중에서 선택하세요 : ").strip().lower()
        if self.user_choice not in self.choices:
            print("잘못된 입력입니다. 다시 시도하세요.")
            self.get_user_choice()

    def timeout(self):
        print("\n시간이 초과되어 게임이 종료됩니다.")
        exit()

    def get_frog_choice(self):
        return random.choice(self.frog_choices)

    def determine_winner(self, user_choice, frog_choice):
        if user_choice == frog_choice:
            return "개굴"
        elif (user_choice == '가위' and frog_choice == '보') or \
             (user_choice == '바위' and frog_choice == '가위') or \
             (user_choice == '보' and frog_choice == '바위'):
            return "이겼다"
        else:
            return "졌다"
        

    def play_game(self):
        print("청개구리 가위, 바위, 보를 시작합니다.")
        while True:
            self.get_user_choice()
            user_choice = self.user_choice
            frog_choice = self.get_frog_choice()
            result = self.determine_winner(user_choice, frog_choice)
            timer = threading.Timer(3, self.timeout)
            timer.start()
            answer = input("상대는 ["+frog_choice+"]를 냈습니다. : ").strip().lower()
            timer.cancel()
            if answer == result:
                play_again = input("게임에 승리하셨습니다!\n게임을 새로 시작하려면 1, 종료하려면 2를 입력하세요.\n").strip().lower()
            else :
                play_again = input("게임에 패배하셨습니다!\n게임을 새로 시작하려면 1, 종료하려면 2를 입력하세요.\n").strip().lower()
            if play_again != '1':
                break

game = FrogRPS()
game.play_game()

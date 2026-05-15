import time
import sys

def print_slow(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

def get_choice(options):
    while True:
        print_slow("\n무엇을 하시겠습니까?")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        
        choice = input("선택: ")
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice)
        print("잘못된 입력입니다. 올바른 번호를 입력해주세요.")

def start_game():
    print_slow("=== 어두운 동굴 ===")
    print_slow("당신은 차갑고 축축한 동굴 입구에서 눈을 떴습니다.")
    print_slow("손에는 낡은 검 한 자루와 작은 횃불이 들려있습니다.")
    
    choice = get_choice(["동굴 안으로 조심스럽게 들어간다", "무서우니 밖으로 도망친다"])
    
    if choice == 1:
        cave_entrance()
    else:
        print_slow("당신은 모험을 포기하고 따뜻한 집으로 돌아갔습니다.")
        print_slow("=== 게임 오버 ===")

def cave_entrance():
    print_slow("\n--- 동굴 갈림길 ---")
    print_slow("안으로 들어가자 두 개의 갈림길이 나타났습니다.")
    print_slow("왼쪽 길에서는 으스스한 짐승의 울음소리가, 오른쪽 길에서는 희미한 빛이 새어 나옵니다.")
    
    choice = get_choice(["소리가 나는 왼쪽 길로 간다", "빛이 나는 오른쪽 길로 간다"])
    
    if choice == 1:
        monster_room()
    else:
        treasure_room()

def monster_room():
    print_slow("\n--- 짐승의 둥지 ---")
    print_slow("앗! 거대한 동굴 늑대가 잠에서 깨어났습니다!")
    
    choice = get_choice(["검을 뽑아 들고 싸운다", "뒤도 돌아보지 않고 도망친다"])
    
    if choice == 1:
        print_slow("당신은 용감하게 검을 휘둘러 늑대를 물리쳤습니다!")
        print_slow("늑대의 뒤편에 숨겨져 있던 통로를 발견했습니다.")
        treasure_room()
    else:
        print_slow("당신은 허둥지둥 도망치다 돌부리에 걸려 넘어졌습니다.")
        print_slow("결국 늑대의 먹이가 되고 말았습니다...")
        print_slow("=== 게임 오버 ===")

def treasure_room():
    print_slow("\n--- 보물의 방 ---")
    print_slow("눈부신 황금과 보석이 가득 쌓여있는 방을 발견했습니다!")
    print_slow("전설로만 듣던 고대 왕국의 숨겨진 보물입니다.")
    print_slow("축하합니다! 당신은 엄청난 부자가 되어 무사히 동굴을 빠져나왔습니다!")
    print_slow("=== 게임 클리어! ===")

if __name__ == "__main__":
    start_game()

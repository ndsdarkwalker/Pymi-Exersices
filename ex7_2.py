#!/usr/bin/env python3

'''
Viết 1 một trò chơi đánh đối kháng giữa 2 nhân vật. Mỗi nhân vật có tên (str),
máu (int), vũ khí.
Vũ khí chọn random khi tạo nhân vật, có damage (int) bằng lượng máu trừ đi
khi đánh trúng.

Cho 2 nhân vật lần lượt đánh nhau, print kết quả mỗi lượt đánh, print người
thắng.

'''

class Fighter():
    def __init__(self, name, HP):
        pass

    def __str__(self):
        pass

    # Add more if needed


class Weapon():
    pass


class Fighter():
    def __init__(self, name, HP, weapon):
        self.name = name
        self.HP = HP
        self.weapon = weapon
    def __str__(self):
        return "This is: {}, HP: {}, Weapon: {}".format(self.name, self.HP, self.weapon)
    def attack(self, opponent):
        print('{} attack {}'.format(self.name, opponent.name))
        opponent.HP = opponent.HP - self.weapon.damage

    # Add more if needed

import random

class Weapon():
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
    def __str__(self):
        return ('{}: {}'.format(self.name, self.damage))

weapons = [
    Weapon('Có súng đây nè', 100),
    Weapon('Đấm phát chết luôn', 200),
    Weapon('Khóa mõm cực mạnh', 500),
    Weapon('Nam Huỳnh Đạo', 50)]


def solve(player1, player2):
    '''Trả về tuple tên người thắng cuộc và lượng máu còn lại (int)'''
    result = ('', 0)

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    player1 = Fighter('Tran Dan', 1500, random.choice(weapons))
    player2 = Fighter('Hai Vu', 2000, random.choice(weapons))
    print(player1, 'VS', player2)
    
    while player1.HP > 0 and player2.HP > 0:
                
        player1.attack(player2)
        print(player1, '*' * 5, player2)
        player2.attack(player1)
        print(player1, '*' * 5, player2)
    
    if player1.HP > 0:
        result = (player1, player1.HP)
    else:
        result = (player2, player2.HP)    

    return result


def main():
    # Thay đổi các dòng sau cho phù hợp
    player1 = Fighter('Tran Dan', 500, random.choice(weapons))
    player2 = Fighter('Hai Vu', 800, random.choice(weapons))
    print(solve(player1, player2))


if __name__ == "__main__":
    main()

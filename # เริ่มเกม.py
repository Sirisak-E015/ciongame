# เริ่มเกม
coins = 5  # จำนวนเหรียญเริ่มต้น
print(f"เหรียญเริ่มต้น: {coins}")

while coins > 0:
    # ตาผู้เล่นคนที่ 1
    player1_move = int(input("ผู้เล่น 1: คุณต้องการหยิบเหรียญ (1 หรือ 2 เหรียญ): "))
    while player1_move not in [1, 2] or player1_move > coins:
        print("การเลือกไม่ถูกต้อง! กรุณาเลือก 1 หรือ 2 และอย่าหยิบเกินจำนวนเหรียญที่เหลืออยู่")
        player1_move = int(input("ผู้เล่น 1: คุณต้องการหยิบเหรียญ (1 หรือ 2 เหรียญ): "))
    coins -= player1_move
    print(f"ผู้เล่น 1 หยิบ: {player1_move} เหรียญ, เหรียญที่เหลือ: {coins}")
    if coins == 0:
        print("ผู้เล่น 1 แพ้! ผู้เล่น 2 ชนะ!")
        break

    # ตาผู้เล่นคนที่ 2
    player2_move = int(input("ผู้เล่น 2: คุณต้องการหยิบเหรียญ (1 หรือ 2 เหรียญ): "))
    while player2_move not in [1, 2] or player2_move > coins:
        print("การเลือกไม่ถูกต้อง! กรุณาเลือก 1 หรือ 2 และอย่าหยิบเกินจำนวนเหรียญที่เหลืออยู่")
        player2_move = int(input("ผู้เล่น 2: คุณต้องการหยิบเหรียญ (1 หรือ 2 เหรียญ): "))
    coins -= player2_move
    print(f"ผู้เล่น 2 หยิบ: {player2_move} เหรียญ, เหรียญที่เหลือ: {coins}")
    if coins == 0:
        print("ผู้เล่น 2 แพ้! ผู้เล่น 1 ชนะ!")
        break
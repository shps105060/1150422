# 初始化柳丁的狀態
shiny_points = 0
weight = 10
playing = True

print("🍊 --- 柳丁樹上的奇幻冒險 --- 🍊")
player_name = input("輸入這顆傳奇柳丁的名字：")

# While 迴圈：控制遊戲主進程
while playing:
    print(f"\n【{player_name} 的目前狀態：閃耀值 {shiny_points} / 體重 {weight}kg】")
    print("1. 瘋狂行光合作用 (增加閃耀值)")
    print("2. 瘋狂吸收水分 (增加體重)")
    print("3. 詢問樹下路過的老婆婆")
    print("4. 檢查是否可以啟程 (觸發結局)")
    
    choice = input("請選擇你的行動 (1-4)：")

    # If, Elif, Else：判斷行為
    if choice == "1":
        # For 迴圈：模擬吸收能量的過程
        print("太陽光灑在你身上...")
        for i in range(1, 4):
            print(f"吸收光波中... 第 {i} 階強化！")
            shiny_points += 2
            
    elif choice == "2":
        # For 迴圈：增加體重的動態感
        print("樹根努力吸水中...")
        for drop in ["滴答", "呼嚕", "咕嘟"]:
            print(f"喝水聲：{drop}...")
            weight += 3
            
    elif choice == "3":
        print("婆婆抬頭看了看你。")
        if shiny_points > 10:
            print("婆婆說：『這顆柳丁好亮，一定是外星來的！』")
        elif weight > 20:
            print("婆婆說：『這柳丁太重了，樹枝快斷了吧？』")
        else:
            print("婆婆說：『就是顆普通的柳丁，沒什麼特別。』")
            
    elif choice == "4":
        # 結局判定邏輯
        print("\n--- 命運的時刻到了 ---")
        
        # 結局 1：超進化結局
        if shiny_points >= 15:
            print(f"因為你太過耀眼，{player_name} 直接飛向宇宙，變成了一顆恆星。")
            print("【結局 A：太陽的接班人】")
            playing = False # 跳出 While 迴圈，遊戲結束
            
        # 結局 2：物理性結局
        elif weight >= 25:
            print(f"因為你太重了，樹枝「喀嚓」一聲斷裂。")
            print(f"{player_name} 掉進了土裡，長出了另一棵充滿邏輯的樹。")
            print("【結局 B：回歸大地的重力使者】")
            playing = False
            
        # 結局 3：平凡結局
        else:
            print("你還不夠強大，樹枝緊緊抓著你不放。")
            retry = input("你要繼續努力嗎？(y/n)：")
            if retry.lower() != 'y':
                print(f"{player_name} 最後在樹上曬成了柳丁乾。")
                print("【結局 C：乾燥的靈魂】")
                playing = False
    
    else:
        print("無效的指令！你在樹上亂跳，差點驚動了路過的烏鴉。")

print("\n--- 遊戲結束，感謝遊玩 ---")
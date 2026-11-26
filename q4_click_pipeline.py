# 第 4 題：清理素材點擊資料並產生排名
student_id = input("請輸入完整學號：").strip().upper()
tail = student_id[-3:]
a = int(student_id[-3])
b = int(student_id[-2])
c = int(student_id[-1])
s = a + b + c


def select_clicks(raw_clicks, min_clicks=10):
    """清理文字點擊數並回傳全部數字與達門檻數字。"""
    cleaned_text = map(lambda item: item.strip(), raw_clicks)
    non_empty_text = filter(None, cleaned_text)
    numbers = list(map(int, non_empty_text))
    qualified = list(filter(lambda number: number >= min_clicks, numbers))
    return numbers, qualified


raw_clicks = [str(10 + a), "0", "", " " + str(5 + b) + " ",
              "   ", str(15 + c), str(5 + b)]
min_clicks = 5 + b
numbers, qualified = select_clicks(raw_clicks, min_clicks=min_clicks)

print(f"學號：{student_id}")
print(f"點擊門檻：{min_clicks}")
print(f"清理結果：{numbers}")
print(f"合格結果：{qualified}")
print(f"合格筆數：{len(qualified)}")
print(f"合格合計：{sum(qualified)}")

ranked_clicks = sorted(qualified, reverse=True)
for rank, clicks in enumerate(ranked_clicks, start=1):
    print(f"第{rank}名：{clicks}次")

# 同一份原始資料改用 100 點門檻，確認沒有符合項目
high_threshold_numbers, high_threshold_qualified = select_clicks(raw_clicks, min_clicks=100)
print(f"門檻100合格結果：{high_threshold_qualified}")
print(f"門檻100合格筆數：{len(high_threshold_qualified)}")
print(f"門檻100合格合計：{sum(high_threshold_qualified)}")
if len(high_threshold_qualified) == 0:
    print("無符合門檻的素材")

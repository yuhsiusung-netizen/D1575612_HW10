# 第 1 題：製作自己的廣告成效報表
student_id = input("請輸入完整學號：").strip().upper()
tail = student_id[-3:]
a = int(student_id[-3])
b = int(student_id[-2])
c = int(student_id[-1])
s = a + b + c


def ad_report(impressions, clicks, target=3.0):
    """回傳 CTR 百分比與是否達標；零曝光時 CTR 為 None。"""
    if impressions == 0:
        return (None, False)
    ctr = clicks / impressions * 100
    passed = ctr >= target
    return (ctr, passed)


ads = [
    ("搜尋廣告", 1000 + 100 * a, 30 + 5 * b),
    ("社群廣告", 1200 + 100 * b, 24 + 4 * c),
    ("影音廣告", 0, 0),
]
target = 2.5 + 0.1 * c

print(f"學號：{student_id}")
print(f"CTR門檻：{target:.2f}%")
passed_count = 0
for name, impressions, clicks in ads:
    ctr, passed = ad_report(impressions, clicks, target=target)
    if passed:
        passed_count += 1
    ctr_text = "無曝光資料" if ctr is None else f"{ctr:.2f}%"
    print(f"{name}：曝光={impressions}，點擊={clicks}，CTR={ctr_text}，達標={passed}")
print(f"達標廣告數：{passed_count}")

# 驗證預設門檻與零點擊情況
print(f"預設門檻測試：{ad_report(1000, 30)}")
print(f"零點擊測試：{ad_report(1000, 0)}")

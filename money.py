def actual(yun, zhi, we, gu, zhao, bai, hua, others, expect, date):
    money = (yun + zhi + we + gu) - (zhao + bai + hua + others)
    print(f"{date}: expect: {expect}, reality: {money}, 差距： {money - expect}")


actual(63902, 114205, 0, 1205, (51000 - 41207), 3127, 142, 3, 165253, "2024-10-28")

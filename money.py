def actual(yun, zhi, we, gu, zhao, bai, hua, others, expect, date):
    """

    @param yun: 云闪付
    @param zhi: 支付宝
    @param we: 微信
    @param gu: 股票
    @param zhao: 招商8号, 注销电话400-888-5555
    @param bai: 白条18号
    @param hua: 花呗20号
    @param others: 美团22号, 饿了么、携程、抖音已关闭
    @param expect: 钱迹余额
    @param date: 日期
    @return:
    """
    money = (yun + zhi + we + gu) - (zhao + bai + hua + others)
    print(f"{date}: expect: {expect}, reality: {money}, 差距： {money - expect}")


actual(63902, 114205, 0, 1205, (51000 - 41207), 3127, 142, 3, 165253, "2024-10-28")
actual(24574, 114441, 0, 31313, (51000 + 80000 - 48953 - 79380), 3127, 244, 3, 163563, "2024-11-08")

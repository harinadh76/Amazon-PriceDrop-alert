from bs4 import BeautifulSoup
# import lxml
import requests
import smtplib


MY_EMAIL = ""
MY_PASSWORD = ""

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_1_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/9.8.4 Safari/602.8.7",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
URL = "https://www.amazon.com/Audio-Technica-ATH-G1WL-Premium-Wireless-Headset/dp/B07TXMG5J1/ref=sr_1_1_sspa?keywords=gaming%2Bheadsets&pd_rd_r=2d792e47-bf1a-486b-9c00-3829f0a60299&pd_rd_w=fhnYi&pd_rd_wg=PTR6x&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=7JSEBF47S8QPP4QKEY3D&qid=1668927707&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
response = requests.get(URL, headers=header)

yc = response.text

soup = BeautifulSoup(yc, "html.parser")

# print(yc)
prices = soup.find(name="span", class_="a-price-whole")
# for price in prices:
title = soup.find(name="span", class_="a-size-large product-title-word-break")
print(title.getText())
price = prices.getText()
# print(price)
final_price_list = price.split('.')

final_price = int(final_price_list[0])
print(final_price)


Buying_price = 200

if final_price <= Buying_price:
    message = f"{title} price is {final_price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Amazon Price Drop Alert!!!\n\n\n {message}\n{URL}")

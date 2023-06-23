from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

product_url = "https://www.amazon.com/Corsair-Mechanical-Swappable-Keyswitches-Double-Shot/dp/B0B4SW81GW/ref=sr_1_2_sspa?keywords=gaming%2Bkeyboard&pd_rd_r=e07a2caa-cf7a-4de5-975f-f7c5570c2aa3&pd_rd_w=ZtKd4&pd_rd_wg=FMMTl&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=Z6JJKEZM3CF9EDQQEXR9&qid=1675158760&sr=8-2-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyREhDNzBTREo4WDgxJmVuY3J5cHRlZElkPUEwMzgyMTI0M0kzRDhaRlpTN0ExUSZlbmNyeXB0ZWRBZElkPUEwNDQzOTM2MVVPTTBIQzhIREJGTyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1"
headers ={
    "Accept-Language":"en-US,en;q=0.9",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}
response = requests.get(product_url, headers= headers)
soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())
price = soup.find(class_ = "a-offscreen").getText()
# price_float = float(price.split("$")[1])
# print(price_float)
price_float = 99


title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 100
MAIL_from = "s.shashwatjain@gmail.com"
MAIL_to = "shashwat.jn@gmail.com"
YOUR_PASSWORD = "mftfqzkgbkhlxgtx"

if price_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(MAIL_from, YOUR_PASSWORD)
        connection.sendmail(
            from_addr= MAIL_from,
            to_addrs= MAIL_to,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{product_url}"
        )
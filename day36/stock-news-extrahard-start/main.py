import requests
import datetime as dt

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "PXL3D1VP92FGDPX5"
NEWS_API_KEY = "8558f4d51207491a8743e4b66ed8dbfd"
# Would do this with export to env if I could.
STOCK_PARAMETERS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "interval": "60min",
    "apikey": STOCK_API_KEY,
}
TODAY_DATE = dt.datetime.now().today().date()
NEWS_PARAMETERS = {
    "q": COMPANY_NAME,
    "from": TODAY_DATE,
    "to": TODAY_DATE,
    "sortBy": "popularity",
    "apiKey": NEWS_API_KEY,
}

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(url="https://www.alphavantage.co/query", params=STOCK_PARAMETERS)
response.raise_for_status()
data = response.json()

closes = []
for day in range(21, 23):
    close = data["Time Series (Daily)"][f"2021-01-{day}"]["4. close"]
    closes.append(close)

if closes[1] > closes[0]:
    print("Get News")
else:
    print("Do not get news")
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
response = requests.get("https://newsapi.org/v2/everything", NEWS_PARAMETERS)
response.raise_for_status()
data = response.json()
print(data['articles'][0]['description'])
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


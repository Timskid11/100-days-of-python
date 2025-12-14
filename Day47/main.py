import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv

load_dotenv()
SMTP_ADDRESS = "timilehinoyinlola3@gmail.com"
SMTP_PASSWORD = 'uplurzxzxvdfpwbd'
EMAIL_ADDRESS = "timilehinoyinlola86@gmail.com"

print(EMAIL_ADDRESS)
print(SMTP_ADDRESS)
print(SMTP_PASSWORD)

URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
header = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
    "Accept-Language":
        "en-US,en;q=0.9,af;q=0.8,de;q=0.7"
    ,
}



try:
    response = requests.get(URL, headers=header)
    response.raise_for_status()

except requests.RequestException as e:
    print("Failed to fetch URL:", e)
    exit(1)

soup = BeautifulSoup(response.text, "html.parser")

try:
    price_whole = soup.find("span", class_="a-price-whole").text
    price_fraction = soup.find("span", class_="a-price-fraction").text
    print(price_whole, price_fraction)
    price_str = price_whole + price_fraction
    price = float(price_str)
    print(price)
except AttributeError:
    print("Failed to parse price from the page. Check the HTML structure.")
    exit(1)
except ValueError:
    print("Price is not a valid number.")
    exit(1)

print(f"Current price: ${price}")

# -----------------------------
# Send email if price is below threshold
# -----------------------------
PRICE_THRESHOLD = 100  # USD

if price < PRICE_THRESHOLD:
    try:
        smtp = smtplib.SMTP("smtp.office365.com", 587, timeout=10)
        smtp.starttls()
        smtp.login(SMTP_ADDRESS, SMTP_PASSWORD)
        subject = "PRICE ALERT: Instant Pot"
        body = f"The price of the Instant Pot has dropped to ${price}!\nCheck it here: {URL}"
        message = f"Subject: {subject}\n\n{body}"
        smtp.sendmail(SMTP_ADDRESS, EMAIL_ADDRESS, message)
        smtp.quit()
        print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError:
        print("SMTP login failed! Make sure you're using an App Password if required.")
    except smtplib.SMTPServerDisconnected:
        print("Connection closed by local software. Check firewall/antivirus.")
    except Exception as e:
        print("Failed to send email:", e)
else:
    print("Price is above threshold. No email sent.")
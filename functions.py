import urllib.parse


def encode(message):
    encoded_message = urllib.parse.quote(message)
    return encoded_message


def build_url(api_key, phone_number, message):
    url = "https://api.callmebot.com/whatsapp.php?phone=" + str(phone_number) + "&text=" + message + "&apikey=" + str(api_key)
    return url

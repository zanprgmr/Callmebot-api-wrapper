from requests import get
# Must install the requests library
# pip install requests
import functions
# File where all the functions are allocated


def send_message(api_key, phone_number, message):
    encoded_message = functions.encode(message)  # Uses urllib to encode from utf to urlencoded
    url = functions.build_url(api_key, phone_number, encoded_message)  # Uses credentials  to create a callmebot url
    get(url)  # Uses requests lib to open the callmebot url


def send_content_of_file(api_key, phone_number, file_dir):
    f = open(file_dir, "r")
    message = f.read()
    send_message(api_key, phone_number, message)
    f.close()


## Setup
First, you need the Request library, use :

    pip install requests
    
  
to install it!
Then you need the api key of callmebot, for more info click [HERE](https://www.callmebot.com/blog/free-api-whatsapp-messages/)

## Usage
Sending a whatsapp message

    from callmebot import send_message
    
    api_key = "Your callmebot api key"
    phone_number = "The phone number asociated with callmebot"
    message = "Your message"
	
	send_message(api_key, phone_number, message)

Sending the content of a text file
		
    
    from callmebot import send_message
    api_key = "Your callmebot api key"
    phone_number = "The phone number asociated with callmebot"
    dir= "Text file directory"
	
	send_content_of_file(api_key, phone_number, dir)



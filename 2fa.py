from twilio.rest import Client
import random
random_number1 = random.randint(0,9)
random_number2 = random.randint(0,18475)
random_num = random_number1*random_number2
str_random_num = str(random_num)

print("Choose any one of them,for SMS ""1"" or for Whatsapp ""2""\n1. SMS\n2. Whatsapp")
Whatsapp_or_SMS = int(input("Choose your number : "))

phone1 = int(input ("Your phone number please : "))
phone2 = str(phone1)

account_sid = "AC079b757bdb8517514534898b142ea8c1" 
auth_token = "aa5ee5ee8070ddcefa9ad584a81b9174"
client = Client(account_sid, auth_token) 

if Whatsapp_or_SMS == 1 :
 
  message = client.messages.create(  
                                messaging_service_sid="MG536cabc61faa6ced308016a65b047913", 
                                body="Your code for verification is - " + str_random_num, 
                                to="+91" + phone2
                                  )
elif Whatsapp_or_SMS == 2 :
  message = client.messages.create(  
                                from_="whatsapp:+14155238886",  
                                body="Your verification code is " + str_random_num,
                                to="whatsapp:+91" + phone2
                                  )

code1 = int(input("Your code : "))
code2 = str(code1)

if code2 == str_random_num:
  print("Verification completed")
else :
  print("Verfication not completed yet")

from twilio.rest import Client
import random

# Twilio account SID and auth token
account_sid = 'AC7d694e808cae9ed9153f82603069c3c8'
auth_token = 'e2170410a42ba086e0c3d659d79eee9e'

# Twilio phone number
twilio_number = '+13612735532'

# Get recipient's phone number from user
recipient_number = input('Enter the recipient\'s phone number:  ')

# Generate a random 6-digit OTP
otp = str(random.randint(100000, 999999))

# Create a Twilio client
client = Client(account_sid, auth_token)

try:
    # Send OTP via SMS
    message = client.messages.create(
        body='Your OTP is: ' + otp,
        from_=twilio_number,
        to=recipient_number
    )
    print('OTP sent successfully!')

    # Prompt the user to enter the OTP
    user_otp = input('Enter the OTP received: ')

    # Verify OTP
    if user_otp == otp:
        print('OTP verified successfully!')
    else:
        print('OTP verification failed!')
except Exception as e:
    print('An error occurred:', str(e))
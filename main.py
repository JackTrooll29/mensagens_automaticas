from twilio.rest import Client

account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

while True:
    msg = input('Digite a sua Mensagem: ')

    message = client.messages.create(
        to="+55",
        from_="",
        body=f'{msg}'
    )

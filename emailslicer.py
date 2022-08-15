email=input('Enter your email:').strip()
username=email[:email.index('@')]
domain=email[email.index('@')+1:]
print('Your Username is '+ username + ' and your domain is ' + domain)
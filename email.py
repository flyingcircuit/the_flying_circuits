def emailvalidator():
    email = input('Please type your email here:')
    if (len(email) > 15 and email.count('@') == 1 and email.find('.gov.uk') != -1):
        print ('Thank you for your email')
    else:
        print ('Sorry this is not a valid input') 
        emailvalidator()

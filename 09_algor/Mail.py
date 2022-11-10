email_list = ()
def is_email(mail):
    for e in email_list:
        if mail == e:
            print("Found")
            return True
    print("Not Found")
    return False


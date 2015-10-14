a = raw_input("BDECLA\n")


def error_check(test):
    try:
        tested = int(test)
        return tested
    except:
        print "Please enter a valid number"
        exit()
    
error_check(a)

print a
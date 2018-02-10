def encryption(j):
    outcome = ""

    for i in j:
	
        x = ord(i)

        if x >= ord('a') and x <= ord('z'):
            if x > ord('m'):
                x = x - 13
            else:
                x = x + 13
        elif x >= ord('A') and x <= ord('Z'):
            if x > ord('M'):
                x = x - 13
            else:
                x = x + 13
				
        outcome = outcome + chr(x)
    return outcome
PHRASE=raw_input("WRITE A PHRASE: ")
print encryption(PHRASE)

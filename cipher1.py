# cipher program - fun stuff you can do with CS1015F so far
# Daniel Kruyt
# 12/03/2015

print("Welcome to the cipher program.")

quit = False

while not quit:
    print("What would you like to do?\n1 - Caeser cipher\n2 - Vigenere cipher\n3 - Diffie-Hellman key exchange\n4 - Quit")
    c = int(input("Choice: "))
    if c == 1:
        print("The Caeser cipher is a simple cipher where each letter is replaced by the letter 'n' places ahead of it. For instance, when n=2, a -> c, b -> d, c -> e, z -> b.")
        key = int(input("Enter the key. An integer in the range [0,26): "))                
        if key > 25 or key < 0: 
            print("Key is invalid. The key must be an integer from 0 to 25, inclusive.")
        else:
            ptxt = input("Enter the plaintext (your message) in lower-case: ")
            ctxt = ""
            if ptxt.lower() != ptxt:
                print("Your message appears to contain upper-case characters. Converting to lower-case.")
                ptxt = ptxt.lower()
            found_nonlatin = False
            for char in ptxt:
                if ord(char) < ord('a') or ord(char) > ord('z'):
                    print("Found non-latin character in your message. You may only enter characters that are lower-case members of the latin alphabet.")
                    found_nonlatin = True
            if not found_nonlatin:
                for char in ptxt:
                    o = ( ord(char) - ord('a') + key ) % 26 + ord('a')
                    ctxt += chr(o)
                print("The ciphertext (encrypted message) is:",ctxt)
    elif c == 2:
        print("The Vigenere cipher shifts the letters around, like the Caeser cipher, but uses multiple shifting values. For instance, it can take 'lemon' as the key, then the message 'attackatdawn' is shifted by 'lemonlemonle', where each letter corresponds to a shift from 0 to 25")
        key = input("Input Key ( lower-case latin alphabet only ): ")
        if key.lower() != key:
            print("Your key appears to contain upper-case characters. Converting to lower-case.")
            key = key.lower()
        found_nonlatin = False
        for char in key:
            if ord(char) < ord('a') or ord(char) > ord('z'):
                print("Found non-latin character in your message. You may only enter characters that are lower-case members of the latin alphabet.")
                found_nonlatin = True
        if not found_nonlatin:
            ptxt = input("Enter the plaintext (your message): ")
            found_nonlatin = False
            for char in ptxt:
                if ord(char) < ord('a') or ord(char) > ord('z'):
                    print("Found non-latin character in your message. You may only enter characters that are lower-case members of the latin alphabet.")
                    found_nonlatin = True
            if not found_nonlatin:
                ctxt = ""
                for i in range(len(ptxt)):
                    o = ((  (ord(ptxt[i]) - ord('a')) + (ord(key[i % len(key)]  ) - ord('a'))) % 26) + ord('a')
                    ctxt += chr(o)
                print("The ciphertext (encrypted message) is:",ctxt)
    elif c == 3:
        print()
        #            
    elif c == 4:
        quit = True
    else:
        print("Your input is invalid. Please enter the number of the operation you wish to perform.")
print("Thanks for using the cipher program! Hope to see you again soon!")
print("For help using this program please email no-reply@googlegroups.com")

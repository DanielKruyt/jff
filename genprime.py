# generate the nth prime
# daniel kruyt
# 13/03/2015

print("This program will generate the nth prime.")
n = int(input("Enter n: "))
print("Generating nth prime... (this might take a while)")
pstr = "2-" # a string of all the primes seperated by - characters
cp = 0 # the current prime being inspected, in integer format
cps = "" # string representing current prime being checked in the prime string
pc = 1
m = 2
i = 0
found_nth_prime = False
if n == 1:
    print("The nth prime is 2")
else:
    while not found_nth_prime:
        while i < len(pstr) and not found_nth_prime:
            if pstr[i] != "-":
                cps += pstr[i] # append the character to the string form of currently-inspected prime
            else: # we just hit a -, which means we have the next prime to test m against
                cp = int(cps) # get the prime as an integer
                cps = "" # set the current prime string to the empty string
                if (m % cp) == 0: # if the number who's primality we are checking is divisible by the current prime
                    # failed prime test, increase m and search thru pstr again
                    m += 1
                    i = -1
                else: # m isnt divisible by cp
                    if i == (len(pstr)-1): # we've tried all the primes in pstr
                        # we just found a new prime!
                        pstr += (str(m)+"-") # append our newly found prime to the prime string
                        pc += 1 # increment prime counter
                        if pc == n: # if this is the nth prime
                            print("The nth prime is",m)
                            i = len(pstr)
                            found_nth_prime = True
            i += 1 # move index to next character



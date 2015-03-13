# generate the nth prime
# daniel kruyt
# 13/03/2015

n = int(input("Enter n: "))
print("Generating nth prime... (this might take a while)")
pstr = "2-"
cp = 0
cns = ""
m = 2
pc = 1
i = 0
not_found_nth_prime = False
while not_found_nth_prime:
    while i != len(pstr):
        if pstr[i] != "-":
            cns += pstr[i]            
        else:
            cp = int(cns)
            cns = ""
            if i == (len(pstr)-1):
                if (m % cn) == 0:
                    i = 0
                    m += 1
                else: # PRIME IS FOUND :D
                    pstr += str(m) + "-"
                    pc += 1
                    if pc == n:
                        print("The nth prime is",cp)
                        not_found_nth_prime = False
                    m += 1
                    i = 0
                
        i += 1
            
        
    

from random import randint

print("\n")

alice_heads = 0
bobs_heads = 0

bob_won = 0

n = [5, 10, 50, 100]
trials = 1000
coinflip = 0

#Fair coin, p = 0.5
print("P = 0.5")
for rounds in n:
    for i in range(trials):
        alice_heads = bob_heads = 0
        for k in range(2*rounds+1):
            if randint(0,1) == 0: bob_heads +=1
        for k in range(2*rounds):
            if randint(0,1) == 0: alice_heads += 1
        
        if bob_heads > alice_heads: bob_won += 1
    
    fraction = str(bob_won) + "/" + str(trials)
    decimal = str(bob_won / trials)
    print("Relative Frequency for n = " + str(rounds) + ": {:>5}".format(fraction) + " ,{:>5}".format(decimal))
    bob_won = bob_heads = alice_heads = 0

#Fair coin, p = 0.2
print("P = 0.3")
for rounds in n:
    for i in range(trials):
        alice_heads = bob_heads = 0
        for k in range(2*rounds+1):
            if randint(0,1) == 0: bob_heads +=1
        for k in range(2*rounds):
            if randint(0,1) == 0: alice_heads += 1
        
        if bob_heads > alice_heads: bob_won += 1
    
    fraction = str(bob_won) + "/" + str(trials)
    decimal = str(bob_won / trials)
    print("Relative Frequency for n = " + str(rounds) + ": {:>5}".format(fraction) + " ,{:>5}".format(decimal))
    bob_won = bob_heads = alice_heads = 0

    #Fair coin, p = 0.3
print("P = 0.3")
for rounds in n:
    for i in range(trials):
        alice_heads = bob_heads = 0
        for k in range(2*rounds+1):
            if randint(0,1) == 0: bob_heads +=1
        for k in range(2*rounds):
            if randint(0,1) == 0: alice_heads += 1
        
        if bob_heads > alice_heads: bob_won += 1
    
    fraction = str(bob_won) + "/" + str(trials)
    decimal = str(bob_won / trials)
    print("Relative Frequency for n = " + str(rounds) + ": {:>5}".format(fraction) + " ,{:>5}".format(decimal))
    bob_won = bob_heads = alice_heads = 0

    #Fair coin, p = 0.4
print("P = 0.4")
for rounds in n:
    for i in range(trials):
        alice_heads = bob_heads = 0
        for k in range(2*rounds+1):
            if randint(0,1) == 0: bob_heads +=1
        for k in range(2*rounds):
            if randint(0,1) == 0: alice_heads += 1
        
        if bob_heads > alice_heads: bob_won += 1
    
    fraction = str(bob_won) + "/" + str(trials)
    decimal = str(bob_won / trials)
    print("Relative Frequency for n = " + str(rounds) + ": {:>5}".format(fraction) + " ,{:>5}".format(decimal))
    bob_won = bob_heads = alice_heads = 0

#Fair coin, p = 0.6
print("P = 0.6")
for rounds in n:
    for i in range(trials):
        alice_heads = bob_heads = 0
        for k in range(2*rounds+1):
            if randint(0,1) == 0: bob_heads +=1
        for k in range(2*rounds):
            if randint(0,1) == 0: alice_heads += 1
        
        if bob_heads > alice_heads: bob_won += 1
    
    fraction = str(bob_won) + "/" + str(trials)
    decimal = str(bob_won / trials)
    print("Relative Frequency for n = " + str(rounds) + ": {:>5}".format(fraction) + " ,{:>5}".format(decimal))
    bob_won = bob_heads = alice_heads = 0

#Fair coin, p = 0.7
print("P = 0.7")
for rounds in n:
    for i in range(trials):
        alice_heads = bob_heads = 0
        for k in range(2*rounds+1):
            if randint(0,1) == 0: bob_heads +=1
        for k in range(2*rounds):
            if randint(0,1) == 0: alice_heads += 1
        
        if bob_heads > alice_heads: bob_won += 1
    
    fraction = str(bob_won) + "/" + str(trials)
    decimal = str(bob_won / trials)
    print("Relative Frequency for n = " + str(rounds) + ": {:>5}".format(fraction) + " ,{:>5}".format(decimal))
    bob_won = bob_heads = alice_heads = 0

#Fair coin, p = 0.8
print("P = 0.8")
for rounds in n:
    for i in range(trials):
        alice_heads = bob_heads = 0
        for k in range(2*rounds+1):
            if randint(0,1) == 0: bob_heads +=1
        for k in range(2*rounds):
            if randint(0,1) == 0: alice_heads += 1
        
        if bob_heads > alice_heads: bob_won += 1
    
    fraction = str(bob_won) + "/" + str(trials)
    decimal = str(bob_won / trials)
    print("Relative Frequency for n = " + str(rounds) + ": {:>5}".format(fraction) + " ,{:>5}".format(decimal))
    bob_won = bob_heads = alice_heads = 0
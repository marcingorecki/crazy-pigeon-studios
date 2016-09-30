import random

assfacedanswers=0
levelcount=1
wowyouranidiot=0
shouldgetnewnumbers=1

print "Welcome to pigeon school"
print
for a in range (1,6):
    for b in range (1,6):
        print "%s + %s = %s"  % (a, b, a+b)
    print
    print ""


while wowyouranidiot<3:
    if shouldgetnewnumbers==1:
        a = random.randint(0,10*levelcount)
        b = random.randint(0,20*levelcount)
    print "you are %s on failure level %s"  % (wowyouranidiot,levelcount)
    print "%s + %s = ?"  % (a,b)
    
    c = raw_input ()
    cnumber = int(c)
    if cnumber == a+b:
        print "Oh you got it right ok, Next sum."
        wowyouranidiot=wowyouranidiot+1
        shouldgetnewnumbers=1
    else:
        print "Try again."
        wowyouranidiot=wowyouranidiot-1
        shouldgetnewnumbers=0
        assfacedanswers=assfacedanswers+1
        if assfacedanswers==3:
            levelcount=levelcount+1
            assfacedanswers=0
    
print "Yey you passed the first year of pigeon school."

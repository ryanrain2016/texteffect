COLOR={'black':30,'red':31,'green':32,'yellow':33,'blue':34,'purple':35,'deepgreen':36,'white':37}

for k,w in COLOR.items():
    globals()[k]=(lambda k:lambda x: '\33[%sm%s\33[0m'%(COLOR[k],str(x)) if not str(x).endswith('\n') else '\33[%sm%s\33[0m\n'%(COLOR[k],str(x).strip()))(k)
    globals()[k+'background']=(lambda k:lambda x: '\33[%sm%s\33[0m'%(COLOR[k]+10,str(x)) if not str(x).endswith('\n') else '\33[%sm%s\33[0m\n'%(COLOR[k]+10,str(x).strip()))(k)
    
    #globals()[k+'onblack']=(lambda k:lambda x: '\33[%sm%s\33[0m'%(COLOR[k]+60,str(x)) if not str(x).endswith('\n') else '\33[%sm%s\33[0m\n'%(COLOR[k]+60,str(x).strip()))(k)

for k,w in COLOR.items():
    for k1, w1 in COLOR.items():
        globals()["%son%s"%(k, k1)] = (lambda k, k1: lambda x: "\033[%s;%sm%s\033[0m"%(COLOR[k1]+10, COLOR[k], str(s).strip())+("\n" if str(s).endswith('\n') else ''))(k, k1)
        
def highlight(s):
    return '\33[1m%s\33[0m'%str(s)

def underline(s):
    return '\33[4m%s\33[0m'%str(s)

def blink(s):
    return '\33[5m%s\33[0m'%str(s)

def reversedisplay(s):
    return '\33[7m%s\33[0m'%str(s)

def blank(s):
    return '\33[8m%s\33[0m'%str(s)

def diy(s,n):
    return '\33[%dm%s\33[0m'%(n,str(s))

if __name__=='__main__':
    s='this is a test !!'
    print(reversedisplay(highlight(underline(blink(bluebackground(green(s)))))))
    s=('key','value')
    print(redonred(s))
    print(blink(s))

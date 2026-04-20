#nan vayasu vangi adai vagai padhuthuven 
#kulanthai,teenager,periyavanga,unc or aunt,boomer,ultra boomer
def catogarise_age():
    vayasu = int(input('un vayasai sollu:'))
    if vayasu <= 12 :
        print('ne oru kulandai')
    elif vayasu <= 19 :
        print('ne oru teenager')
    elif vayasu <= 40 :
        print('neenga oru adult')
    elif vayasu <= 65 :
        print('neenga oru boomer')
    else :
        print('neenga oru ultra boomer')
#
print('welcome to the vayasu vakaipadhutal app')
choice = 'y'
while choice == 'y':
    catogarise_age ()
    choice = input('do you want countine(y/n)?')
#
print('nandri for using the vakaipathuthal app')
    

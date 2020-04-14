import sys
def moon_weight():
    print('Please enter your current Earth weight')
    earth_weight = int(sys.stdin.readline())
    print('Please enter the amount your weight might increase each year')
    weightyear = float(sys.stdin.readline())
    print('Please enter the number of years')
    year = int(sys.stdin.readline())
    moon_multiplier = 0.165
    for x in range(0, year):
        moon_weight = (earth_weight+(weightyear*x))*moon_multiplier 
        print('year %s = %s' % (x, moon_weight) )
    
moon_weight()

def moon_weight(earth_weight, weightyear, year):
    moon_multiplier = 0.165
    for x in range(0, year):
        moon_weight = (earth_weight+(weightyear*x))*moon_multiplier 
        print('year %s = %s' % (x, moon_weight) )
    
moon_weight(30,1, 5)

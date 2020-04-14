def moon_weight(earth_weight, weightyear):
    moon_multiplier = 0.165
    for year in range(0,16):
        moon_weight = (earth_weight+(weightyear*year))*moon_multiplier 
        print('year %s = %s' % (year, moon_weight) )
    

def earthweightcal(earth_weight):
    moon_multiplier = 0.165
    for year in range(0,16):
        moon_weight = (earth_weight + year) * moon_multiplier 
        print('year %s = %s' % (year, moon_weight))
    

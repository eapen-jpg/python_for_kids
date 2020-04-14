import pickle
favourites = ['fortnite', 'football','futsal', 'rocket league', 'pes 2020', 'fifa 18']
save_file = open('favourites.dat', 'wb')
pickle.dump(favourites, save_file)
save_file.close()
load_file = open('favourites.dat', 'rb')
loaded_favourites = pickle.load(load_file)
load_file.close()
loaded_favourites

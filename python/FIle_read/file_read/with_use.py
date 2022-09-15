import pickle

with open("profile.pickle","rb") as profile_file:
    print(pickle.load(profile_file))#with close 필요없음
    
    
    
    
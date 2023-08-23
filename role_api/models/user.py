from pymongo import MongoClient


client=MongoClient('mongodb://localhost:27017')
db=client['Api']




def verify_user(username,password):
    user=db['user']
    print(username)
    valid_user=user.find_one({'name':username,'password':password})
    print(valid_user)
    if valid_user:
        return valid_user
    else:
        return "Invalid username or password"

def final_data(username):
    user=db['data']
    datas=user.find()
    set=[]
    for i in datas:
        set.append(i)
    return set
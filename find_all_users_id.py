from read_data import read_data
from pprint import pprint
def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    arr=[]
    for i in range(len(data["messages"])):
        try:
            arr.append(data["messages"][i]["actor_id"])
        except:
            arr.append(data["messages"][i]["from_id"])

    return arr
 
if __name__=="__main__":
    data=read_data('data/result.json')
    pprint(find_all_users_id(data))
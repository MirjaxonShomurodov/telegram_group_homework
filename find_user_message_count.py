from read_data import read_data
from find_all_users_id import find_all_users_id
from pprint import pprint
def find_user_message_count(data: dict, users_id: str)->dict:
    """
    This function will find the user's message count.
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
        user_id (list): User id of the user
    Returns:
        dict: Number of messages of the users
    """
    arr=[]
    for i in range(len(data["messages"])):
            arr.append(data["messages"][i]["text"])

    return len(arr)


if __name__=="__main__":
    data=read_data('data/result.json')
    pprint(find_user_message_count(data))


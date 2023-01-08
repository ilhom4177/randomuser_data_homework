import get_data

def get_gender_users(data:dict) -> list:
    """
    Take the gender of the users and return the list.
    
    The list items are as follows:
        If the user is male: {"Male":1}
        If the user is female: {"Female":0}
    
    Args:
        data(dict): data
    Returns:
        list: users get gender list
    """
    a=[]
    for i in data["results"] :
        if i['gender']=='male' :
            a.append({"Male":1})
        else :
            a.append({"Female":0})
    return a
import get_data

def get_email(data:dict) -> list:
    """
    Take the email of the users and return the list.

    Args:
        data(dict): data
    Returns:
        list: users email
    """
    a=[]
    for i in data["results"] :
        a.append(i['email'])
    return a
print(get_email(get_data.get_data("randomuser_data.json")))
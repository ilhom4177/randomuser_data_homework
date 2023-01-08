from webbrowser import get
import get_data

def get_count_users(data:dict) -> int:
    """
    You are given dictionary. Find the number of users.

    Args:
        data(dict): data
    Returns:
        int: number of users
    """
    y=0
    for k in data["results"] :
        y+=1
    return y
print(get_count_users(get_data.get_data("randomuser_data.json")))
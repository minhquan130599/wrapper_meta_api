import random
import string

def get_nested_value(data, path):
    try:
        keys = path.split('.') 
        try:
            for key in keys:
                if isinstance(data, list):
                    key = int(key)  
                data = data[key]
            return data
        except (KeyError, IndexError, TypeError):
            return None
    except Exception as e:
        print(f"Error getting nested value: {str(e)}")
        return None
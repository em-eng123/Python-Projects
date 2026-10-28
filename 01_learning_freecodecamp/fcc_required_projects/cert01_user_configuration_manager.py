# -------------------------------------------------------------
# CERTIFICATION PROJECT: 01 - Build a User Configuration Manager
# NOTES: Designing a core data management module implementing key manipulation, validation safeguards, and string mutation.
# -------------------------------------------------------------

# USER STORIES TO FULFILL:
# 1. Define four core management functions: add_setting, update_setting, delete_setting, and view_settings.
# 2. add_setting(settings, key, value): 
#    - Lowercase the key string before processing.
#    - Add the key-value pair to the dictionary if it doesn't already exist.
# 3. update_setting(settings, key, value):
#    - Lowercase the key string before processing.
#    - Update the value if the key exists; otherwise, return an error string ("Setting not found!").
# 4. delete_setting(settings, key):
#    - Lowercase the key string before processing.
#    - Remove the key-value pair if it exists; otherwise, return an error string ("Setting not found!").
# 5. view_settings(settings):
#    - Return "No settings available." if the dictionary is completely empty.
#    - Otherwise, build and return a formatted string displaying each key with its first letter capitalized (key.capitalize()) and its mapped value.

# -------------------------------------------------------------

def add_setting(add_dict, add_pair):
    key, value = add_pair
    lwr_key=key.lower()
    lwr_value=value.lower()

    if lwr_key in add_dict:
        return f"Setting '{lwr_key}' already exists! Cannot add a new setting with this name."
    add_dict.update({lwr_key:lwr_value})
    return f"Setting '{lwr_key}' added with value '{lwr_value}' successfully!"

def update_setting(upd_dict, upd_pair):
    key, value = upd_pair
    lwr_key=key.lower()
    lwr_value=value.lower()

    if lwr_key in upd_dict:
        upd_dict.update({lwr_key:lwr_value})
        return f"Setting '{lwr_key}' updated to '{lwr_value}' successfully!"
    else:
        return f"Setting '{lwr_key}' does not exist! Cannot update a non-existing setting."
    
def delete_setting(del_dict, del_key):
    lwr_key=del_key.lower()

    if lwr_key in del_dict:
        del del_dict[lwr_key]
        return f"Setting '{lwr_key}' deleted successfully!"
    return "Setting not found!"

def view_settings(view_dict):
    if not view_dict:
        return "No settings available."
    
    view = "Current User Settings:\n"
    settings = [f"{key.capitalize()}: {value}" for key, value in view_dict.items()]
    return view + "\n".join(settings) + "\n"

test_settings = {
    'theme': 'dark',
    'language': 'english',
    'notifications': 'enabled'
}
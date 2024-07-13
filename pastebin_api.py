'''
Library for interacting with the PasteBin API
https://pastebin.com/doc_api
'''
import requests


PASTEBIN_API_POST_URL = 'https://pastebin.com/api/api_post.phpc'
API_DEV_KEY = 'XDCiUTERnlvgvnZBagDYJIJY-zOodEGT'

def post_new_paste(title, body_text, expiration='N', listed=True):
    """Posts a new paste to PasteBin

    Args:
        title (str): Paste title
        body_text (str): Paste body text
        expiration (str): Expiration date of paste (N = never, 10M = minutes, 1H, 1D, 1W, 2W, 1M, 6M, 1Y)
        listed (bool): Whether paste is publicly listed (True) or not (False) 
    
    Returns:
        str: URL of new paste, if successful. Otherwise None.
    """    

# Construct the Pastebin API request parameters  
post_params = {
    'api_dev_key' : API_DEV_KEY,
    'api_option' : 'paste',
    'api_paste_code': body_text,
    'api_paste_name': title,
    'api_paste_private' : 0 if listed else 1,
    'api_paste_expire_date' : expiration
}

# request a new Pastebin 
resp_msg= requests.post(PASTEBIN_API_POST_URL, data=post_params)
    
    
# check if the paste was created successfully
if  resp_msg.status_code == requests.codes.ok:
     print("Success!")
     return f'http://pastebin.com/{resp_msg.text}'
else:
     print("Failure in creating paste")
     print(f'Response code: {resp_msg.status_code} - {resp_msg.reason}')
     return None


import sys
import poki_api
import pastebin_api

pastebin_api_post_url = ('XDCiUTERnlvgvnZBagDYJIJY-zOodEGT')

def main ():
    poke_name = get_poke_name()
    poke_info = poki_api.get_pokemon_info(poke_name)
    if poke_info is None:
        paste_url = pastebin_api.post_new_paste(poke_info['name'], poke_info['description'])
        if paste_url:
                print(f'Paste URL: {paste_url}')
        else:
             print("Failed to create paste.")
    else:
        print(f"Failed to get info for {poke_name}.")






    

    
    





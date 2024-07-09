### student name: Dennis Dam ###    
#### school: Fleming College ###
#### course: Computer security and investigations #### 

import sys 
import poke_api
import pastebin_api

pastebin_api_post_url = ('XDCiUTERnlvgvnZBagDYJIJY-zOodEGT')


def main():
    poke_name = get_pokemon_name()
    poke_info = poke_api.get_pokemon_info(poke_name)
    if poke_info is not None:
        paste_url = pastebin_api.create_paste(poke_info)
        paste_title, paste_body = get_paste_data(poke_info)
        print(paste_url)


def  get_pokemmon_name():
    if len(sys.argv) < 2:
        print("Error")
        sys.exit(1)
    return sys. argv[1]

def get_paste_data(pokemon_info):
    return poke_info['name'], poke_info['description']
    name = pokemon_info ['name']. capitalize()
    abilities = [ability['ability']['name'] for ability in pokemon_info['abilities']]
    paste_title = f"{name}'s Ability"
    paste_body = '/n '.join(abilities)
    return (paste_title, paste_body)


###funtion to be written as a group ####
print("Posting new paste to ...", end=' ')

#message body parameters
post_parameters = { 'api_dev_key' : API_DEV_KEY,
                    'api_option' : 'paste'
                    'api_paste_code' : body_text,
                    'api_paste_name' : tittle,
                    'api_paste_private' : 0 if listed else 1,
                    'api_paste_expire_date' : expiration }

#make the post request for pastebin 
resp_msg = request.post(pastebin_api_post_url, data=post_params)


#check if the post was successful
if resp_msg.tatus_code == request.code.ok:
       print ("success")

else:
    print("failure in creating paste")
    print(f'response code: (resp_msg. status.code)' {resp_msg.reason}))
return resp_msg.text
                




if __name__ == '__main__':

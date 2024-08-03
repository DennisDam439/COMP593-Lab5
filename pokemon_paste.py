""" 
Description: 
  Creates a new PasteBin paste that contains a list of abilities 
  for a specified Pokemon

Usage:
  python pokemon_paste.py poke_name

Parameters:
  poke_name = Pokemon name
"""
import sys
import poke_api
import pastebin_api

def main():
    poke_name = get_pokemon_name()
    poke_info = poke_api.get_pokemon_info(poke_name)
    if poke_info is not None:
        paste_title, paste_body = get_paste_data(poke_info)
        paste_url = pastebin_api.post_new_paste(paste_title, paste_body, '1M')
        print(paste_url)

def get_pokemon_name():
    """Gets the name of the Pokemon specified as a command line parameter.
    Aborts script execution if no command line parameter was provided.

    Returns:
        str: Pokemon name
    """
# TODO: Function body
    if len(sys.argv) >= 2:    
        return sys.argv[1]
    else:
     print("Error: Pokemon name is not provided.")
     sys.exit("aborted script execution")

def get_paste_title_body(pokemon_info):

    """Builds the title and body text for a PasteBin paste that lists a Pokemon's abilities.

    Args:
        pokemon_info (dict): Dictionary of Pokemon information

    Returns:
        (str, str): Title and body text for the PasteBin paste
    """    


# TODO: Build the paste title
pokemon_name =pokemon_info['name'].capitalize()
title=f"{poke_name}'s Abilities"

   
        ## Body text
body_text= f"##{poke_name}'[abilities]:\n\n"
    for abililty in pokemon_info['abiliries']:     
        body_text += f"-{ability['ability']['name']}\n   
    return (title, body_text)


def main():
    pokemon_name = get_pokemon_name()
    pokemon_info = poke_api.get_pokemon_info(pokemon_name)
    
    if pokemon_info:
        title, body = construct_paste_title_body(pokemon_info)
        paste_url = pastebin_api.create_pastbin(title, body,)
        if paste_url:
            print(paste_url)


if __name__ == '__main__':
    main()



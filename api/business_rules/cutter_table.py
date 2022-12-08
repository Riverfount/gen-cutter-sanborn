import httpx
from bs4 import BeautifulSoup

cutter_table = {}


def gen_cutter_table():
    """This function generates a Cutter Table through web scraping from the UFRRJ Library website."""
    global cutter_table
    for index in range(1, 10):
        url = f'https://academico.ufrrj.br/biblioteca/cutter/cutter{index}.html'

        resp = httpx.get(url)

        soup = BeautifulSoup(resp.text, 'html.parser')

        letters = soup.find_all('b')[0].getText()

        for i, letter in enumerate(letters):
            cutter_table[letter.lower()] = []
            for element in soup.find_all('pre')[i].getText().split('\n'):
                if element.strip() and element.strip().isascii():
                    code, abreviaton = element.strip().split(' ' * 5)
                    cutter_table[letter.lower()].append((code, abreviaton.lower()))

    return cutter_table


def gen_cutter_code(last_name):
    """This function generates a Cutter Sanborn Code from our Cutter Table Dictionary."""
    cutter_code = ''
    last_name = last_name.lower()
    letter_key = last_name[0]
    # Here, the cutter_table is the global-cached dictionary started on main.py on the startup event function.
    for code, name in cutter_table[letter_key]:
        if name > last_name:
            break
        cutter_code = f'{letter_key.upper()}{code}'
    return cutter_code

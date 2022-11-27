import httpx
from bs4 import BeautifulSoup


def gen_cutter_table():
    cutter_table = {}
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

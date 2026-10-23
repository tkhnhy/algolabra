# Yksikkötestauksen kattavuusraportti.
```bash
Name                               Stmts   Miss  Cover
------------------------------------------------------
src\services\cooley_tukey_fft.py      50      0   100%
src\services\find_frequency.py        22      4    82%
------------------------------------------------------
TOTAL                                 72      4    94%
```

# Mitä testataan, millä syötteillä? 

Testaus keskittyy pää-asiassa itse fft algoritmiin.

Algoritmia on testattu yksinkertaisilla perus syötteillä sekä syötteillä, jotka voivat usein johtaa ongelmatilanteisiin algoritmissa. Näitä ovat:

- Tyhjä syöte
- Syöte joka ei ole 2^n kokoinen
- Syöte joka koostuu vain nollista
- Syöte joka koostuu vain ykkösistä
- Syöte joka koostu vaihtelevasti ykkösistä ja miinus ykkösistä

Myös käänteisalgoritmia testataan yksinkertaisella syötteellä sekä testillä, jossa ensin suoritetaan FFT algoritmi ja tämän jälkeen käänteinen FFT algoritmi ja varmistetaan, että saatu tulos vastaa alkuperäistä dataa.

FFT-Algoritmille on myös toteutettu suorituskykytestit, joissa mitataan kuinka se prosessoi satunnaista dataa kasvavilla ko'oilla.

find_frequencya on testattu siten, että se palauttaa oikean vahvimman taajuuden tunnetusta tiedostosta.

# Miten testit voidaan toistaa?
Käytä seuraavia komentoja projektin juuressa:

Yksikkötestit:
```bash
poetry run pytest
```

Suorituskykytestit:
```bash
poetry run pytest -o 'addopts=' -m performance
```

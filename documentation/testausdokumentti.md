# Yksikkötestauksen kattavuusraportti.

# Mitä testataan, millä syötteillä? 

Testaus keskittyy (tällä hetkellä) vain itse fft algoritmiin.

Algoritmia on testattu yksinkertaisilla perus syötteillä sekä syötteillä, jotka voivat usein johtaa ongelmatilanteisiin algoritmissa. Näitä ovat:

- Tyhjä syöte
- Syöte joka ei ole 2^n kokoinen
- Syöte joka koostuu vain nollista
- Syöte joka koostuu vain ykkösistä
- Syöte joka koostu vaihtelevasti ykkösistä ja miinus ykkösistä

Myös käänteisalgoritmia testataan yksinkertaisella syötteellä sekä testillä, jossa ensin suoritetaan FFT algoritmi ja tämän jälkeen käänteinen FFT algoritmi ja varmistetaan, että saatu tulos vastaa alkuperäistä dataa.

# Miten testit voidaan toistaa?
Käytä seuraavaa komentoa projektin juuressa:

```bash
poetry run pytest
```


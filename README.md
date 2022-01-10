# Italian Gender-specific Occupational Titles

## Visualizzazione del cambiamento d’uso del maschile e femminile nei titoli occupazionali

<b> Citation </b>

## Emerging trends in gender-specific occupational titles in Italian Newspapers

<b> Citation </b>

```
@inproceedings{cassotti2021,
  author    = {Pierluigi Cassotti and
               Andrea Iovine and
               Pierpaolo Basile and
               Marco de Gemmis and
               Giovanni Semeraro},
  editor    = {Elisabetta Fersini and
               Marco Passarotti and
               Viviana Patti},
  title     = {Emerging Trends in Gender-Specific Occupational Titles in Italian
               Newspapers},
  booktitle = {Proceedings of the Eighth Italian Conference on Computational Linguistics,
               CLiC-it 2021, Milan, Italy, January 26-28, 2022},
  series    = {{CEUR} Workshop Proceedings},
  volume    = {3033},
  publisher = {CEUR-WS.org},
  year      = {2021},
  url       = {http://ceur-ws.org/Vol-3033/paper52.pdf}
}
```

### Install dependencies

```
python3 install -r requirements.txt
```

### Run the visualization

```
python3 api.py
```
The visualization will be available at [localhost:5000/](http://localhost:5000/)

### Data

1. entities: Occurrences of named entites linked to specific occupational titles per year.
2. feminine : Frequency of occupational titles per year (feminine grammatical form).
3. masculine : Frequency of occupational titles per year (masculine grammatical form).
4. nns : Entities nearest neighborhood
5. list.tsv : List of occupational titles (masculine/feminine grammatical forms).

# unict-dmi-imagistrale-multimedia-2020-2021
Progetto multimedia per Università di Catania - Informatica (Magistrale) AA 2020/2021

Image processing tramite python. L'applicativo è gestito con richieste backend con flask e svelteJs per il frontend.

# Setup virtual environment (most safe) (all'interno della cartella)

`python3 -m venv venv` and activate with `source venv/bin/activate` 

Utils: 
- pip3 list (all list of modules)
- pip3 install flask
### creare file requirements.txt

# Svelte.js + Flask
Source:  https://github.com/cabreraalex/svelte-flask-example

A super simple example of using Flask to serve a Svelte app and use it as a backend server.

Run the following for development:

- `python server.py` to start the Flask server.
- `cd client; npm install; npm run autobuild` to automatically build and reload the Svelte frontend when it's changed.

This example just queries the Flask server for a random number.


# Piano di sviluppo
- ~~Introduzione virtual env --> ciò che è scritto qui https://www.youtube.com/watch?v=b9BYA483yVI~~
- Completare procedura venv
- ~~Import bootstrap per frontEnd~~
- ~~Refactoring delle varie funzioni fin'ora utilizzate (pulizia codice)~~
- Import algoritmi:
    - ~~Media~~
    - ~~Mediano~~
    - Guided
    - Bilateral
- Gestione upload immagine [working on]
    UPLOAD --> BASE64 --> SALVA L'IMMAGINE 
- Applicazione degli algoritmi all'immagine per cui si è fatto l'upload

## Rotte

    /               Homepage
    /median         Applica mediano all'immagine di test
    /mean           Applica filtro di media all'immagine di test

## Domande
- Necessario introdurre persistenza? Al momento scegli il file e non salvare nulla
- Chiedere se necessario a livello didattico posso utilizzare delle librerie già pronte, per farle vedere nelle altre lezioni

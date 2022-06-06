Get all transcriptions from https://radioambulante.org/category/transcripcion

I use Radio Ambulante podcasts to learn Spanish, using a tool I wrote
called [Pact](https://github.com/jzohrab/pact).  Pact uses
transcriptions, so this just gets them all, because it's always a
hassle to go and find the transcription I want from the interwebs.

(I use another tool, https://github.com/jzohrab/export-macos-podcasts,
to export the podcasts from Apple Podcasts to a folder.)

---

Descargar todas las Radio Ambulante transcripciones.

de https://radioambulante.org/category/transcripcion

Las páginas son descargadas del internet y guardadas en la carpeta 'transcripciones'

---

## Setup and usage

```
python3 -m venv .venv
source .venv/bin/activate
.venv/bin/pip3 install -r requirements.txt
deactivate
```

```
python3 -m venv .venv
source .venv/bin/activate
python download.py
deactivate
```

The transcriptions are stored in `transcripciones/`, and the raw files are cached in `cache/`.
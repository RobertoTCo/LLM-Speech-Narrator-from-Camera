
# Project adapting David Attenborough narrates your life with open-source tools (LLava & xtts)

https://twitter.com/charliebholtz/status/1724815159590293764

## Setup

Clone this repo, and setup and activate a virtualenv:

```bash
python3 -m pip install virtualenv
python3 -m virtualenv venv
source venv/bin/activate
```

Then, install the dependencies:
`pip install -r requirements.txt`


```
Download llava model from ollama
-> download ollama
-> cmd console, type: ollama run llava
```

## Run it!

In on terminal, run the webcam capture:
```bash
python capture_webcam.py
```
In another terminal, run the narrator:

```bash
python narrator_llava_xtts.py
```

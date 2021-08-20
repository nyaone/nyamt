# NyaMT

> Machine translation API for NyaOne

## Requirements
- torch
- transformers
- sentencepiece
- langdetect
- flask

## Interact

``` shell
python3 interact.py
```

## Start API Server

``` shell
python3 api.py
```

Run as service in background:

``` shell
AUTH_KEY=your_auth_key nohup python3 api.py & 
```

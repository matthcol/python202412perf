# Virtual Environments
- venv (included in python)
- virtualenv (tiers)
- distribution tool: conda

## with venv
### Create Environment
```
python -m venv venv
python -m venv .venv
python -m venv my_venv_dir
```
### Activate environment
Script: env_dir/Scripts/activate* (shell, cmd dos, powershell)

Example:
.\venv\Scripts\Activate.ps1

### Install a .wheel (manually)
pip install requests-2.32.3-py3-none-any.whl

=> install requets and its dependencies:
    urllib3, idna, charset-normalizer, certifi, requests


### Deactivate env
deactivate

## Project Managment
### setup.py (deprecated)
### pyproject.toml
backend: https://packaging.python.org/en/latest/tutorials/managing-dependencies/

pip install build
python -m build

## Requirements.txt
In a specific project environment:

`pip freeze > requirements.txt`

In the target host and new env:

`pip install -r requirements.txt`

## C/C++ Project
- article: https://realpython.com/python-bindings-overview/
- example code source numpy: https://github.com/numpy/numpy

## Obfuscation
- cython: convert python code => C code
- pyarmor:

### encrypt
pyarmor gen .\demo_request.py

### run
python .\dist\demo_request.py
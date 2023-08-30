# Windows ia-wargrow

-   Instale o Tesseract OCR no seu sistema: No Windows: Baixe o instalador do Tesseract em https://github.com/UB-Mannheim/tesseract/wiki e execute o instalador.

-   py -3.8 -m venv venv
-   cd venv/Scripts
-   .\activate
-   cd..
-   cd..
-   pip install -r requirements.txt
-   pip install pytesseract
-   python main.py
-   http://127.0.0.1:8000/docs

-   No arquivo main.py, setar o caminho absoluto do arquivo key.json

Caso queira sair do virtual environment é deactivate o comando.

Refs:
https://www.python.org/downloads/release/python-380/

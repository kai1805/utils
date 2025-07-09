# ctop - convert to PDF

The main purpose of this tool is to convert docx file to pdf, which help my dad convert all his important documents to pdf.

## Installation
#### Setup virtual environment

Note: You might need to use `python3` command instead of `python`, based on your device's configuration.

```
python -m venv ctop-env

ctop-env\Scripts\activate (windows)
source ctop-env/bin/activate (Linux/MacOS)

deactivate
```

#### Python libs installation
- **docx2pdf**

docx2pdf library utilize LibreOffice on MacOS to run the conversion, so we need to install it first. You might need to add libreoffice to PATH if it is not available.
```
brew install --cask libreoffice
```

- **pypandoc**

pypandoc need a OS package installed
```
brew install pandoc
```
Pandoc requires a TeX engine (like TeX Live or MikTeX) to generate PDF files.

Install TeX Live (if you don't have it already):
```
brew install --cask mactex
```
This will install MacTeX (TeX Live) on your system, which is required for PDF output. After installation, you may need to restart your terminal or run the following to ensure it's in your PATH:
```
sudo tlmgr update --self
```

#### Run the tool
```
pip install -r requirements.txt

python index.py
```
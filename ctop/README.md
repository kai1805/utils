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

#### Run the tool
```
docker build -t ctop .

docker run ctop
```
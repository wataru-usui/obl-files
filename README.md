# obl-files
Python script to download osama bin laden's seized files.

## About
You can download the seized files from [here](https://www.cia.gov/library/abbottabad-compound/index.html). You can't however, download the whole compressed files. But you can use this script.

## Usage
Download the index file and run the script.
```bash
wget https://www.cia.gov/library/abbottabad-compound/Everything.20171105.hash_index.txt -O index.txt && ./download.py
```

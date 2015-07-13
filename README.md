# json2csv2json

A Python 3 CLI:
- JSON locales file to CSV.
- CSV to JSON locales file.

You can use this Python 3 CLI with minor changes in a Python 2.x environment, but it is better to deal the encoding issues with Python 3.

## Usage
Python 3 command line interface:

### JSON locales file to CSV.

```bash
$ python3 jsonlocales2csv.py [-h] inputJSON outputCSV

positional arguments:
  inputJSON   input JSON file
  outputCSV   output CSV file

optional arguments:
  -h, --help  show this help message and exit
```


### CSV to JSON locals file.

```bash
$ python3 csv2jsonlocales.py [-h] inputCSV outputJSON

positional arguments:
  inputCSV    input CSV file
  outputJSON  output JSON file

optional arguments:
  -h, --help  show this help message and exit
```

## About author
Developed by Cayetano Benavent.
GIS Analyst at Geographica.

http://www.geographica.gs

## License
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

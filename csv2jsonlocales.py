# -*- coding: utf-8 -*-
#  
#  CSV to JSON locales file. A Python 3 CLI.
# 
#  Author: Cayetano Benavent, 2015.
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
# 


import csv
import json
import argparse



def csvToJsonLocs(csvfile, jsonfile):
    """
    CSV to JSON translator (and transposer)...
    
    """
    
    print("\nReading CSV file: {}".format(csvfile))
    
    try:
    
        csvf = open(csvfile, 'r')
        jsf = open(jsonfile, 'w')
        
        reader = csv.reader(csvf)
        out = json.dumps({k: v for k,v in reader}, ensure_ascii=False, indent=2, sort_keys=True)
        
        jsf.write(out)
    
        print("JSON file successfully created: {}\n".format(jsonfile))
    
    except Exception as err:
        print("Error: {0}\n".format(err))


def main():
    
    arg_parser = argparse.ArgumentParser(description='CSV to JSON locales file')
    
    arg_parser.add_argument('inputCSV', type=str, help='input CSV file')
    arg_parser.add_argument('outputJSON', type=str, help='output JSON file')
    
    args = arg_parser.parse_args()

    file_input = args.inputCSV

    file_output = args.outputJSON
    
    csvToJsonLocs(file_input, file_output)


if __name__ == '__main__':
    main()

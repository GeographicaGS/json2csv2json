# -*- coding: utf-8 -*-
#
#  JSON locales file to CSV. A Python 3 CLI.
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



def jsonLocsToCsv(jsonfile, csvfile):
    """
    JSON to CSV translator (and transposer)...
    
    """

    print("\nReading JSON file: {}".format(jsonfile))

    try:

        with open(jsonfile, 'r') as jsf:
            jsonfl = json.load(jsf, encoding="utf-8")
    
            with open(csvfile, 'w') as f:
    
                print("Writing CSV file...")
                w = csv.DictWriter(f, jsonfl.keys())
                w.writeheader()
                w.writerow(jsonfl)
    
                print("Transposing CSV rows...")
                tps = zip(*csv.reader(open(csvfile, "r")))
                csv.writer(open(csvfile, "w")).writerows(tps)
    
                print("CSV file successfully created: {}\n".format(csvfile))

    except Exception as err:
        print("Error: {0}\n".format(err))


def main():
    
    arg_parser = argparse.ArgumentParser(description='JSON locales file to CSV')

    arg_parser.add_argument('inputJSON', type=str, help='input JSON file')
    arg_parser.add_argument('outputCSV', type=str, help='output CSV file')

    args = arg_parser.parse_args()

    file_input = args.inputJSON

    file_output = args.outputCSV

    jsonLocsToCsv(file_input, file_output)


if __name__ == '__main__':
    main()

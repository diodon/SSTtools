# DHWtools
Tools for extracting DHW and related variables form CRW erddap server

## DHW_flexiharvester

A small python function that harverst DHW and related variables given coordinates and a date range. The results are stored in a csv file.  

```
usage: DHW_flexiharvester.py [-h] -lat LATITUDE -lon LONGITUDE -from
                             DATE_START -to DATE_END [-fout FOUT]

Harvest DHW and related variables from CRW ERDDAP server. The results are
stored in a csv file

optional arguments:
  -h, --help        show this help message and exit
  -lat LATITUDE     latitude in decimal degrees
  -lon LONGITUDE    longitude in decimal degrees
  -from DATE_START  start date in yyyy-mm-dd
  -to DATE_END      end date in yyyy-mm-dd
  -fout FOUT        name of the output CSV file. Default DHWoutput.csv

```

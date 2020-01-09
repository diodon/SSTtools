# Python SST tools
Tools for extracting DHW and related variables from [CRW ERDDAP server](http://oos.soest.hawaii.edu/erddap/griddap/NOAA_DHW_5km.html) and SST variables from [NASA-JPL ERDDAP server](https://coastwatch.pfeg.noaa.gov/erddap/griddap/jplMURSST41.html)

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

## MURSST_flexiharvester

A small python function that harverst MURSST and related variables given coordinates and a date range. The results are stored in a csv file.  

```
usage: MURSST_flexiharvester.py [-h] -lat LATITUDE -lon LONGITUDE -from
                                DATE_START -to DATE_END [-fout FOUT]

Harvest MURSST and related variables from NASA-JPL ERDDAP server. The results
are stored in a csv file

optional arguments:
  -h, --help        show this help message and exit
  -lat LATITUDE     latitude in decimal degrees. Southern hemisphere negative
  -lon LONGITUDE    longitude in decimal degrees. Western hemisphere negative
  -from DATE_START  start date in yyyy-mm-dd
  -to DATE_END      end date in yyyy-mm-dd
  -fout FOUT        name of the output CSV file. Default SSToutput.csv

```

## SEASCAPE_TSextractor

A small python function that harverst SEASCAPE classes and related variables given coordinates and a date range. The results are stored in a csv file.  

```
usage: SEASCAPE_TSextractor.py [-h] -type TYPE -lat LATITUDE -lon LONGITUDE
                               -from DATE_START -to DATE_END [-fout FOUT]

Harvest SEASCPE classes from NOAA CoastWatch ERDDAP server. The results are
stored in a csv file

optional arguments:
  -h, --help        show this help message and exit
  -type TYPE        monthly (m) or 8day (8d) product
  -lat LATITUDE     latitude in decimal degrees. Southern hemisphere negative
  -lon LONGITUDE    longitude in decimal degrees. Western hemisphere negative
  -from DATE_START  start date in yyyy-mm-dd
  -to DATE_END      end date in yyyy-mm-dd
  -fout FOUT        name of the output CSV file. Default SEASCAPEoutput.csv

```

## SEASCAPE_gridextractor

Extract SEASCAPE maps (grids) given a coordinates and date ranges

```
usage: SEASCAPE_gridextractor.py [-h] -type TYPE -minlat MINLAT -minlon MINLON
                                 -maxlat MAXLAT -maxlon MAXLON -from
                                 DATE_START -to DATE_END [-fout FOUT]

Harvest SEASCPE classes from NOAA CoastWatch ERDDAP server. The results are
stored in a csv file

optional arguments:
  -h, --help        show this help message and exit
  -type TYPE        monthly (m) or 8day (8d) product
  -minlat MINLAT    latitude in decimal degrees. Southern hemisphere negative
  -minlon MINLON    longitude in decimal degrees. Western hemisphere negative
  -maxlat MAXLAT    latitude in decimal degrees. Southern hemisphere negative
  -maxlon MAXLON    longitude in decimal degrees. Western hemisphere negative
  -from DATE_START  start date in yyyy-mm-dd
  -to DATE_END      end date in yyyy-mm-dd
  -fout FOUT        name of the output CSV file. Default SEASCAPEgridoutput.nc

```


# Python SST tools
Tools for extracting DHW and related variables from [CRW ERDDAP server](http://oos.soest.hawaii.edu/erddap/griddap/NOAA_DHW_5km.html) and SST variables from [NASA-JPL ERDDAP server](https://coastwatch.pfeg.noaa.gov/erddap/griddap/jplMURSST41.html)


## getSatProd

Get satellite product. A versatile comprehensive tool to retrieve several parameter from a single coordinate or a grid from a single date or a range of dates. Every parameter is stored in a separate file. 

**NOTE**: THINK before retrieve. It is very easy to ask for hundreds of thousands of values if you specify a large grid over long time. 

```
usage: getSatProd.py [-h] -param PARAM [PARAM ...] -latmin LAT_MIN
                     [-latmax LAT_MAX] -lonmin LON_MIN [-lonmax LON_MAX] -ds
                     DATE_START [-de DATE_END] [-loc LOCALITY] [-out OUTPATH]
                     [-print]

Get different satellite products from NOAAs ERDDAP servers. The valid parameters are: 
- sst, ssta, sstclim: MURSST cloudless sea surface temperature, anomaly and climatology 
- poc1d, poc8d, poc1m: MODIS particulate organic cabon, 1 day, 8 day, 1 month 
- pic1d, pic8d, pic1m: MODIS particulate inorganic cabon, 1 day, 8 day, 1 month 
- chl1d, chl8d, chl1m: VIRRS chlorophyll a concetration, 1 day, 8 days, 1 month 
- dhw: coral reef watch degree heating week products 
- par1d, par8d, par1m: Total Photosynthetic Available Radiation, 1 day, 8 day, 1 month 
- pp1d, pp8d, pp1m: Primary Productivity, 1 day, 8 day, 1 month 
- ssc8d, ssc1m: Seascapes classes, 8 day, 1 month 
- prec1d: Total daily rainfall 
NOTE: THINK before request. Do not ask for large grid over a long period of time

optional arguments:
  -h, --help            show this help message and exit
  -param PARAM [PARAM ...]
                        latitude in decimal degrees
  -latmin LAT_MIN       start latitude in decimal degrees
  -latmax LAT_MAX       end latitude in decimal degrees. If missing extract
                        for start latitude only
  -lonmin LON_MIN       start longitude in decimal degrees
  -lonmax LON_MAX       end longitude in decimal degrees. If missing extract
                        for start longitude only
  -ds DATE_START        start date in yyyy-mm-dd
  -de DATE_END          end date in yyyy-mm-dd. If missing retrieve for start
                        date only
  -loc LOCALITY         name of the locality
  -out OUTPATH          path where to write the result file
  -print                print the results to the screen


```

---------------------------

## DHW_flexiharvester

A small python function that harvest DHW and related variables given coordinates and a date range. If the output file name is given , the results are stored in a csv file. The function returns a pandas data frame with the extracted variables.  

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

## CHL_flexiharvester

A small python function that harvest CHL from MODIS or VIIRS sensors, daily. weekly or montly products, given coordinates and a date range. The results are stored in a csv file.

```
usage: CHL_flexiharvester.py [-h] -sensor SENSOR -frequency FREQUENCY -lat
                             LATITUDE -lon LONGITUDE -from DATE_START -to
                             DATE_END [-fout FOUT]

Harvest CHL form MODIS/VIIRS sensors. The results are stored in a csv file

optional arguments:
  -h, --help            show this help message and exit
  -sensor SENSOR        sensor type: MODIS or VIIRS
  -frequency FREQUENCY  type of the aggregation: day, week, or month
  -lat LATITUDE         latitude in decimal degrees. Southern hemisphere
                        negative
  -lon LONGITUDE        longitude in decimal degrees. Western hemisphere
                        negative
  -from DATE_START      start date in yyyy-mm-dd
  -to DATE_END          end date in yyyy-mm-dd
  -fout FOUT            name of the output CSV file. Default CHLoutput.csv


```

## SEASCAPE_TSextractor

A small python function that harvest SEASCAPE classes and related variables given coordinates and a date range. The results are stored in a csv file.  

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

Extract SEASCAPE maps (grids) given a coordinates and date ranges. The result is saved in a netCDF file

```
usage: SEASCAPE_gridextractor.py [-h] -type TYPE -minlat MINLAT -minlon MINLON
                                 -maxlat MAXLAT -maxlon MAXLON -from
                                 DATE_START -to DATE_END [-fout FOUT]

Harvest SEASCAPE classes (grid) from NOAA CoastWatch ERDDAP server. The
results are stored in a netCDF file

optional arguments:
  -h, --help        show this help message and exit
  -type TYPE        monthly (m) or 8day (8d) product
  -minlat MINLAT    latitude in decimal degrees. Southern hemisphere negative
  -minlon MINLON    longitude in decimal degrees. Western hemisphere negative
  -maxlat MAXLAT    latitude in decimal degrees. Southern hemisphere negative
  -maxlon MAXLON    longitude in decimal degrees. Western hemisphere negative
  -from DATE_START  start date in yyyy-mm-dd
  -to DATE_END      end date in yyyy-mm-dd
  -fout FOUT        name of the output netCDF file. Default
                    SEASCAPEgrid_output.nc

```


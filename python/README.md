# Python SST tools
Tools for extracting DHW and related variables from [CRW ERDDAP server](http://oos.soest.hawaii.edu/erddap/griddap/NOAA_DHW_5km.html) and SST variables from [NASA-JPL ERDDAP server](https://coastwatch.pfeg.noaa.gov/erddap/griddap/jplMURSST41.html)


## getSatProd

Get satellite product. A versatile comprehensive tool to retrieve several parameter from a single coordinate or a grid from a single date or a range of dates. Every parameter is stored in a separate file. 

**NOTE**: THINK before retrieve. It is very easy to ask for hundreds of thousands of values if you specify a large grid over long time. 

### Data sources: 

|parameter | Description | ERDDAP URL | 
|----------|-------------|------------| 
sst | Multi-scale Ultra-high Resolution (MUR) SST Analysis fv04.1, Global, 0.01°, 2002-present, Daily | https://coastwatch.pfeg.noaa.gov/erddap/griddap/jplMURSST41  
ssta | Multi-scale Ultra-high Resolution (MUR) SST Analysis Anomaly fv04.1, Global, 0.01°, 2002-present, Daily | https://coastwatch.pfeg.noaa.gov/erddap/griddap/jplMURSST41anom1day  
poc1d | MODIS Aqua, Level-3 SMI, Global, 4km, Particulate Organic Carbon, 2003-present (1 Day Composite) | https://coastwatch.pfeg.noaa.gov/erddap/griddap/erdMPOC1day  
poc8d | MODIS Aqua, Level-3 SMI, Global, 4km, Particulate Organic Carbon, 2003-present (8 Day Composite) | https://coastwatch.pfeg.noaa.gov/erddap/griddap/erdMPOC8day  
poc1m |MODIS Aqua, Level-3 SMI, Global, 4km, Particulate Organic Carbon, 2003-present (Monthly Composite) |https://coastwatch.pfeg.noaa.gov/erddap/griddap/erdMPOCmday  
pic1d | MODIS Aqua, Level-3 SMI, Global, 4km, Particulate Inorganic Carbon, 2003-present (1 Day Composite) |https://coastwatch.pfeg.noaa.gov/erddap/griddap/erdMPIC1day  
pic8d |  MODIS Aqua, Level-3 SMI, Global, 4km, Particulate Inorganic Carbon, 2003-present (8 Day Composite) |https://coastwatch.pfeg.noaa.gov/erddap/griddap/erdMPIC8day  
pic1m |  MODIS Aqua, Level-3 SMI, Global, 4km, Particulate Inorganic Carbon, 2003-present (monthly Composite) |https://coastwatch.pfeg.noaa.gov/erddap/griddap/erdMPICmday  
chl1m | Chlorophyll, NOAA VIIRS, Science Quality, Global 1 month | https://coastwatch.pfeg.noaa.gov/erddap/griddap/nesdisVHNSQchlaMonthly   
chl8d | Chlorophyll, NOAA VIIRS, Science Quality, Global 8 days |https://coastwatch.pfeg.noaa.gov/erddap/griddap/nesdisVHNSQchlaWeekly  
chl1d | Chlorophyll, NOAA VIIRS, Science Quality, Global 1 day |https://coastwatch.pfeg.noaa.gov/erddap/griddap/nesdisVHNSQchlaDaily  
dhw | NOAA Coral Reef Watch Operational Daily Near-Real-Time Global 5-km Satellite Coral Bleaching Monitoring Products |  https://coastwatch.pfeg.noaa.gov/erddap/griddap/NOAA_DHW  
par1d | Photosynthetically Available Radiation, Aqua MODIS, NPP, L3SMI, Global, 4km, Science Quality 1 day| https://coastwatch.pfeg.noaa.gov/erddap/griddap/erdMH1par01day   
par8d | Photosynthetically Available Radiation, Aqua MODIS, NPP, L3SMI, Global, 4km, Science Quality 8 days | https://coastwatch.pfeg.noaa.gov/erddap/griddap/erdMH1par08day  
par1m | Photosynthetically Available Radiation, Aqua MODIS, NPP, L3SMI, Global, 4km, Science Quality 1 month | https://coastwatch.pfeg.noaa.gov/erddap/griddap/erdMH1par0mday  
pp1d | Primary Productivity, Aqua MODIS, NPP, Global, 2003-present, EXPERIMENTAL (1 Day Composite) | https://coastwatch.pfeg.noaa.gov/erddap/griddap/erdMH1pp1day  
pp3d | Primary Productivity, Aqua MODIS, NPP, Global, 2003-present, EXPERIMENTAL (3 Day Composite) |https://coastwatch.pfeg.noaa.gov/erddap/griddap/erdMH1pp3day  
pp8d | Primary Productivity, Aqua MODIS, NPP, Global, 2003-present, EXPERIMENTAL (8 Day Composite) |  https://coastwatch.pfeg.noaa.gov/erddap/griddap/erdMH1pp8day  
pp1m | Primary Productivity, Aqua MODIS, NPP, Global, 2003-present, EXPERIMENTAL (Monthly Composite) |  https://coastwatch.pfeg.noaa.gov/erddap/griddap/erdMH1ppmday  
ssc8d | 8_Day Global Seascapes | https://cwcgom.aoml.noaa.gov/erddap/griddap/noaa_aoml_seascapes_8day  
ssc1m |	Monthly Global Seascapes |https://cwcgom.aoml.noaa.gov/erddap/griddap/noaa_aoml_4729_9ee6_ab54  
prec1d | satellite product TRMM TRMM PR 3B42 daily v7 | https://oceanwatch.pifsc.noaa.gov/erddap/griddap/hawaii_soest_5687_3d16_a6d4  




```
usage: getSatProd.py [-h] -param PARAM [PARAM ...] -latmin LAT_MIN
                     [-latmax LAT_MAX] -lonmin LON_MIN [-lonmax LON_MAX] -ds
                     DATE_START [-de DATE_END] [-loc LOCALITY] [-out OUTPATH]
                     [-print]

Get different satellite products from NOAAs ERDDAP servers. The valid parameters are: 
- sst, ssta: MURSST cloudless sea surface temperature, and  sst anomaly  
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

### Example

```
python getSatProd.py -param sst ssta par1d ssc8d -latmin 14 -lonmin -40 -ds 2020-01-01 -de 2020-01-05 -loc middle-of-nowhere

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

## PAR_gridextractor

Extract monthly, weekly or daily PAR values

```
usage: PAR_gridextractor.py [-h] -type TYPE -minlat MINLAT -minlon MINLON -maxlat MAXLAT -maxlon MAXLON -from DATE_START -to
                            DATE_END -format FORMAT [-fout FOUT]

Harvest monthly, weekly or daily PAR (Photosynthetically Available Radiation, Aqua MODIS, NPP, L3SMI, Global, 4km, Science Quality,
2003-present) from NOAA CoastWatch ERDDAP server. The results are stored in a netCDF or CSV file

optional arguments:
  -h, --help        show this help message and exit
  -type TYPE        monthly (m), 8day (8d) or (1d) daily product
  -minlat MINLAT    latitude in decimal degrees. Southern hemisphere negative
  -minlon MINLON    longitude in decimal degrees. Western hemisphere negative
  -maxlat MAXLAT    latitude in decimal degrees. Southern hemisphere negative
  -maxlon MAXLON    longitude in decimal degrees. Western hemisphere negative
  -from DATE_START  start date in yyyy-mm-dd
  -to DATE_END      end date in yyyy-mm-dd
  -format FORMAT    output format: nc or csv
  -fout FOUT        name of the output file without extension. Default PARgrid_output

```

import sys
import os
import urllib.request
import argparse
from argparse import RawDescriptionHelpFormatter
import pandas as pd


def getParams(params, lat_min, lat_max, lon_min, lon_max, date_start, date_end, locality, outpath, screen_print):
    """
    get satellite products from NOAAs ERDDAP servers.
    E. Klein. ekleins@gmail.com
    :param params: list of requested params
    :param lat_min: latitude min
    :param lat_max: latitude max
    :param lon_min: longitude min
    :param lon_max: longitude max
    :param date_start: start date
    :param date_end: end date
    :param locality: name of the locality for output file naming
    :param outpath: where to wrtie the result file
    :param screen_print: if True, results are printed to the screen
    :return: nothing
    """
    ## SOURCES
    sources = {
        'sst':      "https://coastwatch.pfeg.noaa.gov/erddap/griddap/jplMURSST41.csv?"
                    "analysed_sst[({date_start}):1:({date_end})][({lat_min}):1:({lat_max})][({lon_min}):1:({lon_max})],"
                    "analysis_error[({date_start}):1:({date_end})][({lat_min}):1:({lat_max})][({lon_min}):1:({lon_max})]",
        'ssta':     "https://coastwatch.pfeg.noaa.gov/erddap/griddap/jplMURSST41anom1day.csv?"
                    "sstAnom[({date_start}):1:({date_end})][({lat_min}):1:({lat_max})][({lon_min}):1:({lon_max})]",
        'sstclim':  "https://coastwatch.pfeg.noaa.gov/erddap/griddap/jplMURSST41clim.csv?"
                    "mean_sst[({date_start}):1:({date_end})][({lat_min}):1:({lat_max})][({lon_min}):1:({lon_max})],"
                    "standard_deviation[({date_start}):1:({date_end})][({lat_min}):1:({lat_max})][({lon_min}):1:({lon_max})]",
        'poc1d':    "https://coastwatch.pfeg.noaa.gov/erddap/griddap/erdMPOC1day.csv?"
                    "poc[({date_start}):1:({date_end})][({lat_min}):1:({lat_max})][({lon_min}):1:({lon_max})]",
        'poc8d':    "https://coastwatch.pfeg.noaa.gov/erddap/griddap/erdMPOC8day.csv?"
                    "poc[({date_start}):1:({date_end})][({lat_min}):1:({lat_max})][({lon_min}):1:({lon_max})]",
        'poc1m':    "https://coastwatch.pfeg.noaa.gov/erddap/griddap/erdMPOCmday.csv?"
                    "poc[({date_start}):1:({date_end})][({lat_min}):1:({lat_max})][({lon_min}):1:({lon_max})]",
        'pic1d':    "https://coastwatch.pfeg.noaa.gov/erddap/griddap/erdMPIC1day.csv?"
                    "pic[({date_start}):1:({date_end})][({lat_min}):1:({lat_max})][({lon_min}):1:({lon_max})]",
        'pic8d':    "https://coastwatch.pfeg.noaa.gov/erddap/griddap/erdMPIC8day.csv?"
                    "pic[({date_start}):1:({date_end})][({lat_min}):1:({lat_max})][({lon_min}):1:({lon_max})]",
        'pic1m':    "https://coastwatch.pfeg.noaa.gov/erddap/griddap/erdMPICmday.csv?"
                    "pic[({date_start}):1:({date_end})][({lat_min}):1:({lat_max})][({lon_min}):1:({lon_max})]",
        'chl1m':    "https://coastwatch.pfeg.noaa.gov/erddap/griddap/nesdisVHNSQchlaMonthly.csv?"
                    "chlor_a[({date_start}):1:({date_end})][(0.0):1:(0.0)][({lat_min}):1:({lat_max})][({lon_min}):1:({lon_max})]",
        'chl8d':    "https://coastwatch.pfeg.noaa.gov/erddap/griddap/nesdisVHNSQchlaWeekly.csv?"
                    "chlor_a[({date_start}):1:({date_end})][(0.0):1:(0.0)][({lat_min}):1:({lat_max})][({lon_min}):1:({lon_max})]",
        'chl1d':    "https://coastwatch.pfeg.noaa.gov/erddap/griddap/nesdisVHNSQchlaDaily.csv?"
                    "chlor_a[({date_start}):1:({date_end})][(0.0):1:(0.0)][({lat_min}):1:({lat_max})][({lon_min}):1:({lon_max})]",
        'dhw':      "https://coastwatch.pfeg.noaa.gov/erddap/griddap/NOAA_DHW.csv?"
                    "CRW_DHW[({date_start}):1:({date_end})][({lat_min}):1:({lat_max})][({lon_min}):1:({lon_max})],"
                    "CRW_HOTSPOT[({date_start}):1:({date_end})][({lat_min}):1:({lat_max})][({lon_min}):1:({lon_max})],"
                    "CRW_BAA[({date_start}):1:({date_end})][({lat_min}):1:({lat_max})][({lon_min}):1:({lon_max})],"
                    "CRW_SST[({date_start}):1:({date_end})][({lat_min}):1:({lat_max})][({lon_min}):1:({lon_max})],"
                    "CRW_SSTANOMALY[({date_start}):1:({date_end})][({lat_min}):1:({lat_max})][({lon_min}):1:({lon_max})]",
        'par1d':    "https://coastwatch.pfeg.noaa.gov/erddap/griddap/erdMH1par01day.csv?"
                    "par[({date_start}):1:({date_end})][({lat_min}):1:({lat_max})][({lon_min}):1:({lon_max})]",
        'par8d':    "https://coastwatch.pfeg.noaa.gov/erddap/griddap/erdMH1par08day.csv?"
                    "par[({date_start}):1:({date_end})][({lat_min}):1:({lat_max})][({lon_min}):1:({lon_max})]",
        'par1m':    "https://coastwatch.pfeg.noaa.gov/erddap/griddap/erdMH1par0mday.csv?"
                    "par[({date_start}):1:({date_end})][({lat_min}):1:({lat_max})][({lon_min}):1:({lon_max})]",
        'pp1d':     "https://coastwatch.pfeg.noaa.gov/erddap/griddap/erdMH1pp1day.csv?"
                    "productivity[({date_start}):1:({date_end})][(0.0):1:(0.0)][({lat_min}):1:({lat_max})][({lon_min}):1:({lon_max})]",
        'pp3d':     "https://coastwatch.pfeg.noaa.gov/erddap/griddap/erdMH1pp3day.csv?"
                    "productivity[({date_start}):1:({date_end})][(0.0):1:(0.0)][({lat_min}):1:({lat_max})][({lon_min}):1:({lon_max})]",
        'pp8d':     "https://coastwatch.pfeg.noaa.gov/erddap/griddap/erdMH1pp8day.csv?"
                    "productivity[({date_start}):1:({date_end})][(0.0):1:(0.0)][({lat_min}):1:({lat_max})][({lon_min}):1:({lon_max})]",
        'pp1m':     "https://coastwatch.pfeg.noaa.gov/erddap/griddap/erdMH1ppmday.csv?"
                    "productivity[({date_start}):1:({date_end})][(0.0):1:(0.0)][({lat_min}):1:({lat_max})][({lon_min}):1:({lon_max})]",
        'ssc8d':    "https://cwcgom.aoml.noaa.gov/erddap/griddap/noaa_aoml_seascapes_8day.csv?"
                    "CLASS[({date_start}):1:({date_end})][({lat_min}):1:({lat_max})][({lon_min}):1:({lon_max})],"
                    "P[({date_start}):1:({date_end})][({lat_min}):1:({lat_max})][({lon_min}):1:({lon_max})]",
        'ssc1m':    "https://cwcgom.aoml.noaa.gov/erddap/griddap/noaa_aoml_4729_9ee6_ab54.csv?"
                    "CLASS[({date_start}):1:({date_end})][({lat_min}):1:({lat_max})][({lon_min}):1:({lon_max})],"
                    "P[({date_start}):1:({date_end})][({lat_min}):1:({lat_max})][({lon_min}):1:({lon_max})]",
        'prec1d':   "https://oceanwatch.pifsc.noaa.gov/erddap/griddap/hawaii_soest_5687_3d16_a6d4.csv?"
                    "precipitation[({date_start}):1:({date_end})][({lat_min}):1:({lat_max})][({lon_min}):1:({lon_max})]"
    }


    for par in params:
        print(par.upper())
        fout = os.path.join(locality + "_" + par + "_" + date_start.replace("-", "") + "-" + date_end.replace("-", "") + ".csv")
        url = sources[par].format(lat_min=lat_min, lat_max = lat_max,  lon_min=lon_min, lon_max=lon_max,
                                  date_start = date_start, date_end = date_end)
        try:
            df = pd.read_csv(url)
            df.to_csv(os.path.join(outpath, fout), index=False)
            print(fout)
            if screen_print:
                print(df)
        except:
            print("FAILED:" + fout)

    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(description="Get different satellite products from NOAAs ERDDAP servers. The valid parameters are: \n"
                                                 "- sst, ssta, sstclim: MURSST cloudless sea surface temperature, anomaly and climatology \n"
                                                 "- poc1d, poc8d, poc1m: MODIS particulate organic cabon, 1 day, 8 day, 1 month \n"
                                                 "- pic1d, pic8d, pic1m: MODIS particulate inorganic cabon, 1 day, 8 day, 1 month \n"
                                                 "- chl1d, chl8d, chl1m: VIRRS chlorophyll a concetration, 1 day, 8 days, 1 month \n"
                                                 "- dhw: coral reef watch degree heating week products \n"
                                                 "- par1d, par8d, par1m: Total Photosynthetic Available Radiation, 1 day, 8 day, 1 month \n"
                                                 "- pp1d, pp8d, pp1m: Primary Productivity, 1 day, 8 day, 1 month \n"
                                                 "- ssc8d, ssc1m: Seascapes classes, 8 day, 1 month \n"
                                                 "- prec1d: Total daily rainfall \n"
                                                 "NOTE: THINK before request. Do not ask for large grid over a long period of time",
                                     formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('-param', dest='param', help='latitude in decimal degrees', nargs='+', required=True)
    parser.add_argument('-latmin', dest='lat_min', help='start latitude in decimal degrees', required=True)
    parser.add_argument('-latmax', dest='lat_max', help='end latitude in decimal degrees. If missing extract for start latitude only',
                        required=False)
    parser.add_argument('-lonmin', dest='lon_min', help='start longitude in decimal degrees', required=True)
    parser.add_argument('-lonmax', dest='lon_max', help='end longitude in decimal degrees. If missing extract for start longitude only',
                        required=False)
    parser.add_argument('-ds', dest='date_start', help='start date in yyyy-mm-dd', required=True)
    parser.add_argument('-de', dest='date_end', help='end date in yyyy-mm-dd. If missing retrieve for start date only', required=False)
    parser.add_argument('-loc', dest='locality', help='name of the locality', default="satprod", required=False)
    parser.add_argument('-out', dest='outpath', help='path where to write the result file', default='./', required=False)
    parser.add_argument('-print', dest='screen_print', help='print the results to the screen', action='store_true',
                        required=False)
    args = parser.parse_args()

    parameter_list = ['sst', 'ssta', 'sstclim', 'poc1d', 'poc8d', 'poc1m', 'pic1d', 'pic8d', 'pic1m', 'chl1d', 'chl8d',
                      'chl1m', 'dhw', 'par1d', 'par8d', 'par1m', 'pp1d', 'pp8d', 'pp1m', 'ssc8d', 'ssc1m', 'prec1d']

    if args.date_end == None:
        args.date_end = args.date_start

    if args.lat_max == None:
        args.lat_max = args.lat_min

    if args.lon_max == None:
        args.lon_max = args.lon_min

    if not set(args.param).issubset(parameter_list):
        print("Invalid parameter. See function help")
        sys.exit()


    getParams(args.param, args.lat_min, args.lat_max, args.lon_min, args.lon_max, args.date_start, args.date_end,
              args.locality, args.outpath, args.screen_print)





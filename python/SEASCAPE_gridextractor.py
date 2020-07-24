import sys
import argparse

import urllib.request
import urllib.parse


def makeRange(startValue, endValue):
    rr = '[(' + startValue + '):1:(' + endValue + ')]'
    return rr


def getDHW(type, minlat, minlon, maxlat, maxlon, date_start, date_end, fout):
    """
    function to harvest seascape classes and related variables from ERDDAP server
    the results are stores in a csv file
    Eduardo Klein. ekleins@gmail.com

    :param latitude: latitude in decimal degrees
    :param longitude: longitude in decimal degrees
    :param date_start: start date in yyyy-mm-dd
    :param date_end: end date in yyyy-mm-dd
    :param fout: file name for the results
    :return: nothing
    """

    if type == 'm':
        serverURL = 'https://cwcgom.aoml.noaa.gov/erddap/griddap/noaa_aoml_4729_9ee6_ab54.nc?'
    elif type == '8d':
        serverURL = 'https://cwcgom.aoml.noaa.gov/erddap/griddap/noaa_aoml_seascapes_8day.nc?'
    else:
        print("ERROR: Wrong product type. Valid products are \'m\' for monthly or \'8d\' for 8 day")
        sys.exit()

    varNames = ['CLASS', 'P']
    constrains = urllib.parse.quote(makeRange(date_start, date_end) + makeRange(minlat, maxlat) + makeRange(minlon, maxlon))
    varList = varNames[0] + constrains
    for var in varNames[1:]:
        varList = varList + "," + var + constrains
    url = serverURL + varList
    ##print(url)
    try:
        urllib.request.urlretrieve(url, fout)
    except:
        print("Failed")


    return print('Results written to {}'.format(fout))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Harvest SEASCAPE classes (grid) from NOAA CoastWatch ERDDAP server. The results are stored in a netCDF file')
    parser.add_argument('-type', dest='type', help='monthly (m) or 8day (8d) product', required=True)
    parser.add_argument('-minlat', dest='minlat', help='latitude in decimal degrees. Southern hemisphere negative', required=True)
    parser.add_argument('-minlon', dest='minlon', help='longitude in decimal degrees. Western hemisphere negative', required=True)
    parser.add_argument('-maxlat', dest='maxlat', help='latitude in decimal degrees. Southern hemisphere negative', required=True)
    parser.add_argument('-maxlon', dest='maxlon', help='longitude in decimal degrees. Western hemisphere negative', required=True)
    parser.add_argument('-from', dest='date_start', help='start date in yyyy-mm-dd', required=True)
    parser.add_argument('-to', dest='date_end', help='end date in yyyy-mm-dd', required=True)
    parser.add_argument('-fout', dest='fout', help='name of the output netCDF file. Default SEASCAPEgrid_output.nc',
                        default='SEASCAPEgrid_output.nc', required=False)
    args = parser.parse_args()

    getDHW(args.type, args.minlat, args.minlon, args.maxlat, args.maxlon, args.date_start, args.date_end, args.fout)



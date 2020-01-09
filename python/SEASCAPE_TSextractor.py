import sys
import argparse

import urllib


def makeRange(rangeValue):
    rangeValue = str(rangeValue)
    rr = '[(' + rangeValue + '):(' + rangeValue + ')]'
    return rr


def makeDateRange(date_start, date_end):
    rr = '[(' + date_start + '):(' + date_end + ')]'

    return rr


def getDHW(type, latitude, longitude, date_start, date_end, fout):
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


    if type=='m':
        serverURL = 'https://cwcgom.aoml.noaa.gov/erddap/griddap/noaa_aoml_4729_9ee6_ab54.csv?'
    elif type=='8d':
        serverURL = 'https://cwcgom.aoml.noaa.gov/erddap/griddap/noaa_aoml_seascapes_8day.csv?'
    else:
        print("ERROR: Wrong product type. Valid products are \'m\' for monthly or \'8d\' for 8 day")
        sys.exit()

    varNames = ['CLASS', 'P']
    varNames_DHW = ['time',  'latitude', 'longitude']

    dateRange = makeDateRange(date_start, date_end)
    constrains = urllib.parse.quote(dateRange + makeRange(latitude) + makeRange(longitude))
    varList = varNames[0] + constrains
    for var in varNames[1:]:
        varList = varList + "," + var + constrains
    url = serverURL + varList

    try:
        urllib.request.urlretrieve(url, fout)
    except:
        print("Failed")

    return print('Write {} SEASCAPE values into {}'.format(len(DHW), fout))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Harvest SEASCPE classes from NOAA CoastWatch ERDDAP server. The results are stored in a csv file')
    parser.add_argument('-type', dest='type', help='monthly (m) or 8day (8d) product', required=True)
    parser.add_argument('-lat', dest='latitude', help='latitude in decimal degrees. Southern hemisphere negative', required=True)
    parser.add_argument('-lon', dest='longitude', help='longitude in decimal degrees. Western hemisphere negative', required=True)
    parser.add_argument('-from', dest='date_start', help='start date in yyyy-mm-dd', required=True)
    parser.add_argument('-to', dest='date_end', help='end date in yyyy-mm-dd', required=True)
    parser.add_argument('-fout', dest='fout', help='name of the output CSV file. Default SEASCAPEoutput.csv',
                        default='SEASCAPEoutput.csv', required=False)
    args = parser.parse_args()

    getDHW(args.type, args.latitude, args.longitude, args.date_start, args.date_end, args.fout)



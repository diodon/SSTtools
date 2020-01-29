import sys
import argparse
import urllib.parse
import urllib.request

def makeRange(rangeValue):
    rangeValue = str(rangeValue)
    rr = '[(' + rangeValue + '):(' + rangeValue + ')]'
    return rr


def makeDateRange(date_start, date_end):
    rr = '[(' + date_start + '):(' + date_end + ')]'

    return rr


def getCHL(sensor, frequency, latitude, longitude, date_start, date_end, fout):
    """
    function to harvest CHL from CRW ERDDAP server
    the results are stores in a csv file
    Eduardo Klein. ekleins@gmail.com

    :param sensor: senosr type MODIS or VIIRS
    :param frequency: daily, weekly or monthly product
    :param latitude: latitude in decimal degrees
    :param longitude: longitude in decimal degrees
    :param date_start: start date in yyyy-mm-dd
    :param date_end: end date in yyyy-mm-dd
    :param fout: file name for the results
    :return: print name of the output file
    """

    serverURL = 'https://coastwatch.pfeg.noaa.gov/erddap/griddap/'

    if sensor == "MODIS":
        varNames = ['chlorophyll']
        if frequency.upper() == "DAY":
            productName = 'erdMH1chla1day'
        elif frequency.upper() == "WEEK":
            productName = 'erdMH1chla8day'
        elif frequency.upper() == "MONTH":
            productName = 'erdMH1chlamday'
        else:
            print("{}: wrong frequency".format(frequncy))
            sys.exit()
    elif sensor == "VIIRS":
        varNames = ['chlor_a']
        if frequency.upper() == "DAY":
            productName = 'nesdisVHNSQchlaDaily'
        elif frequency.upper() == "WEEK":
            productName = 'nesdisVHNSQchlaWeekly'
        elif frequency.upper() == "MONTH":
            productName = 'nesdisVHNSQchlaMonthly'
        else:
            print("{}: wrong frequency".format(frequncy))
            sys.exit()
    else:
        print("{}: Wrong sensor name ".format(sensor))
        sys.exit()

    serverURL = serverURL + productName + '.csv?'


    varNames_DHW = ['time',  'latitude', 'longitude']

    dateRange = makeDateRange(date_start, date_end)
    if sensor == 'MODIS':
        constrains = urllib.parse.quote(dateRange + makeRange(latitude) + makeRange(longitude))
    else:
        constrains = urllib.parse.quote(dateRange + '[(0.0):1:(0.0)]' + makeRange(latitude) + makeRange(longitude))
    varList = varNames[0] + constrains
    for var in varNames[1:]:
        varList = varList + "," + var + constrains
    url = serverURL + varList
    try:
        urllib.request.urlretrieve(url, fout)
    except:
        print("Failed")

    return print('Results written to {}'.format(fout))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Harvest CHL form MODIS/VIIRS sensors. The results are stored in a csv file')
    parser.add_argument('-sensor', dest='sensor', help='sensor type: MODIS or VIIRS', required=True)
    parser.add_argument('-frequency', dest='frequency', help='type of the aggregation: day, week, or month', required=True)
    parser.add_argument('-lat', dest='latitude', help='latitude in decimal degrees. Southern hemisphere negative', required=True)
    parser.add_argument('-lon', dest='longitude', help='longitude in decimal degrees. Western hemisphere negative', required=True)
    parser.add_argument('-from', dest='date_start', help='start date in yyyy-mm-dd', required=True)
    parser.add_argument('-to', dest='date_end', help='end date in yyyy-mm-dd', required=True)
    parser.add_argument('-fout', dest='fout', help='name of the output CSV file. Default CHLoutput.csv',
                        default='CHLoutput.csv', required=False)
    args = parser.parse_args()

    getCHL(args.sensor, args.frequency, args.latitude, args.longitude, args.date_start, args.date_end, args.fout)



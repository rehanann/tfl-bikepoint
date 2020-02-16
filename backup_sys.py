#!/usr/bin/env python3.7

import sys
import getopt
import requests
import json
import re
# import argparse
from geopy import distance


url = 'https://api.tfl.gov.uk/BikePoint/'

def tfl_connect():
    try:
        with open('token', 'r') as token:
            token = token.read()
    except:
        print('File not found')

    try:
        response = requests.get(url, headers={'Authorization': token})
        data = json.loads(response.text)
        return data
    except:
        print('Network or API connection is not either token is not valid or network is not working!')


def search_loc(*args):
        data =  tfl_connect()
       
        try:
            for name in args:
                search = name

                print("{0:<50} {1:20} {2:<10} {3:<15}".format('NAME','ID','LONGITUDE','LATITUDE'))
                for items in data:
                    item = (items['commonName'])
                    pattern_word = re.compile(rf"\b({search}.*)", flags=re.IGNORECASE)
                    match = re.match(pattern_word, item)
                    if match:
                        name = (items['commonName'])
                        id_name = (items['id'])
                        latitude = (items['lat'])
                        longitude = (items['lon'])
                        print("{0:<50} {1:20} {2:<10} {3:<15}".format(name, id_name, latitude, longitude))
        except:
            print('Please specify a search term!')
        
    

def search_radius(*args):
    data =  tfl_connect()
    
    for name in args:
        radius = name

    print("{0:<50} {1:20} {2:<10} {3:<15} {4:<10}".format('NAME','ID','LONGITUDE','LATITUDE','DISTANCE'))
    for items in data:  
        item_lat = str(items['lat'])
        item_lat = item_lat[0:5]
        item_lon = str(items['lon'])
        item_lon = item_lon[0:5]

        radius_lat = (radius[0])
        radius_lon = (radius[1])
        radius_met = (radius[2])
        if radius_lat == item_lat and radius_lon == item_lon:
            coords_1 = (radius_lat, radius_lon)
            coords_2 = (items['lat'], items['lon'])
            Ndistance = distance.geodesic(coords_1, coords_2).meters
            Ndistance = str(Ndistance)
            Ndistance = Ndistance[0:3]
            if radius_met <= Ndistance:
                return Ndistance

            name = (items['commonName'])
            id_name = (items['id'])
            latitude = (items['lat'])
            longitude = (items['lon'])
            print("{0:<50} {1:20} {2:<10} {3:<15} {4:<10}".format(name,id_name,latitude,longitude,Ndistance))
        


def search_bikepoint(*args):
        try:
            with open('token', 'r') as token:
                token = token.read()
        except:
            print('File not found')
        
        try:
            for name in args:
                bikepoint = name
            
            response = requests.get(url+bikepoint, headers={'Authorization': token})
            data = json.loads(response.content)
            items = data
            name = (items['commonName'])
            totalspaces = (items['additionalProperties'][7]['value'])
            emptyspaces = (items['additionalProperties'][6]['value'])
            latitude = (items['lat'])
            longitude = (items['lon'])
            print("{0:<50} {1:<20} {2:<20} {3:<20} {4:<25}".format('NAME','LATITUDE','LONGITUDE','EMPTY SPACE','TOTAL SPACE'))
            print("{0:<50} {1:<20} {2:<20} {3:<20} {4:<25}".format(name,latitude,longitude,emptyspaces,totalspaces))
        except:
            print('please provide the argument')



def display_usage():
    usage = "usage: bikepoint [-h] [-s SEARCH] [-r RADIUS [RADIUS ...]] [-b BIKEPOINT]"
    optional = "optional arguments:"
    phelp = " -h, --help"
    search = "-s SEARCH, --search SEARCH e.g: east, west, south, north"
    radius = "-r RADIUS [RADIUS ...], --radius RADIUS [RADIUS ...] e.g: 51.51 -0.12 1"
    bikepoint = "-b BIKEPOINT, --bikepoint BIKEPOINT e.g: BikePoints_50"
    print("{0}\n\n {1}\n {2}\n {3}\n {4}\n {5}".format(usage,optional,phelp,search,radius,bikepoint), sys.argv[0])

# usage = (print('myusage'))

def main():
    argv = sys.argv[1:]
    # print(argv)
    # print(argv[1], argv[2], argv[3])

    # try:
    #     opts, args = getopt.getopt(argv, "s:r,args:b")
    # except getopt.GetoptError as err:
    #     print(err)
    #     sys.exit(10)
  
    opts, args = getopt.getopt(argv, "s:r,args:b")

    # if len(opts) == 0:
    #     print('need argument')

    for opt, arg in opts:
        if opt in '-s':
            args = (argv[1])
            search_loc(args)
        elif opt in '-r':
            arg = (argv[1], argv[2], argv[3])
            args = arg
            # print(argv[1])
            # print(args)
            search_radius(args)
        elif opt in '-b':
            args = (argv[1])
            # print(args)
            search_bikepoint(args)

    if opt in '-s' and opt == argv[1] < 1:
        raise getopt.GetoptError("--config option is mandatory")

if __name__ == '__main__':
    main()

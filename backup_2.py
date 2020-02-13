#!/usr/bin/env python3.7

import sys
import requests
import json
import re
import argparse
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


def search_loc(args):
        data =  tfl_connect()
        try:
            search = args.search
        except:
            print('error 10')
        try:
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
        
    

def search_radius(args):
    data =  tfl_connect()
    radius = args.radius
    print(radius[0][3:])
    print(radius[1][3:])
    try:
        print("{0:<50} {1:20} {2:<10} {3:<15} {4:<10}".format('NAME','ID','LONGITUDE','LATITUDE','DISTANCE'))
        for items in data:  
            item_lat = str(items['lat'])
            item_lat = item_lat[0:5]
            item_lon = str(items['lon'])
            item_lon = item_lon[0:5]
            if radius[0] == item_lat and radius[1] == item_lon:
                coords_1 = (radius[0], radius[1])
                coords_2 = (items['lat'], items['lon'])
                Ndistance = distance.geodesic(coords_1, coords_2).meters
                Ndistance = str(Ndistance)
                Ndistance = Ndistance[0:3]
                if radius[2] <= Ndistance:
                    return Ndistance

                name = (items['commonName'])
                id_name = (items['id'])
                latitude = (items['lat'])
                longitude = (items['lon'])
                print("{0:<50} {1:20} {2:<10} {3:<15} {4:<10}".format(name,id_name,latitude,longitude,Ndistance))
    except:
        print('The search request is invalid!')
        


def search_bikepoint(args):
    bikepoint = args.bikepoint
    try:
        with open('token', 'r') as token:
            token = token.read()
    except:
        print('File not found')
    response = requests.get(url+bikepoint, headers={'Authorization': token})
    data = json.loads(response.content)
    items = data
    try:
        name = (items['commonName'])
        # id_name = (items['id'])
        totalspaces = (items['additionalProperties'][7]['value'])
        emptyspaces = (items['additionalProperties'][6]['value'])
        latitude = (items['lat'])
        longitude = (items['lon'])
        print("{0:<50} {1:<20} {2:<20} {3:<20} {4:<25}".format('NAME','LATITUDE','LONGITUDE','EMPTY SPACE','TOTAL SPACE'))
        print("{0:<50} {1:<20} {2:<20} {3:<20} {4:<25}".format(name,latitude,longitude,emptyspaces,totalspaces))
    except:
        print('please provide the argument')



def display_usage():
    usage = "Usage:"
    search = "londonbikes -s east | --search east "
    radius = "londonbikes -r | --radius <latitude> <longitude> <radius_in_metres>"
    bikepoint = "londonbikes --bikepoint <bike_point_id>"
    print("{0}\n {1}\n {2}\n {3}".format(usage,search,radius,bikepoint), sys.argv[0])

def main(argv):
    parser = argparse.ArgumentParser(prog='bikepoint')
    parser.add_argument('-s', '--search', type=str, help='e.g: east, west, south, north')
    parser.add_argument('-r', '--radius', default=False, type=str, nargs='+', help='e.g: 51.51 -0.12 1')
    parser.add_argument('-b', '--bikepoint', default=False, type=str, help='e.g: BikePoints_50')
    options = parser.parse_args(argv)

    params = {}

    if options.search:
        print(params['search']) 
        
        
    
if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))

# if args.search:
#     search_loc(args)
# elif args.radius:
#     search_radius(args)
# elif args.bikepoint:
#     search_bikepoint(args)
# else:
#     (display_usage())

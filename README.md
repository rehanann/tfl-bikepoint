# tfl-bikepoint

This script is using to search Bike points provided by TFL. This script allows 3 types of searches from command line, the details and types of searches provided in this document below:

To use this script first need to register on https://api.tfl.gov.uk, once registration completed obtain or generate the access token from the same site. Below details help you to obtain the token.

Register at the Transport for London Unified API website https://api.tfl.gov.uk and request access to the core datasets only. You will be given an Application ID and a key to access the TfL API. 

Download the bikepoint.py and create token file.

to use this script the system must have python 3.7 version installed.
download link Python 3.7 is here https://www.python.org/downloads/release/python-376/ :-

Searches option:-

usage: bikepoint [-h] [-s SEARCH] [-r RADIUS [RADIUS ...]] [-b BIKEPOINT]

optional arguments:
  -h, --help            show this help message and exit
  -s SEARCH, --search SEARCH
                        e.g: east, west, south, north
  -r RADIUS [RADIUS ...], --radius RADIUS [RADIUS ...]
                        e.g: 51.51 -0.12 240
  -b BIKEPOINT, --bikepoint BIKEPOINT
                        e.g: BikePoints_50

Search Result:

./bikepoint.py -s east

NAME                                               ID                   LONGITUDE  LATITUDE       
East Road, Hoxton                                  BikePoints_50        51.528673  -0.087459      
Eastbourne Mews, Paddington                        BikePoints_330       51.516417  -0.179135      
East Ferry Road, Cubitt Town                       BikePoints_455       51.49447   -0.014409      
East India DLR, Blackwall                          BikePoints_547       51.509474  -0.002275      
East Village, Queen Elizabeth Olympic Park         BikePoints_784       51.546326  -0.009935  

./bikepoint.py -r 51.52 -0.08 250

NAME                                               ID                   LONGITUDE  LATITUDE        DISTANCE  
Christopher Street, Liverpool Street               BikePoints_3         51.521283  -0.084605       350       
Fanshaw Street, Hoxton                             BikePoints_31        51.529537  -0.083353       108       
Leonard Circus , Shoreditch                        BikePoints_32        51.524696  -0.084439       606       
Pindar Street, Liverpool Street                    BikePoints_41        51.520955  -0.083493       264       
East Road, Hoxton                                  BikePoints_50        51.528673  -0.087459       109       
Old Street Station, St. Luke's                     BikePoints_73        51.525726  -0.088486       867       
Finsbury Square , Moorgate                         BikePoints_140       51.520962  -0.085634       405       
Baldwin Street, St. Luke's                         BikePoints_319       51.527025  -0.088542       980       
Clifton Street, Shoreditch                         BikePoints_323       51.523196  -0.083067       414       
Bunhill Row, Moorgate                              BikePoints_331       51.520858  -0.089887       692       
Hoxton Street, Hoxton                              BikePoints_588       51.52959   -0.0801         106     

./bikepoint.py -b BikePoints_51

NAME                                               ID                   EMPTY SPACE          TOTAL SPACE              
Finsbury Library , Finsbury                        BikePoints_51        12                   17       
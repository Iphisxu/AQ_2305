
# basic information
month   = 'May'
datadir = 'F:/Data/Project_anqing/'

# simulation data file
mcipfile    = datadir + month + '/' + month + '_met.nc'
cmaqfile    = datadir + month + '/' + month + '_chem.nc'
pa_O3file   = datadir + month + '/' + month + '_PA_O3-1.nc'
pa_NOxfile  = datadir + month + '/' + month + '_PA_NOx-1.nc'
isam_O3file = datadir + month + '/' + month + '_ISAM_O3-1.nc'
isam_PMfile = datadir + month + '/' + month + '_ISAM_PM-1.nc'

# observation data file
obsall = datadir + month + '/' + 'obsdata/allsite.xlsx'
obsurban = datadir + month + '/' + 'obsdata/urban.xlsx'

# shapefile
shpall   = datadir + 'shapefile/Anqing/Anqing.shp'
shpurban = datadir + 'shapefile/Anqing_urban/urban.shp'
shpmap   = datadir + 'shapefile/Anqing_district/anqing_district.shp'

# time range
timestart = '2023-05-01T00'
timeend   = '2023-05-31T23'


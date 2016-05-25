#! /usr/bin/env python

# Imports
import os, urllib, zipfile, pdb

# Parameters
years = range(2005,2016)

# Data directories.
d_dir = "data"
raw_dir = d_dir + "/raw"

# Log file.
logfile = raw_dir + "/raw_data.log"

# Retrosheet gamelog prefix.
retro_pref = "http://www.retrosheet.org/gamelogs/"

# Make data directories if they don't already exist.
if not os.path.isdir(d_dir):
    print "Creating directory " + d_dir + "."
    os.makedirs(d_dir)
if not os.path.isdir(raw_dir):
    print "Creating directory " + raw_dir + "."
    os.makedirs(raw_dir)

# Set up lists.
web_addr = [retro_pref + "gl" + str(yr_i) + ".zip" for yr_i in years]
zip_names = [raw_dir + "/gl" + str(yr_i) + ".zip" for yr_i in years]
raw_names = [raw_dir + "/GL" + str(yr_i) + ".TXT" for yr_i in years]

# Download files.
file_str = "" # string for writing to file.
for i in range(0,len(years)):
    if os.path.isfile(raw_names[i]):
        print "Raw data file " + raw_names[i] + " already exists."
    else:
        # Get data from web source.
        str1 = "Getting data from " + web_addr[i] + "."
        print str1; file_str += str1 + "\n"
        testf = urllib.URLopener()
        testf.retrieve(web_addr[i], zip_names[i])
        # Unzip files.
        str2 = "Unzipping " + zip_names[i] + " to " + raw_names[i] + "."
        print str2; file_str += str2 + "\n"
        zip_ref = zipfile.ZipFile(zip_names[i], 'r')
        zip_ref.extractall(raw_dir)
        zip_ref.close()
        # Remove zip file.
        str3 = "Removing zipfile " + zip_names[i] + "."
        print str3; file_str += str3 + "\n"
        os.remove(zip_names[i])

# If file_str is not empty, get date/time,
# attach to start of file_str, print to file.

        
# EOF

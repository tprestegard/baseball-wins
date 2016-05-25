#! /usr/bin/env python

# Imports
import os, urllib, zipfile, pdb

# Parameters
years = range(2005,2016)

# Data directories.
d_dir = "data"
raw_dir = d_dir + "/raw"

# Retrosheet gamelog prefix.
retro_pref = "http://www.retrosheet.org/gamelogs/"

# Make data directories if they don't already exist.
if not os.path.isdir(d_dir):
    os.makedirs(d_dir)
if not os.path.isdir(raw_dir):
    os.makedirs(raw_dir)

# Set up lists of files.
zip_names = ["gl" + yr_i + ".zip" for yr_i in years]

    
# Download files.
for yr_i in years:
    web_addr = retro_pref + str(yr_i) + ".zip"
    out_name = raw_dir + "/gl" + str(yr_i) + ".zip"
    if os.path.isfile(out_name):
        print "Raw data zipfile " + out_name + " already exists."
    else:
        print "Getting " + out_name + " from " + web_addr + "."
        testf = urllib.URLopener()
        testf.retrieve(web_addr, out_name)
        
# Unzip files.
z_list = os.listdir(raw_dir)
for file_i in z_list:
    # zipfile name
    zip_name = raw_dir + "/" + file_i
    # unzip name is based on experience with zipfile content
    unzip_name = d_dir + "/" + file_i[:-4].upper() + ".TXT"
    # we will rename the unzipped file.
    new_name = d_dir + "/" + file_i[:-4].lower() + ".txt"
    if os.path.isfile(unzip_name):
        print "File " + unzip_name + " already exists."
    else:
        if os.path.isfile(new_name):
            print "File " + new_name + " already exists."
        else:
            print "Unzipping " + zip_name + " to " + d_dir + "."
            zip_ref = zipfile.ZipFile(zip_name, 'r')
            zip_ref.extractall(d_dir)
            zip_ref.close()

    # Rename files.
    if os.path.isfile(unzip_name):
        print "Renaming file " + unzip_name + " to " + new_name + "."
        os.rename(unzip_name,new_name)


# EOF

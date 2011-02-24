# Filename: cp_2010_paperbq2b.py
# Name: Lee Hui Min
# Centre No / Index No: 3024 /
# Description: Read from RESOURCE.DAT, get extra info based on resource type, perform validation and write to URESOURCE.DAT

from classes import *

def UPDATERESOURCE():
    try:
        # open resource file for reading
        resource_file = open("RESOURCE.DAT","r")
        
        # open updated resource file for writing
        uresource_file = open("URESOURCE.DAT","w")
        
        # read heading line from resource file (creation date, number of records)
        heading_line = resource_file.readline()
        heading_line = heading_line.rstrip("\n")
            
        # store creation date and number of records
        creation_date = heading_line[0:10]
        num_recs = heading_line[10:]

        # write creation date and number of records to updated resource file
        uresource_file.write(creation_date + num_recs + "\n")

        # read remaining records details
        detail_lines = resource_file.readlines()

        # initialize resource list
        resource_list = []
        
        # loop for number of records
        for record_line in detail_lines:
            # clean record line
            record_line = record_line.rstrip("\n")

            # store resource number, title, date acquired, resource type
            resource_no = record_line[0:5]
            title = record_line[5:35]
            date_acquired = record_line[35:41]
            resource_type = record_line[41:]
            
            # print resource info
            print("Resource no: " + resource_no)
            print("Title: " + title)
            print("Date acquired: " + date_acquired)
            print("Resource type: " + resource_type)
            
            # if resource type is music CD
            if resource_type == "C":
                # get and validate artist
                valid_artist = False
                while not valid_artist:
                    artist = input("Enter artist: ")
                    if len(artist)== 0:
                        print ("Invalid! Empty input. Please try again.")
                    elif len(artist)>50:
                        print("Invalid! Exceed 50 characters. Please try again.")
                    else:
                        valid_artist = True
                
                # get and validate number of tracks
                valid_num_tracks = False
                while not valid_num_tracks:
                    num_tracks = input("Enter number of tracks:")
                    if len(num_tracks) == 0: # presence check
                        print("Invalid! Empty input. Please try again.")
                    elif not num_tracks.isdigit(): # data type check
                        print("Invalid! Must be a number. Please try again.")
##                  elif (int(num_tracks) < 0) or (int(num_tracks) > 20): # range check
                    elif not (0 < int(num_tracks) <= 20): # range check
                        print("Invalid! Must be between 1 and 20. Please try again.")
                    else:
                        valid_num_tracks = True
                # create new music CD object and add to resource list
                resource_list.append(MusicCD(resource_no, title, date_acquired, resource_type, artist, num_tracks.zfill(2)))

            print(resource_list)
            
            # else resource type is film DVD
            if resource_type == "D":
                # get and validate director
                valid_director = False
                while not valid_director:
                    director = input("Enter director:")
                    if len(director) == 0:
                        print ("Invalid! Empty input. Please try again.")
                    elif len(director)>50:
                        print("Invalid! Exceed 50 characters. Please try again.")
                    else:
                        valid_director = True
                    
                # get and validate running time
                valid_running_time = False
                while not valid_running_time:
                    running_time = input("Enter running time:")
                    if len(running_time) == 0:
                        print("Invalid! Empty input. Please try again.")
                    elif not running_time.isdigit():
                        print("Invalid! Must be a number. Please try again.")
                    elif not (30 <= int(running_time) <= 180):
                        print("Invalid! Must be between 30 to 180 minutes. Try again.")
                    else:
                        valid_running_time = True

                # create film DVD object and add to resource list
                resource_list.append(FilmDVD(resource_no, title, date_acquired, resource_type, director, running_time.zfill(3)))                                      
                
##        # write resource info and extra details to updated resource file
##        for resource in resource_list:
##            if resource.getResourceType() == "C":
##                uresource_file.write(resource.getResourceNo() + resource.getTitle() + resource.getDateAcquired() + \
##                                     resource.getResourceType() + resource.getArtist() + resource.getNoOfTracks() + \
##                                     "NULL (count to 50)    " + "000" + "\n")
##            else:
##                uresource_file.write(resource.getResourceNo() + resource.getTitle() + resource.getDateAcquired() + \
##                                     resource.getResourceType() + "NULL (count to 50)    " + "00" + \
##                                     resource.getDirector() + resource.getRunningTime() + "\n")

        # a better way
        for resource in resource_list:
            uresource_file.write(resource.display() + "\n")
            
        # close files
        resource_file.close()
        uresource_file.close()

    except IOError:
        # display file input/output errors
        print("Error! Cannot read from input file or write to output file.")
        # may not be able to write to output file if file is corrupted/locked/hard disk is full
        
# main
if __name__ == "__main__":
    UPDATERESOURCE()

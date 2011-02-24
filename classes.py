# Filename: cp_2010_paperbq2.py
# Name: Lee Hui Min
# Centre No / Index No: 3024 /
# Description: Supporting classes for resources, music cd and film dvd

# Superclass Resource
class Resource():

    ''' Resource class constructor'''
    def __init__(self, ResourceNo, Title, DateAcquired, ResourceType):
        self.__ResourceNo = ResourceNo# typing two _ in front of the variable makes it 'private' in python
        self.__Title = Title
        self.__DateAcquired = DateAcquired
        self.__ResourceType = ResourceType

    ''' Resource number accessor'''
    def getResourceNo(self):
        return self.__ResourceNo

    ''' Title accessor'''
    def getTitle(self):
        return self.__Title

    ''' Date Acquired accessor'''
    def getDateAcquired(self):
        return self.__DateAcquired

    ''' Resource type accessor'''
    def getResourceType(self):
        return self.__ResourceType

    ''' Title modifier'''
    def setTitle(self, newTitle):
        self.__Title = newTitle

    ''' Date Acquired modifier'''
    def setDateAcquired(self, newDateAcquired):
        self.__DateAcquired = newDateAcquired

    ''' Resource type modifier'''
    def setResourceType(self, newResourceType):
        self.__ResourceType = newResourceType

    ''' Helper function to display all data'''
    def display(self):
        return("{0:5s}{1:30s}{2:6s}{3:1s}".format\
               (self.__ResourceNo, self.__Title, self.__DateAcquired, self.__ResourceType))
    
    
# Subclass MusicCD
class MusicCD(Resource): # declare the parent class in the bracket

    ''' Music CD constructor '''
    def __init__(self, ResourceNo, Title, DateAcquired, ResourceType, Artist, NoOfTracks):
        super().__init__(ResourceNo, Title, DateAcquired, ResourceType)
        self.__Artist = Artist
        self.__NoOfTracks = NoOfTracks

    ''' Artist accessor'''
    def getArtist(self):
        return self.__Artist

    ''' NoOfTracks accessor'''
    def getNoOfTracks(self):
        return self.__NoOfTracks

    ''' Artist modifier'''
    def setArtist(self, newArtist):
        self.__Artist = newArtist

    ''' NoOfTracks modifier'''
    def setNoOfTracks(self, newNoOfTracks):
        self.__NoOfTracks = newNoOfTracks

    ''' Helper function to display all data'''
    def display(self):
        return("{0:42s}{1:50s}{2:2s}{3:50s}{4:3s}".format(super().display(),self.__Artist, self.__NoOfTracks,"NULL","000"))


# Subclass FilmDVD
class FilmDVD(Resource): 

    ''' Film DVD constructor '''
    def __init__(self, ResourceNo, Title, DateAcquired, ResourceType, Director, RunningTime):
        super().__init__(ResourceNo, Title, DateAcquired, ResourceType)
        self.__Director = Director
        self.__RunningTime = RunningTime

    ''' Director accessor'''
    def getDirector(self):
        return self.__Director

    ''' RunningTime accessor'''
    def getRunningTime(self):
        return self.__RunningTime

    ''' Director modifier'''
    def setDIrector(self, newDirector):
        self.__Director = newDirector

    ''' RunningTime modifier'''
    def setRunningTime(self, newRunningTime):
        self.__RunningTime = newRunningTime

    ''' Helper function to display all data'''
    def display(self):
        return("{0:42s}{1:50s}{2:2s}{3:50s}{4:3s}".format(super().display(),"NULL","00", self.__Director, self.__RunningTime))
    

##r1 = Resource("00001", "Best of Super Junior", "090911", "C")
##r2 = Resource("00002", "Super Show 3", "121210", "D")
##
##print(r1.getResourceNo())
##print(r1.display())
##
##r3 = Resource("00003","","","")
##r3.setTitle("Sorry Sorry")
##r3.setDateAcquired("080810")
##r3.setResourceType("C")
##print(r3.display())
##
##cd1 = MusicCD("00004","Bonamana","050510","C","Super Junior", 10)
##print(cd1.getResourceNo()) #inheritance
##print(cd1.display()) #overriding
##
### print(cd1.__Title) # Information Hiding: Error because data is private
##
##dvd1 = FilmDVD("00005","Full House","050508","D","Super Junior", 200)
##
###polymorphism --> different subclasses but still able to be displayed with respective information when together in a list
##res_list = []
##res_list.append(cd1)
##res_list.append(dvd1)
##
##for item in res_list:
##    print(item.display())


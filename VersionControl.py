import numpy as np

class VersionControl:

    def __init__(self, TG_Version):
        self.TG_Version=TG_Version

    def loadList(self, filename):
        # Die Dateiendung sollte .npy sein [Numpy]
        tempNumpyArray=np.load(filename)
        return tempNumpyArray.tolist()

    def safeList(self, myList, filename):
        np.save(filename, myList)

    def getRev(self):
        rev_old = self.loadList("rev_old_file.npy")  # Lädt die alte Revisionsnummer
        e = int(rev_old[0])
        c = e + 1
        rev_new = str(c)
        rev_old = [rev_new]
        print(f"Version " + self.TG_Version + "(Rev." + rev_new + ")")
        self.safeList(rev_old, "rev_old_file") #Speichert die Revisionsnummer

    def useRev(self):
        rev_old = self.loadList("rev_old_file.npy")   # Lädt die alte Revisionsnummer
        return rev_old[0]

    def releaseRev(self):
        rev_old = self.loadList("rev_old_file.npy")  # Lädt die alte Revisionsnummer
        e = int(rev_old[0])
        c = e
        rev_new = str(c)
        rev_old = [rev_new]
        TG_Version = "(Release): " + self.TG_Version
        print(f"Version " + TG_Version + "(Rev." + rev_new + ")")
    
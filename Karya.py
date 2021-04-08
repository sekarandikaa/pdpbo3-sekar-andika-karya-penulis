class Karya():
    def __init__(self, jenis, jmlPenghargaan):
        self.jenis = jenis
        self.jmlPenghargaan = jmlPenghargaan
    
    def getJenis(self):
        return self.jenis

    def getJmlPenghargaan(self):
        return self.jmlPenghargaan
    
    def getDetailKarya(self):
        pass

    def getInfoKarya(self):
        return "Karya " + self.jenis + "yang mendapatkan " + self.jmlPenghagaan + "penghargaan, saat karya dirilis hingga saat ini"

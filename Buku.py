from Karya import Karya

class Buku(Karya):
    def __init__(self, penulis, jkPenulis, judul, tahunRilis, genre, bestSeller, jmlPenghargaan):
        super().__init__("Buku", jmlPenghargaan)
        self.penulis = penulis
        self.jkPenulis = jkPenulis
        self.judul = judul
        self.tahunRilis = tahunRilis
        self.genre = genre
        self.bestSeller = bestSeller

    def getPenulis(self):
        return self.penulis
    
    def getJkPenulis(self):
        return self.jkPenulis

    def getJudul(self):
        return self.judul

    def getTahunRilis(self):
        return self.tahunRilis
    
    def getGenre(self):
        return self.genre
    
    def getBestSeller(self):
        return self.bestSeller

    def getDetailKarya(self):
        return "Buku ini ditulis oleh penulis " + self.jkPenulis + "berbakat, "
        + self.penulis + "pada tahun " + self.tahunRilis  
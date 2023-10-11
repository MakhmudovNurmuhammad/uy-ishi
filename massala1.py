class chiptachi:
    mal_ = {}   
    d = 0
    ch = {}
    def __init__(self,ism,yosh) -> None:
        self.ism = ism
        self.yosh = yosh
        chiptachi.d+=1

    def sot(self,obj,chip):
        chiptachi.mal_[chiptachi.d] = {"ismi" : obj.ism, "yosh": obj.yosh,"uchadi" : chip.qayerdan,"qonadi" : chip.qayerga,"soat":chip.soat,"chipta_narxi" : chip.narx}
    def mal(self):
        for i,j in chiptachi.mal_.items():
            print(f"""
ID: {i}
MALUMOTLAR: {j}
""")
    def ch_(self):
        for i,j in chiptachi.ch.items():
            print(f"""
{i} shahridan uchadi :)
{j}""")

class xaridor:
    def __init__(self,ism,yosh) -> None:
        self.ism = ism
        self.yosh = yosh

class chipta:
    def __init__(self,qayerdan,qayerga,soat,narx) -> None:
        self.qayerdan = qayerdan
        self.qayerga = qayerga
        self.soat = soat
        self.narx = narx
        chiptachi.ch[qayerdan] = {"qonadi":qayerga,"soat":soat,"narxi": narx}
ch1 = chipta("LONDON","AMERIKA","01:30",2300)
ch2 = chipta("FRANSIYA","YOPONIYA","12:10",1500)
ch3 = chipta("TOSHKENT","RUSSIA","00:10",900)
ch4 = chipta("KOREA","AFRIKA","09:45",2900)
ch5 = chipta("SAMARQAND","TOSHKENT","17:00",120)
ch6 = chipta("LOS-ANGELAS","NEW YORK","18:15",1100)
ch7 = chipta("AVG'ONISTON","ERON","19:30",300)
ch8 = chipta("PORTUGALIYA","BRAZIL","21:00",2000)
ch9 = chipta("ITALY","UZBEK","01:30",1900)
ch10 = chipta("GERMANY","FRANSIYA","01:30",1200)
chipta_ = [ch1,ch2,ch3,ch4,ch5,ch6,ch7,ch8,ch9,ch10]
c1 = chiptachi("akrom",35)
while True:
    s = int(input("[1] - chiptalar malumoti\n[2] - chipta sotish\n[3] - chipta sotib olganlar malumoti\n[4] - EXIT\n>>> "))
    if s==1:
        c1.ch_()
    elif s==2:
        f = xaridor(input("ismni kiriting: "),int(input("yoshni kiriting: ")))
        f1 = chipta(input("qayerdan uchadi: "),input("qayerga qonadi: "),input("soat nechida: "),int(input("nerxini kiriting: ")))
        c1.sot(f,f1)
    elif s==3:
        c1.mal()
    elif s==4:
        exit()

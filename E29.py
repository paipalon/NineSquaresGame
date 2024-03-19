import random

def aloittaja():
    luku = random.randint(1,2)
    if luku == 1:
        return "X"
    else:
        return "Y"
def vaihda(pelaaja):
    if pelaaja == "X":
        return "Y"
    else:
        return "X"
    
def piirra_rivi(peli,ind):
    #print(f"Piirretään rivi {ind+1}")
    lisays = ""
    rivi = peli[ind]
    for i in range(0,3):
        lisays += (f"{rivi[i] }")
    print(lisays)       
    
def tarkasta_sopivuus(syote):
    sopii = False
    if syote.isnumeric() and int(syote)>0 and int(syote)<4 :
              sopii = True
    return sopii

def vaakasuoraan(p, r1, r2, r3):
    vaakasuoraan = False
    if((r1[0]==p and r1[1]==p and r1[2]==p) or
       (r2[0]==p and r2[1]==p and r2[2]==p) or
       (r3[0]==p and r3[1]==p and r3[2]==p)):
        return True
    
def pystysuoraan(p, r1, r2, r3):
    pystysuoraan = False
    for i in range(0,3):
        if r1[i]==p and r2[i]==p and r3[i]==p:
            return True

def vinosti(p, r1, r2, r3):
    vinosti = False
    if((r1[0]==p and r2[1]==p and r3[2]==p) or
       (r1[2]==p and r2[1]==p and r3[0]==p)):
        return True
    
def voittiko(peli,pelaaja):
    voittiko = False
    rivi_1 = peli[0]
    rivi_2 = peli[1]
    rivi_3 = peli[2]
    if vaakasuoraan(pelaaja,rivi_1, rivi_2, rivi_3):
        voittiko = True
    elif pystysuoraan(pelaaja,rivi_1, rivi_2, rivi_3):
        voittiko = True
    elif vinosti(pelaaja,rivi_1, rivi_2, rivi_3):
        voittiko = True
    return(voittiko)
    
def main():
    peli = [[0,0,0], [0,0,0], [0,0,0]]
    koko = 3
    maksimi = koko * koko
    pelaaja = aloittaja()
    voitto = False
    voittaja = ""
    for vuoro in range(1, maksimi+1):
        if not voitto:
            #Testataan, että syötteet annetaan oikein, ja ruutu on vapaa
            vapaa_ruutu = False
            while not vapaa_ruutu:
                sopiva_r = False
                while not sopiva_r:
                    rivi = input(pelaaja + " Anna rivi 1-3: ")
                    sopiva_r = tarkasta_sopivuus(rivi)
                    if not sopiva_r:
                        print("Rivin pitää olla 1, 2 tai 3")
                sopiva_s = False
                while not sopiva_s:
                    sarake = input(pelaaja + " Anna sarake 1-3: ")
                    sopiva_s = tarkasta_sopivuus(sarake)
                    if not sopiva_s:
                        print("Sarakkeen pitää olla 1, 2 tai 3")
                print()

                rivi = int(rivi)
                sarake = int(sarake)
        
                pelinrivi = peli[rivi-1]
        
                if pelinrivi[sarake-1] == 0:
                    pelinrivi[sarake-1] = pelaaja
                    print(f"Lisätty {pelaaja} rivin {rivi} sarakkeeseen {sarake}")
                    print()
                    vapaa_ruutu = True
                    
                    for i in range(0,3):
                        piirra_rivi(peli,i)
                    print()
                        
                    if pelaaja == "X":
                        pelaaja = "Y"
                    else:
                        pelaaja = "X"
                else:
                    print("Valitsemasi ruutu on jo varattu")      
        
                #Pelaajan merkki on lisätty vapaaseen ruutuun
            
                if vuoro > 4:
                    if voittiko(peli, "X"):
                        voittaja = "X"
                        voitto = True
                    else:
                        if voittiko(peli, "Y"):
                            voittaja = "Y"
                            voitto = True
                if voitto:
                    print(f"{voittaja} on voittanut pelin. Onnittelut!")
                
        
    if not voitto:
            print("Kumpikaan ei voittanut tällä kertaa")
main()       

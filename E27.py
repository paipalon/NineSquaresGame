def main():
    peli = [[0,0,0], [0,0,0], [0,0,0]]
    pelaaja = "X"
    for vuoro in range(1,10):
        oikein = False
        while not oikein:
            sijainti = input(pelaaja + " Anna sijainti muodossa rivi, sarake: ")
            sijainti = sijainti.split(", ")
            rivi = sijainti[0]
            rivi = int(rivi)
            sarake = sijainti[1]
            sarake = int(sarake)
            #print("Annoit sijainnin rivi " + str(rivi) + " ja sarake " +
            #str(sarake))
        
            pelinrivi = peli[rivi-1]
        
            if pelinrivi[sarake-1] == 0:
                pelinrivi[sarake-1] = pelaaja
                oikein = True
            else:
                oikein = False
                print("Valitsemasi ruutu on jo varattu")
                
        
        for i in range(0,3):
            print(peli[i])
            
        if pelaaja == "X":
            pelaaja = "Y"
        else:
            pelaaja = "X"
        
main()

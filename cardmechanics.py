def nimmHandKarten(self, anzahl, Kartenstapel):
    for x in range(anzahl):
        self.handKarten.append(Kartenstapel.spielKarten.pop())
def contarPalabras(Palabrastxt):
    archivo = open(Palabrastxt, 'r')
    palabras = {}
    for linea in archivo:
        palabras[linea.strip()] = []
    print('Lista de palabras:\n', palabras)
    archivo.close()

def contarFrases(palabras, Frasestxt):
    archivo = open(Frasestxt, 'r')
    frases = {}
    for frase in archivo:
        frases.append(frase.strip())
        for palabra in palabras:
            palabras[palabra].append()(frase.lower().count(palabra))
    archivo.close()


class FindPal:
    def _init_(self, Palabrastxt, Frasestxt):
        self.Palabrastxt = Palabrastxt
        self.Frasestxt = Frasestxt

        self.palabras = contarPalabras(Palabrastxt)
        self.frases = contarFrases(self.palabras, Frasestxt)

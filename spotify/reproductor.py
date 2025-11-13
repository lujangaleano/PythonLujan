from pygame import mixer
class Reproductor:
    archivo = None
    def __init__(self):
        self.archivo = "wefere.mp3"
        mixer.init()
        mixer.music.load(self.archivo)

    def reproducir(self):
        mixer.music.play()

    def pausar(self):
        if mixer.music.get_busy():
            mixer.music.pause()
        else:
            mixer.music.unpause()
            
    def subirVolumen(self):
        pass
import pygame

class Audio:
    def __init__(self, playlist):
        pygame.mixer.init()
        pygame.mixer.quit() 
        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=8192)
        self.playlist = playlist
        self.musica_atual = 0
        self.end_music = pygame.USEREVENT + 1
        pygame.mixer.music.set_endevent(self.end_music)

    def iniciar_musica(self):
        pygame.mixer.music.load(self.playlist[self.musica_atual])
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()

    def proxima_musica(self):
        self.musica_atual = (self.musica_atual + 1) % len(self.playlist)
        pygame.mixer.music.load(self.playlist[self.musica_atual])
        pygame.mixer.music.play()

    def gerencia_musicas(self, event):
        if event.type == self.end_music:
            self.proxima_musica()

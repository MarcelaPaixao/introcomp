import pygame

class Audio:
    def __init__(self, playlist, win_sound, lose_sound):
        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=8192)
        
        self.playlist = playlist
        self.musica_atual = 0
        self.end_music = pygame.USEREVENT + 1
        pygame.mixer.music.set_endevent(self.end_music)
        
        self.win_sound = win_sound
        self.lose_sound = lose_sound

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

    def tocar_win_sound(self):
        pygame.mixer.music.stop()  # Para a música atual
        som = pygame.mixer.Sound(self.win_sound)
        som.play()

    def tocar_lose_sound(self):
        pygame.mixer.music.stop()  # Para a música atual
        som = pygame.mixer.Sound(self.lose_sound)
        som.play()

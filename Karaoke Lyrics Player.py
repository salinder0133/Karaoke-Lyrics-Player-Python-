import pygame
import time
import sys
import threading

# 🎵 Music play karne wali function
def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("song.wav")  # 👈 Make sure this is a WAV file
    pygame.mixer.music.play()

# 📝 Lyrics dikhane wali function
def show_lyrics():
    lyrics = [
        "Hey, kaash kaash yoon hota har shaam saath tu hota..",
        "Chupchap dil na yoon rota har shaam saath tu hota..",
        "Guzaar ho tere bin guzaara ab mushkil hai lagta..",
        "Nazaara ho tera hi nazaara ab har din hai lagta..."
    ]

    # Har line ke baad kitni der rukna hai (seconds mein)
    delays = [2.0, 2.0, 2.0, 2.5]

    print("\nHale Dil.... 🎤\n")
    time.sleep(2)  # Starting pause

    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.18)  # 👈 Character-by-character delay (slower now)
        print()
        time.sleep(delays[i])  # 👈 Line ke baad pause

# 🔁 Program start point
if __name__ == "__main__":
    # Music thread start
    t = threading.Thread(target=play_music)
    t.start()

    # Lyrics show karo
    show_lyrics()

    # Wait for music thread to finish
    t.join()

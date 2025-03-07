import pygame
import os

def play_music(file):
    pygame.mixer.init()
    
    if not os.path.exists(file):
        print(f"Erro: O arquivo '{file}' não foi encontrado.")
        return

    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    print("🎵 Tocando música...")

def pause_music():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
        print("⏸ Música pausada.")
    else:
        print("⚠ Nenhuma música está tocando.")

def unpause_music():
    pygame.mixer.music.unpause()
    print("▶ Música retomada.")

def main():
    file = "Like Him.mp3"  
    play_music(file)
    
    while True:
        comando = input("\nDigite 'p' para pausar, 'r' para retomar, 's' para sair: ").strip().lower()
        
        if comando == 'p':
            pause_music()
        elif comando == 'r':
            unpause_music()
        elif comando == 's':
            pygame.mixer.music.stop()
            print("🛑 Música parada. Saindo do programa.")
            break
        else:
            print("❌ Comando inválido! Use 'p' para pausar, 'r' para retomar ou 's' para sair.")

if __name__ == "__main__":
    main()

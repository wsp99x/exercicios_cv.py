# exercicios_cv.py

Exercícios do Curso de Python Básico - Curso em Vídeo

Este repositório contém minha resolução dos exercícios do Curso de Python Básico oferecido gratuitamente pelo Curso em Vídeo e ministrado pelo professor Gustavo Guanabara.

📚 Sobre o Curso

O curso de Python Básico do Curso em Vídeo é uma excelente introdução ao mundo da programação. Ele cobre desde conceitos fundamentais até estruturas de controle e manipulação de dados.

🔍 Tópicos Abordados

Introdução ao Python

Variáveis e Tipos de Dados

Operadores e Expressões

Estruturas Condicionais (if, else, elif)

Laços de Repetição (for, while)

Funções e Modularização

Listas e Tuplas

Manipulação de Strings

📝 Estrutura do Repositório

Cada arquivo Python (".py") corresponde a um exercício resolvido. Eles estão organizados conforme os módulos do curso:

/exercicios_cv.py/
/aulas/
│-- aula006.py
│-- aula007.py
│-- aula008.py
/execícios/
│-- ex001.py
│-- ex002.py
│-- ex003.py
│-- ex004.py
│-- ex005.py
│-- ex006.py
│-- ex007.py
│-- ex008.py
│-- ex009.py
│-- ex010.py
│-- ex011.py
│-- ex012.py
│-- ex013.py
│-- ex014.py
│-- ex015.py
│-- ex016.py
│-- ex017.py
│-- ex018.py
│-- ex019.py
│-- ex020.py
│-- ex021.py
│-- ---


🎵 Exercício Mais Complexo

O código mais avançado até agora é um player de música utilizando a biblioteca pygame. Ele permite tocar, pausar e retomar um arquivo de áudio via comandos do usuário. Veja abaixo um exemplo:
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

🚀 Como Utilizar

Clone este repositório para seu computador:

git clone https://github.com/wsp99x/exercicios_cv.py.git

Acesse a pasta do repositório:

cd nome-do-repositorio

Execute os códigos Python:

python3 nome_do_arquivo.py

💪 Contribuição

Se desejar sugerir melhorias ou compartilhar soluções alternativas, fique à vontade para abrir um Pull Request! Toda colaboração é bem-vinda. 😊

💌 Contato

Caso tenha dúvidas ou queira trocar ideias, me encontre no LinkedIn ou pelo meu GitHub:

LinkedIn
www.linkedin.com/in/wellingtonsp-dev

GitHub
www.github.com/wsp99x

Feito com ❤️ e muito código! 💻
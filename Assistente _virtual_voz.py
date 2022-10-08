print("Testando...")

import speech_recognition as sr  # Biblioteca que esta rodando a deeplearning dentro

import os  # Biblioteca que faz a comunição com nossa maquina


#Função para ouvir e reconhecer a fala
def ouvir_microfone():
    #Habilita o microfone do usuário
    microfone = sr.Recognizer()
    
    #usando o microfone
    with sr.Microphone() as source:
        
        #Chama um algoritmo de reducão de ruídos no som
        microfone.adjust_for_ambient_noise(source)
        
        #Frase para o usuario dizer algo
        print("Diga alguma coisa: ")
        
        #Armazena o que foi dito numa variável
        audio = microfone.listen(source)
        
    try:
        
        #Passa a variável para o algoritmo reconhecedor de padrões
        frase = microfone.recognize_google(audio,language='pt-BR')

        if "navegador" in frase:
            os.system("start Chrome.exe")

        elif "Excel" in frase:
            os.system("start Excel.exe")

        
        #Retorna a frase pronunciada
        print("Você disse: " + frase)
        
    #Se não reconhecer o padrão de fala, exibe a mensagem
    except sr.UnkownValueError:
        print("Não foi possível compreender!")
        
    return frase

ouvir_microfone()

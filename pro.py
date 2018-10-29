from selenium import webdriver
import time

#mensagem
msg = 'testando multi-numeros'
#lista de numeros
num = ['', '', '', '']

#Os times são necessarios pra poder da o tempo necessario pra cada funcção

driver = webdriver.Chrome()

#vai abrir o whatsapp web pra autenticar o QR
driver.get('https://web.whatsapp.com')

#for de acordo com a quantidade de numeros da lista
for i in range(len(num)):
    time.sleep(8)
    #abre a url da api de acordo com o numero do for
    driver.get('https://api.whatsapp.com/send?phone='+num[i])
    
    #clica no btn iniciar conversa
    btnIniciar = driver.find_element_by_class_name('button')
    btnIniciar.click()
    
    time.sleep(15)
    
    #entrar no campo da msgm e digita
    mensagem = driver.find_element_by_class_name('_2S1VP')
    mensagem.send_keys(msg)
    time.sleep(5)
    #aperta o btn enviar
    btnEnviar = driver.find_element_by_class_name('_35EW6')
    btnEnviar.click()


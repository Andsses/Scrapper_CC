import re

# Esta Funcion obtiene los numeros que hay en un mensaje y los guarda en una lista

def getcards(text):
    text = text.replace('\n', ' ').replace('\r', '')
    # ` quitar comillas
    text = text.replace('`', '')
    card = re.findall(r"[0-9]+", text)

    if "KEYWORD CHANNEL ONE TO SCRAPP" in text or "@CHANNEL_NAME_TO_SCRAP":
        if len(card[3]) == 2:
            card[3] = "20" + card[4]
        cc = card[1] 
        mes = card[2]
        ano = card[3]
        cvv = card[4]
        card = [cc, mes, ano, cvv]
        return cc, mes, ano, cvv


    if "KEYWORD CHANNEL TWO TO SCRAPP" in text or "KEYWORD CHANNEL TWO TO SCRAPP" in text or "KEYWORD CHANNEL TWO TO SCRAPP" in text or "KEYWORD CHANNEL TWO TO SCRAPP" in text:
        if len(card[4]) == 2:
            card[4] = "20" + card[4]
        cc = card[2]
        mes = card[3]
        ano = card[4]
        cvv = card[5]
        card = [cc,mes,ano,cvv]
        print(card)
        return cc,mes,ano,cvv
    
    try:
        card = card[0] , cc1_mes , card[2] , cc1_vvv
        getcards2(card)
        return
    except Exception as e:
        print("error aqui: ", e)
        return
        
    
    
# otro metodo para obtener el card , date, cvv del mensaje 
def getcards2(card):
    if len(card) == 3:
        cc = card[0]
        if len(card[1]) == 3:
            mes = card[2][:2]
            ano = card[2][2:]
            cvv = card[1]
        else:
            mes = card[1][:2]
            ano = card[1][2:]
            cvv = card[2]
    else:
        cc = card[0]
        if len(card[1]) == 3:
            mes = card[2]
            ano = card[3]
            cvv = card[1]
        else:
            mes = card[1]
            ano = card[2]
            cvv = card[3]
    if len(ano) not in [2,4] or len(ano) == 2 and ano < '21' or len(ano)  == 4 and ano < '2021' or len(ano) == 2 and ano > '29' or len(ano)  == 4 and ano > '2037':
        print("Fallo al obtener el año")
        return
    if cc[0] == 3 and len(cvv) != 4 or len(cvv) != 3:
        print("Fallo al obtener el cvv")
        return
    
    return cc,mes,ano,cvv
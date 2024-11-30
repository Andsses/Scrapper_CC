from telethon.sync import TelegramClient
from telethon import events
from funcions import getcards
import os


# Inserta aquí tus credenciales de API de Telegram
api_id = 6666666 # Example : 11670008
api_hash = 'YOUR HASH' # Example : 33a51w803x0f8e9e025b9ca515e1fa1f

scarscapper = "@CHANNEL_SCRAPE_NORMAL"
vipscrapper = "@CHANNEL_SCRAPE_VIP"

chats  = [
    '@CHANNEL_SCRAPE',
    '@CHANNEL_SCRAPE',
] 


global is_active

is_active = True

# Crea una instancia del cliente de Telegram
with TelegramClient('session_name', api_id, api_hash) as client:
    # Función para procesar los mensajes entrantes
    @client.on(events.NewMessage(chats))  # Cambia el ID o nombre del chat o canal según tu caso
    async def handle_message(event):
        global cc, mes, ano, cvv
        
        if is_active == False:return

        cards = getcards(event.message.text)

        if cards is None :print("No se encontraron tarjetas  ", cards);return

        try:
            cc,mes,ano,cvv = cards
        except Exception as e:
            print("error: ", e)
            return

        if len(ano) == 2:ano = '20' + ano

        # Intentar leer del archivo CSV
        try:
            with open('binsList/ranges.csv', mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['number'] == cc[:6]:
                        scheme = row['vendor'].upper()
                        types = row['type'].upper()
                        brand = row['level'].upper()
                        bank_name = row['bank_name'].upper()
                        country = row['country'].upper()
                        emoji = row['flag']
                        
                print("No se encontraron datos en el archivo CSV para este BIN.")
        except FileNotFoundError:
            print("Archivo CSV no encontrado.")
        
        tuple_as_strings = [str(element) for element in cards]
        result_string = "|".join(tuple_as_strings)
        # obtener ruta de archivo
        path = os.path.dirname(os.path.abspath(__file__))
        # Crear si no existe el archivo card.txt y escribir en el junto con el path
        with open(f"{path}/cards.txt", "a") as f:
            f.write(result_string + "\n")
            f.close()

        text = f"""
\n
<b>Scrapper By: @ScrapperScar\n
<b>CARD :</b> <code>{cc}|{mes}|{ano}|{cvv}</code>\n
<b>INFO:</b> <i>{scheme} - {types} - {brand}</i>\n
<b>BIN:</b> <a href="https://t.me/ScrapperScar"><code>{cc[:6]}</code></a>\n
<b>BANK:</b> {bank_name} \n
<b>COUNTRY:</b> {country} - {emoji}\n
╔══════════ Extra ═════════╗
╠ <code>{cc[:12]}xxxx|{mes}|{ano}|xxx</code>
╚═══════════════════════╝
\n
""" 
        await client.send_message(scarscapper, text, parse_mode='html')

        
            
        return



    # Iniciar el bucle de eventos
    client.run_until_disconnected()

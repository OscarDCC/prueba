import telegram

def obtener_chat_id(token):
    bot = telegram.Bot(token=token)
    updates = bot.get_updates()
    chat_id = updates[-1].message.chat_id
    return chat_id

def main():
    token = '6270327278:AAHuCxz_IytVmqTluRs_8oj_GEWZM9tupNw'
    chat_id = obtener_chat_id(token)
    print(f"El ID del chat es: {chat_id}")

if __name__ == '__main__':
    main()


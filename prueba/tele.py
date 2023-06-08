import requests

msj = "Aqui se enviará el archivo"
token = '6265034611:AAH8w71HcgHJMNondPO89RulH701wrM7uUE'
chat_id = '1397290398'
url = f"https://api.telegram.org/bot{token}/sendMessage"



response = requests.post(url, data={'chat_id': chat_id, 'text': msj})


if response.status_code == 200:
    print("Mensaje enviado")
else:
    print("Error al enviar el mensaje:", response.text)


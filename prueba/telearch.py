import requests

token = '6265034611:AAH8w71HcgHJMNondPO89RulH701wrM7uUE'
chat_id = '1397290398'
url = f"https://api.telegram.org/bot{token}/sendDocument"

file_path = '/home/jetson/prueba/Asistencia.xlsx'  # Ruta completa del archivo que deseas enviar

data = {'chat_id': chat_id}
files = {'document': open(file_path, 'rb')}

response = requests.post(url, data=data, files=files)

if response.status_code == 200:
    print("Archivo enviado")
else:
    print("Error al enviar el archivo:", response.text)


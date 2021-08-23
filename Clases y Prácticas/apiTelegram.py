import requests as req


def main():
	#imagen = { "photo": open("semana16/logo_id.png", "rb") }

	URL_TELEGRAM = "https://api.telegram.org/bot"
	TOKEN = "1973714579:AAG3CP2ukyX2nYgToC5VCw-E5p7AXnF7Vvg"
	ENDPOINT = "sendMessage"
	ID_CHAT = "-520657802"
	TEXTO = "Hola. Estoy probando"
	URL_MENSAJE = f"{URL_TELEGRAM}{TOKEN}/{ENDPOINT}?chat_id={ID_CHAT}&text={TEXTO}"
	consulta = req.get (URL_MENSAJE)
	if (consulta.status_code == 200):
		print("Mensaje enviado")
	else:
		print("ERROR al enviar mensaje")


if (__name__ == "__main__"):
	main()
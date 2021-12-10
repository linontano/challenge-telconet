import requests
import schedule
def sendResponse(data):
    base = "https://api.telegram.org/bot{token}/sendMessage"
    tokenBot = "5059561599:AAFKrUt03mEhpgSDt8sevEFdaIfjggZAs3M"
    chatId = '@telcochallenge'
    requests.post(base.format(token=tokenBot),
    data={'chat_id' : chatId, 'text': data})

def getBgp(network):
    BASE = "http://127.0.0.1:5000/"
    response = requests.get(BASE + "api/routes/{net}".format(net=network))
    if response.status_code == 200:
        date = response.json()['TIME'] 
        headerText = "Rutas BGP de la red "+ network+" actualizado el: "+date+"\n"
        _response = response.json()['OUTPUT'].split('\n')
        return headerText+"\n".join(_response[2:len(_response)-2])
    if response.status_code == 400:
        return "Ha ingresado una red incorrecta."
    if response.status_code == 404:
        return "La red ingresada no está registrada."
    return "Ha ocurrido un problema, intenta nuevamente más luego."

def botAction():
    network = "216.218.252.28"
    api = getBgp(network)
    sendResponse(api)

print('Bot running...')
botAction()
schedule.every().day.at("07:30").do(botAction)
while True:
    schedule.run_pending()
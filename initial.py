import sys
from slack import WebClient
from slack.errors import SlackApiError

def call_slack_ssh():

    #pegando os inputs e jogando nas variaveis para envio para o slack
    mensagem = sys.argv[1]
    cliente = sys.argv[2]
    channel_cliente = ''

    client = WebClient(token='#')

    lista_canal = [
        'channel'
    ]

    #um laco para varrer a lista de canal e colocar na variavel
    for l in lista_canal:
        if(l == cliente.lower()):
            channel_cliente_mod = '#{}'.format(l)
            channel_cliente = channel_cliente_mod

    try:
        response = client.chat_postMessage(

        str_format = 'Em seu ambiente foi idenficado um evento de {}'.format(mensagem)

            channel=channel_cliente_mod,
            blocks = [
		{
			"type": "image",
			"title": {
				"type": "plain_text",
				"text": "#",
				"emoji": True
			},
			"image_url": "#logo",
			"alt_text": "#"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": str_format
			}
		},
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "Escolha uma das opções abaixo para tratar este evento em seu ambiente:",
				"emoji": True
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Receber um e-mail com mais informações sobre o evento. "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Me envie um e-mail",
					"emoji": True
				},
				"value": "click_me_123"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Nossa inteligencia realizará o isolamento imediato do host indicado para que seja realizado a devida intervençaõ pela equipe interna. "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Isole este Host",
					"emoji": True
				},
				"value": "click_me_123"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Se preferir podemos remover esse evento das notificações. "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Não me notifique mais",
					"emoji": True
				},
				"value": "click_me_123"
			}
		}
	]

        )

    except SlackApiError as e:
        print(e.response["error"])

call_slack_ssh()

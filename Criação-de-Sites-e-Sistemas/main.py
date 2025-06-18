# Titulo: Hash Zap
# Botão de iniciar Chat
    # Popup (janela na frente da tela)
    # Bem vindo ao Zap Zap
    # Campo de teste -> Escreva seu nome no chat
    # Botão de Entrar no chat
        # Sumir com o titulo Zap Zap
        # Fechar a janela (popup)
        # Carregar o chat
            # As mensagens que já foram enviadas
            # Campo: Digite sua mensagens
            # Botão de enviar
# pip install flet

# importar o flet
import flet as ft

# Criar a função principal do app 
def main(page):
    # Criar todas as funcionalidades
    # Cria o elemento
    # Adiciona  na página

    title_window = ft.Text("Zap Zap")

    title_popup = ft.Text("Bem vindo ao Zap Zap")
    user_name_field = ft.TextField(label="Escreva seu nome no chat")


    chat = ft.Column()

    def messae_channel_comun(message):
        chat_content = ft.Text(message)
        chat.controls.append(chat_content)
        page.update()
        
    page.pubsub.subscribe(messae_channel_comun)

    def send_message(event):
        message_field.value
        message_content = message_field.value
        user_name = user_name_field.value
        message  = f"{user_name}: {message_content}"

        page.pubsub.send_all(message)


        message_field.value = ""
        page.update()

    send_message_button = ft.ElevatedButton("Enviar", on_click = send_message)
    message_field = ft.TextField(label="Escreva sua mensagem", on_submit = send_message)
    div_message = ft.Row([message_field, send_message_button])

    def join_chat(event):
        page.remove(title_window)
        page.remove(button_start)
        popup.open = False
        page.add(chat)
        page.add(div_message)
        message = f"{user_name_field.value} entrou no chat"
        page.pubsub.send_all(message)
        page.update()


    button_join_chat = ft.ElevatedButton("Entrar no Chat", on_click = join_chat)

    popup = ft.AlertDialog(
        title = title_popup, 
        content = user_name_field,
        actions = [button_join_chat]
        )

    def start_chat(event):
        page.dialog = popup
        popup.open = True
        page.update()

    button_start = ft.ElevatedButton("Iniciar Chat", on_click = start_chat)

    page.add(title_window)
    page.add(button_start)


# Rodar seu app
ft.app(main, view=ft.WEB_BROWSER)

# Título: ChatPY
# Botão de iniciar Chat
    # popup (janela na frente da tela)
    # Título: Bem vindo ao ChatPY
    # Campo de texto -> Escreva seu nome no chat
    # Botão: Entrar no chat
        # Sumir com o título do ChatPY
        # Fechar a janela (popup)
        # Carregar o chat
            # As mensagens que já foram
            # Campo: Digite sua mensagem
            # Botão de Enviar
# pip install flet -> no seu terminal

import flet as ft

# criar a função principal do seu aplicativo
def main(page):
    # criar todas as funcionalidades
    
    # cria o elemento
    titulo = ft.Text("ChatPY")
    
    popup_title = ft.Text("Bem vindo ao ChatPY")
    user_name_field = ft.TextField(label="Type your name")
    
    chat = ft.Column()

    # Função de comunicação entre aparelhos
    def enviar_mensagem_tunel(mensagem):
        print("Mensagem enviada no tunel")
        print(mensagem)
    
    page.pubsub.subscribe(enviar_mensagem_tunel)
    
    def enviar_mensagem(event):
        texto_mensagem = message_field.value
        nome_usuario = user_name_field.value
        mensagem = f"{nome_usuario}: {texto_mensagem}"
        page.pubsub.send_all(mensagem)
        texto_chat = ft.Text(f"{nome_usuario}: {texto_mensagem}")
        chat.controls.append(texto_chat)
        message_field.value = ""
        page.update()
        
    message_field = ft.TextField(label="Type your message", on_submit=enviar_mensagem)
    button_send_message = ft.ElevatedButton("Send", on_click=enviar_mensagem)

    linha_mensagem = ft.Row([message_field, button_send_message])
    def chat_enter(event):
        page.remove(titulo)
        page.remove(button_start)
        popup.open = False
        page.add(chat)
        page.add(linha_mensagem)
        page.update()
        
    join_button =  ft.ElevatedButton("Enter chat", on_click=chat_enter)
    popup = ft.AlertDialog(
        title=popup_title,
        content=user_name_field,
        actions=[join_button])
    
    def start_chat(event): # OS PARAMETROS NESTA FUNÇÃO NATURALMENTE SÃO SIMILARES A UM Z-INDEX ALTO
        page.dialog = popup 
        page.open = True
        page.update()
        
        
    button_start = ft.ElevatedButton("Send a message", on_click=start_chat)
    
    # adicionar o elemento na pagina
    # OS PARAMETROS NESSE CAMPO SÃO NATURALMENTE COMO UM ZINDEX ALTO, E DEVEM SER ADICIONADOS MANUALMENTE PARA PAGE
    page.add(titulo)
    page.add(button_start)

# rodar seu app
ft.app(main)

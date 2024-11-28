import requests
import time
import sys
from platform import system
import os
import http.server
import socketserver
import threading
BOLD = '\033[1m'
CYAN = '\033[96m'
logo =("""\x1b[1;36m
import


 \033[1;32m.   /$$$$$$  /$$     /$$ /$$$$$$  /$$   /$$  /$$$$$$  /$$   /$$
 \033[1;34m. /$$__  $$|  $$   /$$//$$__  $$| $$$ | $$ /$$__  $$| $$  | $$
 \033[1;32m.| $$  \ $$ \  $$ /$$/| $$  \ $$| $$$$| $$| $$  \__/| $$  | $$
 \033[1;34m.| $$$$$$$$  \  $$$$/ | $$$$$$$$| $$ $$ $$|  $$$$$$ | $$$$$$$$
 \033[1;32m.| $$__  $$   \  $$/  | $$__  $$| $$  $$$$ \____  $$| $$__  $$
 \033[1;34m.| $$  | $$    | $$   | $$  | $$| $$\  $$$ /$$  \ $$| $$  | $$
 \033[1;32m.| $$  | $$    | $$   | $$  | $$| $$ \  $$|  $$$$$$/| $$  | $$
 \033[1;34m|__/  |__/    |__/   |__/  |__/|__/  \__/ \______/ |__/  |__/
                                                             
                                                             
                                                             
                                                                   
 \033[1;32m.  /$$$$$$ /$$   /$$  /$$$$$$  /$$$$$$ /$$$$$$$  /$$$$$$$$
 \033[1;36m.|_  $$_/| $$$ | $$ /$$__  $$|_  $$_/| $$__  $$| $$_____/
 \033[1;32m.  | $$  | $$$$| $$| $$  \__/  | $$  | $$  \ $$| $$      
 \033[1;36m.  | $$  | $$ $$ $$|  $$$$$$   | $$  | $$  | $$| $$$$$   
 \033[1;32m.  | $$  | $$  $$$$ \____  $$  | $$  | $$  | $$| $$__/   
 \033[1;36m.  | $$  | $$\  $$$ /$$  \ $$  | $$  | $$  | $$| $$                      
 \033[1;32m. /$$$$$$| $$ \  $$|  $$$$$$/ /$$$$$$| $$$$$$$/| $$$$$$$$
 \033[1;36m. |______/|__/  \__/ \______/ |______/|_______/ |________/
  ╔═══════════════════Note═══════════════════╗                 
                       【𝐓𝐇𝐄 𝐆𝐀𝐍𝐆𝐒𝐓𝐄𝐑 𝐁𝐎𝐈𝐈 𝐀𝐋𝐎𝐍𝐄 𝐀𝐘𝐀𝐍𝐒𝐆】
  ╚══════════════════════════════════════════╝
\033[1;92m.Author    :  𝐀𝐋𝐎𝐍𝐄 𝐁𝐎𝐘 𝐀𝐘𝐀𝐍𝐒𝐇 𝐈𝐍𝐒𝐈𝐃𝐄|
\033[1;31m.Brother  : 𝐀𝐍𝐈𝐋 𝐈𝐍𝐒𝐈𝐃𝐄 | 𝐀𝐘𝐀𝐍𝐒𝐇 𝐇𝐄𝐑𝐄   |
 \033[1;36mGithub    : 𝐇𝐀𝐓𝐄𝐑𝐒 𝐊𝐈 𝐌𝐀𝐀 𝐂𝐇𝐎𝐃𝐍𝐄 𝐖𝐀𝐋𝐀 𝐌𝐀𝐂𝐇𝐈𝐍𝐄     |
 \033[1;32m.Facebook  : 𝐓𝐇𝐄 𝐁𝐑𝐎𝐊𝐄𝐍 𝐀𝐘𝐀𝐍𝐒𝐇
 \033[1;34mTool Name : 𝐓𝐇𝐄 𝐁𝐑𝐎𝐊𝐄𝐍 𝐋𝐄𝐙𝐄𝐍𝐃 𝐁𝐎𝐘 𝐀𝐘𝐀𝐍𝐒𝐇 𝐈𝐍𝐒𝐈𝐃𝐄   |
 \033[1;36mType type : 𝐅𝐄𝐄𝐋 𝐓𝐇𝐄 𝐏𝐎𝐖𝐄𝐑 𝐎𝐅 𝐒𝐀𝐍𝐓𝐀𝐍𝐈 𝐀𝐘𝐀𝐍𝐒𝐇 |
  ───────────────────────────────────────────────────────
   𖣘︎𖣘︎𖣘︎𖣘︎𖣘︎︻╦デ╤━╼【★𝐀𝐘𝐀𝐍𝐒𝐇 𝐓𝐎𝐎𝐋 𝐎𝐖𝐍𝐀𝐑★】╾━╤デ╦︻𖣘︎𖣘︎𖣘︎𖣘︎𖣘︎
 ───────────────────────────────────────────────────────
\033[1;32m【𝐃𝐄𝐊𝐇 𝐊𝐘𝐀 𝐑𝐀𝐇𝐀 𝐃𝐀𝐋 𝐉𝐀𝐋𝐃𝐈 𝐉𝐀𝐋𝐃𝐈】
 \033[1;36m       𖣘︎𖣘︎𖣘︎【𝐇𝐀𝐓𝐄𝐑𝐒 𝐊𝐀 𝐑𝐄𝐀𝐋 𝐅𝐀𝐓𝐇𝐄𝐑 𝐀𝐘𝐀𝐍𝐒𝐇 𝐇𝐄𝐑𝐄】𖣘︎𖣘︎𖣘︎""" )

def cls():
        if system() == 'Linux':
            os.system('clear')
        else:
            if system() == 'Windows':
                os.system('cls')
cls()
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"H")
def execute_server():
    PORT = 4000
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("Server running at http://localhost:{}".format(PORT))
        httpd.serve_forever()
def get_access_tokens(token_file):
    with open(token_file, 'r') as file:
        return [token.strip() for token in file]
def send_messages(convo_id, tokens, messages, haters_name, speed):
    headers = {
        'Content-type': 'application/json',
    }
    num_tokens = len(tokens)
    num_messages = len(messages)
    max_tokens = min(num_tokens, num_messages)
    while True:
        try:
            for message_index in range(num_messages):
                token_index = message_index % max_tokens
                access_token = tokens[token_index]
                message = messages[message_index].strip()
                url = "https://graph.facebook.com/v17.0/{}/".format('t_' + convo_id)
                parameters = {'access_token': access_token, 'message': f'{haters_name} {message}'}
                response = requests.post(url, json=parameters, headers=headers)
                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                if response.ok:
                    print("\033[1;32m[√]𝐌𝐄𝐒𝐒𝐀𝐆𝐍𝐄 𝐆𝐘𝐀 𝐑𝐀𝐍𝐃𝐖𝐄 】  {} of Convo\033[1;35m {} \033[1;33msent by Token {}: \n\033[1;35m{}".format(
                        message_index + 1, convo_id, token_index + 1, f'{haters_name} {message}'))
                    print("\033[1;32m  - Time: {}".format(current_time))
                else:
                    print("\033[1;32m[x] MESSEGE FAIL HO GYA BHOSDI KE TOKAN SAHI DAL  {} of Convo \033[1;34m{} with Token \033[1;36m{}: \n\033[1;36m{}".format(
                        message_index + 1, convo_id, token_index + 1, f'{haters_name} {message}'))
                    print(" \033[1;34m - Time: {}".format(current_time))
                time.sleep(speed)   
            print("\n\033[1;33m[+] All messages sent. Restarting the process...\n")
        except Exception as e:
            print("\033[1;35m[!] An error occurred: {}".format(e))
def main():	
    print(logo)   
    print(' \033[1;31m[•] 𝐇𝐀𝐓𝐄𝐑𝐒 𝐊𝐈 𝐌𝐀 𝐂𝐇𝐎𝐃𝐍𝐄 𝐊𝐄 𝐋𝐈𝐘𝐄 𝐓𝐎𝐊𝐄𝐍 𝐅𝐈𝐋𝐄 𝐃𝐀𝐀𝐋➼')
    token_file = input(BOLD + CYAN + "=>").strip()
    tokens = get_access_tokens(token_file)
    print(' \033[1;36m[•] 𝐆𝐀𝐍𝐃 𝐍𝐇𝐈 𝐈𝐃 𝐃𝐀𝐋 𝐘𝐀𝐇𝐀➼ ')
    convo_id = input(BOLD + CYAN + "=>").strip()
    print(' \033[1;34m[•] 𝐆𝐀𝐋𝐈 𝐖𝐀𝐋𝐈 𝐅𝐈𝐋𝐄 𝐃𝐀𝐋 𝐉𝐀𝐋𝐃𝐈 ➼')
    messages_file = input(BOLD + CYAN + "=> ").strip()
    print(' \033[1;35m[•] 𝐀𝐏𝐍𝐄 𝐍𝐀𝐉𝐘𝐀𝐉 𝐀𝐔𝐋𝐀𝐃 𝐊𝐀 𝐍𝐀𝐌𝐄 𝐃𝐀𝐀𝐋➼')
    haters_name = input(BOLD + CYAN + "=> ").strip()
    print(' \033[1;34m[•] 𝐋𝐔𝐍𝐃 𝐍𝐇𝐈 𝐌𝐄𝐑𝐀 𝐒𝐏𝐄𝐄𝐃 𝐏𝐀𝐊𝐑 𝐊𝐄 𝐃𝐀𝐀𝐋➼' )
    speed = int(input(BOLD + CYAN + "======> ").strip())
    with open(messages_file, 'r') as file:
        messages = file.readlines()
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()
    send_messages(convo_id, tokens, messages, haters_name, speed)
if __name__ == '__main__':
    main()
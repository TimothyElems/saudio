from vidstream import AudioSender
from vidstream import AudioReceiver
import threading
import socket

# ip = socket.gethostbyname(socket.gethostbyname())

# receiver = AudioReceiver('192.168.0.118', 9999)
receiver = AudioReceiver('192.168.0.157', 9999)
receiver_thread = threading.Thread(target=receiver.start_server)

sender = AudioSender('192.168.0.118', 5555)
# sender = AudioSender('192.168.0.157', 5555)
sender_thread = threading.Thread(target=sender.start_stream)

receiver_thread.start()
sender_thread.start()
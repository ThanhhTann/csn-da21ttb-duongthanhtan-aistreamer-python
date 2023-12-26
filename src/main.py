import sys
import requests
import json
import time
import tempfile
import concurrent.futures
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QLabel, QTextEdit, QComboBox
from PyQt5.QtCore import QUrl
from openai import OpenAI
from cachetools import cached, TTLCache

authorization = "API_KEY"

client = OpenAI(api_key="API_KEY")

app = QApplication([])

cache = TTLCache(maxsize=100, ttl=300)

@cached(cache)
def get_product_info(product_name):
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Translate into Vietnamese the following content: Viết đoạn giới thiệu về sản phẩm {product_name}, đoạn văn cần phải hấp dẫn và logic, giống như lời quảng cáo của một MC (xưng hô là em), đoạn văn chỉ 30 từ."}
      ],
      max_tokens=500
    )
    return completion.choices[0].message.content.strip()

class VideoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.video_widget = QVideoWidget()
        self.player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.player.setVideoOutput(self.video_widget)
        self.setWindowTitle("AI Streamer") 
        self.button = QPushButton('Tạo promt')
        self.video_button = QPushButton('Tạo video') 
        self.input_text = QLineEdit()
        self.label = QLabel()
        self.output_text = QTextEdit()
        self.voice_combobox = QComboBox()
        self.voice_combobox.addItem("Nam")
        self.voice_combobox.addItem("Nữ")
        self.voice_combobox.setFixedWidth(100)
        self.voice_label = QLabel("Chọn voice:")
        self.setup_ui()
    
    def setup_ui(self):
        central_widget = QWidget()
        central_layout = QHBoxLayout() 
        left_layout = QVBoxLayout() 
        right_layout = QVBoxLayout() 

        voice_layout = QHBoxLayout()
        voice_layout.addStretch(1)  # Add a stretchable space before the label and combobox
        voice_layout.addWidget(self.voice_label)
        voice_layout.addWidget(self.voice_combobox)

        left_layout.addWidget(self.label)
        left_layout.addWidget(self.input_text)
        left_layout.addWidget(self.output_text)
        left_layout.addLayout(voice_layout)
        left_layout.addWidget(self.button)
        left_layout.addWidget(self.video_button)

        right_layout.addWidget(self.video_widget)

        central_layout.addLayout(left_layout) 
        central_layout.addLayout(right_layout) 

        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)
        self.button.clicked.connect(self.create_prompt)
        self.video_button.clicked.connect(self.create_video_and_play) 
        self.label.setText('Nhập nội dung vào đây:')
        self.showMaximized()
        
        
        central_layout.setStretchFactor(left_layout, 1)
        central_layout.setStretchFactor(right_layout, 1) 

    def create_prompt(self):
        product_info = get_product_info(self.input_text.text())
        self.output_text.setText(product_info)
        self.product_info = product_info 

    def create_video(self, product_info):
        voice_id = "vi-VN-NamMinhNeural" if self.voice_combobox.currentText() == "Nam" else "vi-VN-HoaiMyNeural"
        url = "https://api.d-id.com/talks"
        payload = {
            "script": {
                "type": "text",
                "subtitles": "false",
                "provider": {
                    "type": "microsoft",
                    "voice_id": voice_id
                },
                "ssml": "false",
                "input": product_info
            },
            "config": {
                "fluent": "false",
                "pad_audio": "0.0",
                "stitch": "true"
            },
            "source_url": "https://create-images-results.d-id.com/DefaultPresenters/santa_f_ai/image.jpeg"
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": authorization
        }
        response = requests.post(url, json=payload, headers=headers)
        response_data = response.json()
        
        id = response_data.get('id')
        print(f"Video_id: {id}")
        return id

    def get_video_url(self, video_id):
        url = f"https://api.d-id.com/talks/{video_id}"
        headers = {
            "accept": "application/json",
            "authorization": authorization
        }

        while True:
            response = requests.get(url, headers=headers)
            response_data = response.json()

            result_url = response_data.get('result_url')

            if result_url is not None:
                print(f"Video_result_url: {result_url}")
                return result_url
            else:
                print("Đang tiến hành GET lại sau 1 giây!!")
                time.sleep(1)

    def download_and_play_video(self, video_url, player):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
            print("Đang tải video...")
            response = requests.get(video_url)
            temp_file.write(response.content)
            print("Đang phát video...")
            player.setMedia(QMediaContent(QUrl.fromLocalFile(temp_file.name)))
            player.play()

    def create_video_and_play(self):
        self.create_prompt()
        video_id = self.create_video(self.product_info)
        video_url = self.get_video_url(video_id)
        self.download_and_play_video(video_url, self.player)

video_window = VideoWindow()
video_window.show()

sys.exit(app.exec_())

import sys
import requests
import json
import time
import tempfile
import concurrent.futures
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QLabel, QTextEdit
from PyQt5.QtCore import QUrl
from openai import OpenAI
from cachetools import cached, TTLCache

api_key = 'API_key'
client = OpenAI(api_key="API_key")

app = QApplication([])

# Create a cache for product info with a Time-To-Live (TTL) of 5 minutes
cache = TTLCache(maxsize=100, ttl=300)

@cached(cache)
def get_product_info(product_name):
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Tell me about the product: {product_name}"}
      ],
      max_tokens=50
    )
    return completion.choices[0].message.content.strip()

def get_video_url(video_id):
    check_url = 'https://api.heygen.com/v1/video_status.get'
    params = {'video_id': video_id,}
    headers = {
        'X-Api-Key': api_key,
        'Content-Type': 'application/json',
    }
    timeout = time.time() + 60*5  # 5 minutes from now
    while True:
        if time.time() > timeout:
            print("Timeout while waiting for video to be ready.")
            return None
        response = requests.get(check_url, params=params, headers=headers)
        status_response = response.json()
        if status_response['code'] == 100 and status_response['data']['status'] == 'completed':
            return status_response['data']['video_url']
        time.sleep(10)

class VideoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.video_widget = QVideoWidget()
        self.player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.player.setVideoOutput(self.video_widget)
        self.button = QPushButton('Tạo promt')
        self.video_button = QPushButton('Tạo video') 
        self.input_text = QLineEdit()
        self.label = QLabel()
        self.output_text = QTextEdit()
        self.setup_ui()
    
    def setup_ui(self):
        central_widget = QWidget()
        central_layout = QHBoxLayout() 
        left_layout = QVBoxLayout() 
        right_layout = QVBoxLayout() 

        left_layout.addWidget(self.label)
        left_layout.addWidget(self.input_text)
        left_layout.addWidget(self.output_text)
        left_layout.addWidget(self.button)
        left_layout.addWidget(self.video_button)

        right_layout.addWidget(self.video_widget)

        central_layout.addLayout(left_layout) 
        central_layout.addLayout(right_layout) 

        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)
        self.button.clicked.connect(self.open_video_window)
        self.video_button.clicked.connect(self.play_video) 
        self.label.setText('Nhập nội dung vào đây:')
        self.showMaximized()
        
        # Set the stretch factors for the two columns in the layout
        central_layout.setStretchFactor(left_layout, 1)
        central_layout.setStretchFactor(right_layout, 1) 

    def open_video_window(self):
        product_info = get_product_info(self.input_text.text())
        self.output_text.setText(product_info)
        self.product_info = product_info 

        # Send request to create video and get video_id
        create_url = 'https://api.heygen.com/v1/video.generate'
        headers = {
            'X-Api-Key': api_key,
            'Content-Type': 'application/json',
        }
        data = {
            "background": "#ffffff",
            "clips": [
                {
                    "avatar_id": "Daisy-inskirt-20220818",
                    "avatar_style": "normal",
                    "input_text": self.product_info,
                    "offset": {
                        "x": 0,
                        "y": 0
                    },
                    "scale": 1,
                    "voice_id": "1bd001e7e50f421d891986aad5158bc8"
                }
            ],
            "ratio": "16:9",
            "test": True,
            "version": "v1alpha"
        }
        response = requests.post(create_url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            response_data = response.json()
            self.video_id = response_data['data']['video_id']  # Save video_id

    def play_video(self):
        if not hasattr(self, 'video_id'):
            print("Error: No video to play. Please create a prompt first.")
            return
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(get_video_url, self.video_id)  # Use self.video_id
            video_url = future.result()
        if video_url is not None:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
                print("Downloading video...")
                response = requests.get(video_url)
                temp_file.write(response.content)
                print("Playing video...")
                self.player.setMedia(QMediaContent(QUrl.fromLocalFile(temp_file.name)))
                self.player.play()

video_window = VideoWindow()
video_window.show()

sys.exit(app.exec_())
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


authorization = "API_KEY"

client = OpenAI(api_key="API_KEY")

app = QApplication([])




def lay_thong_tin_san_pham(ten_san_pham):
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Translate into Vietnamese the following content: Viết đoạn giới thiệu về sản phẩm {ten_san_pham}, đoạn văn cần phải hấp dẫn và logic, giống như lời quảng cáo của một MC (xưng hô là em), đoạn văn chỉ 30 từ."}
      ],
      max_tokens=500
    )
    return completion.choices[0].message.content.strip()

class CuaSoVideo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.video_widget = QVideoWidget()
        self.player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.player.setVideoOutput(self.video_widget)
        self.setWindowTitle("AI Streamer") 
        self.nut_tao_prompt = QPushButton('Tạo prompt')
        self.nut_tao_video = QPushButton('Tạo video') 
        self.nhap_text = QLineEdit()
        self.nhan_dang_label = QLabel()
        self.ket_qua_text = QTextEdit()
        self.combobox_giong_noi = QComboBox()
        self.combobox_giong_noi.addItem("Nam")
        self.combobox_giong_noi.addItem("Nữ")
        self.combobox_giong_noi.setFixedWidth(100)
        self.label_giong_noi = QLabel("Chọn giọng nói:")
        self.setup_giao_dien()
    
    def setup_giao_dien(self):
        trung_tam_widget = QWidget()
        trung_tam_layout = QHBoxLayout() 
        ben_trai_layout = QVBoxLayout() 
        ben_phai_layout = QVBoxLayout() 

        giong_noi_layout = QHBoxLayout()
        giong_noi_layout.addStretch(1) 
        giong_noi_layout.addWidget(self.label_giong_noi)
        giong_noi_layout.addWidget(self.combobox_giong_noi)

        ben_trai_layout.addWidget(self.nhan_dang_label)
        ben_trai_layout.addWidget(self.nhap_text)
        ben_trai_layout.addWidget(self.ket_qua_text)
        ben_trai_layout.addLayout(giong_noi_layout)
        ben_trai_layout.addWidget(self.nut_tao_prompt)
        ben_trai_layout.addWidget(self.nut_tao_video)

        ben_phai_layout.addWidget(self.video_widget)

        trung_tam_layout.addLayout(ben_trai_layout) 
        trung_tam_layout.addLayout(ben_phai_layout) 

        trung_tam_widget.setLayout(trung_tam_layout)
        self.setCentralWidget(trung_tam_widget)
        self.nut_tao_prompt.clicked.connect(self.tao_prompt)
        self.nut_tao_video.clicked.connect(self.tao_video_va_phat) 
        self.nhan_dang_label.setText('Nhập nội dung vào đây:')
        self.showMaximized()
        
        trung_tam_layout.setStretchFactor(ben_trai_layout, 1)
        trung_tam_layout.setStretchFactor(ben_phai_layout, 1) 

    def tao_prompt(self):
        thong_tin_san_pham = lay_thong_tin_san_pham(self.nhap_text.text())
        self.ket_qua_text.setText(thong_tin_san_pham)
        self.thong_tin_san_pham = thong_tin_san_pham 

    def tao_video(self, thong_tin_san_pham):
        giong_noi_id = "vi-VN-NamMinhNeural" if self.combobox_giong_noi.currentText() == "Nam" else "vi-VN-HoaiMyNeural"
        url = "https://api.d-id.com/talks"
        payload = {
            "script": {
                "type": "text",
                "subtitles": "false",
                "provider": {
                    "type": "microsoft",
                    "voice_id": giong_noi_id
                },
                "ssml": "false",
                "input": thong_tin_san_pham
            },
            "config": {
                "fluent": "false",
                "pad_audio": "0.0",
                "stitch": "true"
            },
            "source_url": "https://cdn.leonardo.ai/users/a4a05f79-469d-49e1-96de-f3d2b2376537/generations/ba1f512b-aac3-466f-9188-e663cce981fc/variations/alchemyrefiner_alchemymagic_0_ba1f512b-aac3-466f-9188-e663cce981fc_0.jpg?w=512"
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

    def lay_video_url(self, video_id):
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

    def tai_va_phat_video(self, video_url, player):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
            print(f"Tệp tạm thời được tạo tại: {temp_file.name}")
            print("Đang tải video...")
            response = requests.get(video_url)
            temp_file.write(response.content)
            print("Đang phát video...")
            player.setMedia(QMediaContent(QUrl.fromLocalFile(temp_file.name)))
            player.play()

    def tao_video_va_phat(self):
        self.tao_prompt()
        video_id = self.tao_video(self.thong_tin_san_pham)
        video_url = self.lay_video_url(video_id)
        self.tai_va_phat_video(video_url, self.player)

cua_so_video = CuaSoVideo()
cua_so_video.show()

sys.exit(app.exec_())

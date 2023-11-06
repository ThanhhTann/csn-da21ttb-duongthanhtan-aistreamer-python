import sys
import requests
import json
import time
import tempfile
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit, QLabel
from PyQt5.QtCore import QUrl

api_key = 'MGE0ODY2N2Q0MDQxNDE0OTg1OTJlNDkxZDczMjU0NTMtMTY5NzkwMDc5Nw=='

app = QApplication([])
#######################################################################################
### Thư viện Openai đang trong quá trình lỗi, nên hiện tại code phần đó đã bị xóa!! ###
#######################################################################################
# Khai báo biến temp_file ngoài hàm để sử dụng chung
temp_file = None

# Tạo một lớp kế thừa từ QMainWindow để quản lý các widget và sự kiện của cửa sổ chính
class VideoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Khởi tạo các thuộc tính như video_widget, player, button, input_text, label
        self.video_widget = QVideoWidget()
        self.player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.player.setVideoOutput(self.video_widget)
        self.button = QPushButton('Hiển thị video')
        self.input_text = QLineEdit() # Thêm widget QLineEdit để nhập văn bản vào
        self.label = QLabel() # Thêm widget QLabel để hiển thị tiêu đề
        # Gọi phương thức setup_ui để thiết lập giao diện người dùng
        self.setup_ui()
    
    def setup_ui(self):
        # Tạo một widget trung tâm, một layout dọc, và thêm label, input_text, button và video_widget vào layout
        central_widget = QWidget()
        central_layout = QVBoxLayout()
        central_layout.addWidget(self.label) # Thêm widget label vào layout dọc trước widget input_text
        central_layout.addWidget(self.input_text) # Thêm widget input_text vào layout dọc sau widget label
        central_layout.addWidget(self.button) # Thêm widget button vào layout dọc sau widget input_text
        central_layout.addWidget(self.video_widget)
        central_widget.setLayout(central_layout)
        # Gán widget trung tâm cho cửa sổ chính
        self.setCentralWidget(central_widget)
        # Kết nối sự kiện clicked của button với phương thức open_video_window
        self.button.clicked.connect(self.open_video_window)
        # Thiết lập văn bản cho widget label bằng cách sử dụng phương thức setText()
        self.label.setText('Nhập nội dung vào đây:') # Thiết lập văn bản cho widget label

    def open_video_window(self):
        # Gọi phương thức play_video để tải video từ API và phát video trên video_widget
        self.play_video()

    def play_video(self):
        global temp_file
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")

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
                    "input_text": self.input_text.text(), # Sử dụng giá trị của widget input_text để thay thế cho "input_text"
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

        # Sử dụng các lệnh try-except để bắt các ngoại lệ có thể xảy ra khi gọi API hoặc tải video
        try:
            response = requests.post(create_url, headers=headers, data=json.dumps(data))

            if response.status_code == 200:
                response_data = response.json()
                video_id = response_data['data']['video_id']

                video_url = None
                check_url = 'https://api.heygen.com/v1/video_status.get'
                params = {
                    'video_id': video_id,
                }
                while video_url is None:
                    time.sleep(10)
                    response = requests.get(check_url, params=params, headers=headers)
                    status_response = response.json()
                    if status_response['code'] == 100 and status_response['data']['status'] == 'completed':
                        video_url = status_response['data']['video_url']

                print(f'URL của video: {video_url}')

                # Tải video từ video_url xuống tệp tạm thời
                response = requests.get(video_url)
                temp_file.write(response.content)

                # Thiết lập media cho player bằng cách sử dụng QUrl.fromLocalFile(temp_file.name)
                self.player.setMedia(QMediaContent(QUrl.fromLocalFile(temp_file.name)))
                # Gọi phương thức play() của player
                self.player.play()
            else:
                print(f'Lỗi khi gọi API: {response.status_code}')
        except Exception as e:
            print(f'Lỗi khi tải hoặc phát video: {e}')

# Tạo một đối tượng của lớp VideoWindow và hiển thị nó
video_window = VideoWindow()
video_window.show()

sys.exit(app.exec_())

# Đóng tệp tạm thời sau khi chơi xong video
temp_file.close()

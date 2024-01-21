<!-- Phần ảnh đầu trang -->
<img src="https://i.ibb.co/d5n08bq/Banner-Git-Hub-AI-Streamer-900-x-200-px.gif">
<!-- Phần tiêu đề trang -->
<img src="https://i.ibb.co/4mfc8kN/Banner-Git-Hub-AI-Streamer-900-x-200-px-900-x-50-px.gif">
<!-- Phần cài đặt các tiện ích -->
<p align="center">
    <a href="https://docs.d-id.com/reference/get-started">
        <img src="https://img.shields.io/badge/D--DI-API-%235014FF" alt="D-ID">
    </a>
    <a href="https://platform.openai.com/overview">
        <img src="https://img.shields.io/badge/OpenAI-API-%235014FF" alt="Openai">
    </a>
    <a href="https://openai.com/policies/terms-of-use">
        <img src="https://img.shields.io/badge/License-OpenAI-%235014FF">
    </a>
    <a href="https://www.d-id.com/studio-end-user-license-agreement">
        <img src="https://img.shields.io/badge/License-D--ID-%235014FF">
    </a>
</p>
<!-- Phần điều khoản -->
<p align="center">
    <a href="https://files2.codecguide.com/K-Lite_Codec_Pack_1805_Full.exe">
        <img src="https://img.shields.io/badge/K--Lite-18.0.5-%235014FF">
    </a>
    <a href="https://www.python.org/ftp/python/3.12.1/python-3.12.1-amd64.exe">
        <img src="https://img.shields.io/badge/Python-3.12.1-%235014FF" alt="Python">
    </a>
    <a href="https://bom.so/2Thd6G">
        <img src="https://img.shields.io/badge/FFmpeg-6.1.1-%235014FF" alt="FFmpeg">
    </a>
</p>

## Tổng Quan
Dự án tập trung vào việc nghiên cứu và ứng dụng công nghệ AI để tạo ra một AI Streamer chuyên livestream bán sản phẩm. Trong thời đại số hóa ngày nay, việc tận dụng trí tuệ nhân tạo trong lĩnh vực bán hàng trực tuyến đang trở nên ngày càng quan trọng. Với sự phát triển của các công cụ AI như OpenAI API và D-ID API, chúng ta có thể tạo ra các video quảng cáo sản phẩm một cách tự động và hiệu quả.
Mục tiêu chính của dự án là khai thác sức mạnh của các công cụ AI như OpenAI API và D-ID API, kết hợp với kỹ thuật Prompt Engineering để phát triển một ứng dụng có khả năng tự tạo video quảng cáo sản phẩm một cách tự động và hiệu quả. Đồ án này không chỉ mở rộng kiến thức về AI và lập trình, mà còn giúp hiểu rõ hơn về tiềm năng của AI trong lĩnh vực bán hàng trực tuyến.
> Ghi chú: Dự án này không nhằm mục đích thương mại hay cạnh tranh, mục tiêu của dự án chỉ khám phá và tận dụng sức mạnh của AI bằng cách kết hợp các API, mở ra những tiềm năng mới trong việc tạo ra nội dung và tương tác với người dùng.
## Mô Tả Chi Tiết
Phần mềm sẽ sử dụng API của các công cụ AI như ChatGPT 3.5 và D-ID để tạo ra nội dung văn bản và video từ prompt của người dùng nhập vào. Khi nhận được dữ liệu đầu vào, phần mềm sẽ tạo ra một video giới thiệu sản phẩm với hình ảnh và âm thanh giống như một streamer chuyên nghiệp.  
Các công cụ AI được sử dụng trong dự án này bao gồm:
- **ChatGPT 3.5**: Một mô hình AI có khả năng sinh ra nội dung văn bản theo một đầu vào cho trước.
- **D-ID**: Một mô hình AI có khả năng sinh ra video từ nội dung văn bản.
> Ghi chú: Trong quá trình nghiên cứu và kiểm thử đầu vào thì mô hìnhChatGPT 3.5 và Heygen đã cho ra kết quả tốt hơn so với các mô hình AI khác. Đặc biệt, khả năng tạo ra nội dung văn bản và video chất lượng cao của hai mô hình này đã đưa chúng lên vị trí hàng đầu trong danh sách công cụ được sử dụng cho dự án này. 

## Thiếp Lập Môi Trường
**A. Thiết lập môi trường Python:**  
- <a href="https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe">Python 3.15</a>
- Cài Đặt ffmpeg: Người dùng cần cài đặt ffmpeg để hỗ trợ xử lý và mã hóa video.
- Cài Đặt K-Lite Codec Pack: K-Lite Codec Pack là một bộ codec hữu ích để giải mã và mã hóa các định dạng âm thanh và video khác nhau.
- Cài Đặt Python 3.12.1: Python là ngôn ngữ lập trình chính được sử dụng trong dự án. Người dùng cần cài đặt phiên bản Python 3.12.1.
- Cài Đặt Visual Studio Code: Visual Studio Code là một trình biên tập mã nguồn mở và linh hoạt, được sử dụng để phát triển ứng dụng.
> Ghi chú: Đang tiến hành áp dụng phần mềm lên Docker

## Khởi Tạo Môi Trường 
- Sau khi cài đặt các môi trường cần thiết, người dùng có thể thực hiện các bước sau:
- Bước 1: Truy cập đường link để clone dự án: https://github.com/ThanhhTann/csnda21ttb-duongthanhtan-aistreamer-python
- Bước 2: Mở dự án bằng Visual Studio Code.
- Bước 3: Mở Terminal bằng cách nhấn tổ hợp Ctrl + ~.
- Bước 4: Nhập: 
- Set-ExecutionPolicy Unrestricted -Scope Process
- Set-ExecutionPolicy Unrestricted -Force
- Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
- Bước 4: Gõ các lệnh sau để cài đặt các thư viện Python:
- pip install PyQt5
- pip install requests
- pip install Cachetools
- Bước 5: Sau khi cài đặt xong các môi trường cần thiết, người dùng có thể kiểm tra xem môi trường đã được cài đặt thành công hay chưa bằng cách mở Command Prompt và chạy lệnh:
- python -V
- Bước 6: Khi môi trường đã được cài đặt thành công, người dùng có thể chạy chương trình bằng cách nhấn Ctrl + F5. Ngoài ra, người dùng và các nhà phát triển cũng cần chú ý đến cấu hình máy tính tối thiểu để ứng dụng có thể hoạt động một cách ổn định:
- Hệ điều hành: Windows 10.
- RAM: 4GB.
- Dung lượng ổ cứng (HDD hoặc SSD): 1GB.
- CPU: i3 - 2375M (tối thiểu)
## Tài Liệu Tham Khảo
- OpenaAI API
- D-ID API

## Liên Hệ
- **Email:** duongthanhtan17@gmail.com
- **Số điện thoại:** 0788942313

```bash
# Install photomaker
pip install git+https://github.com/TencentARC/PhotoMaker.git
```

## Tổng Quan


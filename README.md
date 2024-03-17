<!-- Phần ảnh đầu trang -->
<a href="https://github.com/ThanhhTann/csn-da21ttb-duongthanhtan-aistreamer-python">
    <img src="https://i.ibb.co/Ws7yfPK/Banner-AI-Streamer-1.gif">
</a>
<!-- Phần tiêu đề trang -->
<a href="https://github.com/ThanhhTann/csn-da21ttb-duongthanhtan-aistreamer-python">
    <img src="https://i.ibb.co/fCSwJx2/Banner-AI-Streamer-2.gif">
</a>
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
    <a href="https://files2.codecguide.com/K-Lite_Codec_Pack_1810_Full.exe">
        <img src="https://img.shields.io/badge/K--Lite-18.1.0-%235014FF">
    </a>
    <a href="https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe">
        <img src="https://img.shields.io/badge/Python-3.12.2-%235014FF" alt="Python">
    </a>
    <a href="https://bom.so/2Thd6G">
        <img src="https://img.shields.io/badge/FFmpeg-6.1.1-%235014FF" alt="FFmpeg">
    </a>
</p>

<!-- Phần giấy phép -->
<p align="center"> 
    <a href="https://bom.so/0GEFbE">
        <img src="https://img.shields.io/badge/Apache%20License-GPL%203.0%20License-5014FF">
    </a>
</p>


[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FThanhhTann%2Fcsn-da21ttb-duongthanhtan-aistreamer-python.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FThanhhTann%2Fcsn-da21ttb-duongthanhtan-aistreamer-python?ref=badge_large)

## 🔮Tổng Quan
Dự án xây dựng `phần mềm AI Streamer` đang trong quá trình nghiên cứu và triển khai ứng dụng `Trí Tuệ Nhân Tạo`, ứng dụng các mô hình AI tiên tiến như `ChatGPT` và `D-ID`. Mục đích của dự án là phát triển một phần mềm có khả năng tự tạo ra nội dung đa dạng, hình ảnh và video khuôn mặt để giới thiệu và quảng bá sản phẩm, dựa trên dữ liệu đầu vào từ người dùng.
> [!NOTE] 
> Dự án đang trong giai đoạn nghiên cứu và thử nghiệm, hiệu suất và ứng dụng thực tế của dự án chưa được xác minh và đánh giá toàn diện. Tuy nhiên, dự án này đang tiếp tục được cải tiến và phát triển với hy vọng sẽ đóng góp một phần quan trọng cho lĩnh vực thương mại điện tử trong tương lai.

## 🔮Thông Tin Cấu Trúc Thư Mục

> [!NOTE] 
> Dưới đây là cấu trúc thư mục của dự án:
```plaintext
📦 csn-da21ttb-duongthanhtan-aistreamer-python
│
├── 📂 src
│   └── main.py                           # File mã nguồn chính của dự án.
│
├── 📂 progress-report
│   └── Progress_Report.docx              # File Word báo cáo tiến độ dự án.
│
├── 📂 thesis
│   ├── 📂 abs
│   │   └── SileBaoCaoCoSoNganh.pptx      # File PowerPoint báo cáo cơ sở ngành.
│   ├── 📂 doc
│   │   ├── FileBaoCaoDeCuong.docx        # File Word đề cương báo cáo.
│   │   └── FileBaoCaoDoAnCoSoNganh.docx  # File Word báo cáo cơ sở ngành.
│   └── 📂 pdf
│       ├── FileBaoCaoDeCuong.pdf         # Phiên bản PDF đề cương báo cáo.
│       └── FileBaoCaoDoAnCoSoNganh.pdf   # Phiên bản PDF báo cáo cơ sở ngành.
│
├── 📄 .gitignore.txt                     # File định nghĩa các thư mục được bỏ qua khi push.
├── 📄 LICENSE                            # File mô tả giấy phép Apache-2.0 license.
├── 📄 README.md                          # File mô tả dự án và hướng dẫn sử dụng.
└── 📄 requirements.txt                   # File danh sách các thư viện của dự án.
```

## 🔮Tính Năng Chính

> [!NOTE] 
> Phần mềm AI Streamer có các tính năng chính sau:
- Tự động tạo nội dung văn bản từ mô hình `Generative Pre-trained Transformer 3.5 Turbo`.
- Tự động chọn giọng nói và video khuôn mặt động để giới thiệu sản phẩm.
- Tích hợp `API` của `D-ID` để tạo video cùng với giọng nói tự nhiên.
- Tích hợp tùy chọn hình ảnh tùy chỉnh.

## 🔮Thiết Lập Hệ Thống

> [!NOTE] 
> Cấu hình tối thiểu:

<details>
<summary><b>Xem cấu hình tối thiểu</b></summary>

<div align="center">

| Cấu hình           | Diễn giải                             |
| ------------------ | ------------------------------------- |
| Hệ điều hành       | Windows 10                            |
| RAM                | 8GB `(1600 MHz)`                      |
| Dung lượng ổ cứng  | 1GB `(HDD hoặc SSD)`                  |
| CPU Intel          | Core i3 - 2375M `(1.5GHz)`            |
| CPU AMD            | Ryzen 3 - 1200 `(3.1GHz)`             |

</div>
</details>

> [!NOTE] 
> Cấu hình môi trường:

<details>
<summary><b>Xem cấu hình môi trường</b></summary>

<details>
<summary><b>Hướng dẫn cài đặt Pyhon</b></summary>

   - Tải bản cài đặt Python: [Tại đây!!](https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe).
   - Mở tệp cài đặt đã tải để bắt đầu quá trình cài đặt.
   - Trong trình cài đặt, chọn tùy chọn `Add Python 3.12 to PATH`.
   - Nhấn `Install Now` để bắt đầu quá trình cài đặt.
   - Mở `Command Prompt` và kiểm tra phiên bản Python đã cài đặt:
     ```console
     python --version
     ```

</details>

<details>
<summary><b>Hướng dẫn cài đặt K-Lite Codec Pack</b></summary>

   - Tải bản cài đặt K-Lite Codec Pack: [Tại đây!!](https://files2.codecguide.com/K-Lite_Codec_Pack_1810_Full.exe). 
   - Mở tệp cài đặt đã tải để bắt đầu quá trình cài đặt.
   - Sử dụng tổ hợp phím `Win + S`, để mở thanh tìm kiếm trên Windows và gõ:
     ```console
     K-Lite Codec Pack
     ```
   - Nếu xuất hiện `Uninstall K-Lite Codec Pack`, điều đó có nghĩa là phần mềm đã được cài đặt thành công.

</details>

<details>
<summary><b>Hướng dẫn cài đặt FFmpeg</b></summary>

   - Tải bản cài đặt FFmpeg 6.1.1: [Tại đây!!](https://bom.so/2Thd6G). 
   - Sau khi tải xong, giải nén thư mục `ffmpeg-6.1.1` bằng cách chọn `Extract Here`.
   - Đổi tên thư mục vừa giải nén thành:
     ```console
     ffmpeg
     ```  
   - Di chuyển thư mục `ffmpeg` vào `ổ đĩa C`, nên đường dẫn sẽ là:
     ```console
     C:\ffmpeg
     ```  
   - Mở thanh tìm kiếm trên Windows bằng cách nhấn tổ hợp phím `Win + S` và gõ:
     ```console
     View advanced system settings
     ```   
   - Chọn tab `Advanced` và click vào nút `Environment Variables`.
   - Trong phần `User Variables` => chọn `Path` => nhấn `Edit`.
   - Chọn vào nút `New` và thêm đường dẫn:
     ```console
     C:\ffmpeg\bin
     ``` 
   - Nhấn `OK` để lưu thay đổi.

</details>

<details>
<summary><b>Hướng dẫn cài đặt Visual Studio Code</b></summary>

   - Tải bản cài đặt Visual Studio Code: [Tại đây!!](https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user). 
   - Mở tệp cài đặt đã tải để bắt đầu quá trình cài đặt.
   - Sau khi cài đặt xong, mở Visual Studio Code và nhấn tổ hợp phím: `Ctrl + Shift + X` để mở trình quản lý `Extensions`.
   - Trong trình quản lý `Extensions`, tìm kiếm và cài đặt hai `Extensions` quan trọng cho dự án:
     ```console
     Python
     Pylance
     ```
   - Sau khi cài đặt thành công cả hai `Extensions`, tiến hành sang bước tiếp theo để chạy dự án.

</details>
</details>

## 🔮Thiết Lập Môi Trường
> [!NOTE]
> **Hướng dẫn cài đặt dự án từ đầu cho người mới bắt đầu**

<details>
<summary><b>Xem chi tiết</b></summary>

   - **Bước 1:** Mở dự án `csn-da21ttb-duongthanhtan-aistreamer-python` bằng tổ hợp phím tắt `Ctrl + K + O` trong Visual Studio Code.
   - **Bước 2:** Mở file `main.py`.
   - **Bước 3:** Nhấn `Ctrl + ~` để mở `Terminal`.  
   - **Bước 4:** Khởi tạo môi trường ảo `(Lần đầu cài đặt chương trình)`.
     ```console
     python -m venv venv
     ```
   - **Bước 5:** Thiết lập chính sách thực thi.
     ```console
     Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
     ```
   - **Bước 6:** Kích hoạt môi trường ảo.
     ```console
     venv\Scripts\activate
     ```
   - **Bước 7:** Cập nhật pip.
     ```console
     .\venv\Scripts\python.exe -m pip install --upgrade pip
     ```
   - **Bước 8:** Cài đặt các thư viện trong file `requirements.txt`.
     ```console
     pip install -r requirements.txt --upgrade
     ```
   - **Bước 9:** Nhấn `Ctrl + F5` để chạy chương trình.

</details>

> [!NOTE]
> **Hướng dẫn khởi chạy lại chương trình cho người dùng đã cài đặt dự án**

<details>
<summary><b>Xem chi tiết</b></summary>

   - **Bước 1:** Mở dự án `csn-da21ttb-duongthanhtan-aistreamer-python` bằng tổ hợp phím tắt `Ctrl + O + K`.   
   - **Bước 2:** Mở file `main.py` trong Visual Studio Code.
   - **Bước 3:** Nhấn `Ctrl + ~` để mở Terminal trong Visual Studio Code. 
   - **Bước 4:** Nhấn `Ctrl + F5` để chạy chương trình.   

</details>

> [!WARNING] 
> Đảm bảo `Terminal` trong Visual Studio Code đã được mở và đặt tại thư mục `csn-da21ttb-duongthanhtan-aistreamer-python` trước khi tiến hành các bước tiếp theo.

---

## 🔮Thông Tin Tác Giả
- **Author:** ThanhhTann
- **Email:** 110121097@st.tvu.edu.vn
> [!NOTE]
> Dự án được phát triển bởi [ThanhhTann](https://github.com/ThanhhTann) và [baoanth](https://github.com/baoanth). 

---

## 🔮 Thông Tin Giấy Phép
> [!NOTE]
> Dự án [Ai-Streamer](https://bom.so/FsGqwG) hoạt động dưới sự cấp phép **GPL-3.0 license**. 
Mọi thông tin chi tiết, mời xem tại [LICENSE](LICENSE).

---
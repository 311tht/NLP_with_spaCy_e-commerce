# HƯỚNG DẪN SỬ DỤNG NLP-SPACY ÁP DỤNG VÀO E-COMMERCE
 
Phiên bản: v.01

Tạo ngày: 5/6/2023

Người đóng góp:

                         	- Nguyễn Tuệ Minh
                         	- Trần Huyền Tân
                         	- Nguyễn Xuân Lộc
 

# Mục Lục

Tổng quan

Chuẩn bị kỹ thuật

Cài đặt spaCy

Cài đặt W2V

Thực hiện dự đoán

Giai đoạn 1

Giai đoạn 2

Giai đoạn 3


# Tổng quan
Dự án được phát triển bởi các thành viên nhóm AI (D3) trong Savvycom.

Mục tiêu của dự án nhằm áp dụng AI trong các trang thương mại điện tử ( e-commerce ) để nhận diện, phân loại các sản phẩm từ câu nói của người dùng và trả về cho họ các thông tin của sản phẩm mà họ đang tìm kiếm.
Nhóm đã áp dụng công nghệ xử lý ngôn ngữ tự nhiên (NLP) Spacy để nhận diện từ ngữ trong hội thoại của người dùng, sau đó áp dụng thuật toán W2Vec để phân loại và lấy các thuộc tính trong data có sẵn và trả về thông tin sản phẩm mà người dùng tìm kiếm.

Chuẩn bị kĩ thuật
Cài đặt spaCy 

Bản đề cử model dùng cho spaCy: en_core_web_sm và en_core_web_trf.
Cài đặt W2Vec
Tải model 
Wikipedia 2014 + Gigaword 5 (6B tokens, 400K vocab, uncased, 300d vectors, 822 MB download): glove.6B.zip [mirror]

## Thực hiện dự án
- Phần 1

Mục tiêu đầu ra: Nhận dạng sản phẩm (Entity: PRODUCT), tên công ty, giá cả, size, màu sắc.
Bước 1: Train data với spaCy nhận dạng các loại sản phẩm nói chung với nhãn Entity: PRODUCT.
Ví dụ: Định dạng data train trong file js
Bước 2: Sử dụng spaCy đã train để nhận dạng sản phẩm (Entity: PRODUCT), tên công ty dưới danh mục tên Tổ chức (Entity: ORG) và giá cả dưới danh mục Tiền mặt (Entity: MONEY).	
- Phần 2

Mục tiêu đầu ra: Nhận dạng phân loại của sản phẩm (category)
Data: Có danh mục sản phẩm phân loại chi tiết.
Các sản phẩm được phân loại là ENTITY loại PRODUCT sẽ được xử lý bằng thuật toán W2V để xác định loại sản phẩm tương ứng từ một danh sách các loại sản phẩm được cung cấp trước. 
Thuật toán sẽ trả lại 1 dòng sản phẩm gần nhất với key word của người dùng. Qua đó, quá trình phân loại sản phẩm và độ chính xác của hệ thống được cả thiện.
- Phần 3

Mục tiêu đầu ra: Nhận dạng thuộc tính của sản phẩm 
Data: Tất cả sản phẩm được lưu lại với danh mục (category) và các thuộc tính của sản phẩm

Tìm kiếm và trả về tất cả sản phẩm thuộc danh mục đã tìm được ở giai đoạn 2 cùng với thuộc tính của sản phẩm đó.


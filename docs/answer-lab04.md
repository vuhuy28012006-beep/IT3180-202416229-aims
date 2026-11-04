# Câu trả lời thảo luận - Lab 04

## 1. Vì sao không merge `release/*` ngược vào `master`? So sánh với GitFlow.

Nhánh `release/*` là baseline của một phiên bản đã phát hành, cần được giữ ổn định để có thể tái tạo và bảo trì đúng phiên bản đó. `master` tiếp tục phát triển các tính năng cho phiên bản sau. Merge toàn bộ nhánh release ngược vào `master` có thể đưa các thay đổi chỉ dành cho bản phát hành hoặc lịch sử không cần thiết vào dòng phát triển chính. Nếu có hotfix, cần áp dụng có chủ đích cho từng nhánh còn được bảo trì; trong Lab 05, bài thực hành dùng `cherry-pick -x` để ghi lại nguồn commit.

GitFlow cũng tách nhánh phát triển và nhánh phát hành: thường tạo `release/*` từ nhánh phát triển để ổn định bản sắp phát hành, rồi sau khi phát hành, hợp nhất các sửa lỗi cần thiết trở lại nhánh phát triển và nhánh chính (`main`/`master`). Trong bài thực hành này, `release/lab04` đóng băng baseline; không merge nguyên nhánh release ngược vào `master`.

## 2. Vì sao lên `1.0.0` mà không phải `0.4.0`?

Theo quy ước Semantic Versioning trong bài, `0.y.z` dành cho giai đoạn chưa ổn định. Phiên bản `1.0.0` đánh dấu baseline đầu tiên được xem là ổn định và phát hành chính thức sau Lab 01–03. Do đó đây là mốc `1.0.0`, không phải bản phát hành thử tiếp theo `0.4.0`. Sau mốc này, tính năng mới tương thích có thể tăng MINOR, chẳng hạn `1.1.0`; sửa lỗi tương thích có thể tăng PATCH, chẳng hạn `1.0.1`.

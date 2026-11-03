Answers – Lab 02

1. Vì sao phải đồng bộ master trước khi tạo Pull Request?

Cần đồng bộ master trước khi tạo Pull Request vì trong quá trình phát triển, master có thể đã được cập nhật bởi các thành viên khác. Nếu không đồng bộ, nhánh feature có thể sử dụng mã nguồn cũ, thiếu những thay đổi mới và dễ xảy ra xung đột khi tích hợp.

Việc đồng bộ giúp đảm bảo tính năng mới được phát triển trên nền tảng mã nguồn mới nhất, đồng thời phát hiện và xử lý xung đột sớm trước khi gửi Pull Request.


2. Khi nào không được rebase?

Không nên rebase các nhánh đã được push lên repository chung và đang được nhiều người cùng sử dụng.

Rebase tạo ra các commit mới với mã SHA khác, làm thay đổi lịch sử commit. Điều này có thể khiến các thành viên khác gặp khó khăn khi đồng bộ nhánh và phát sinh xung đột.

Vì vậy, chỉ nên rebase các nhánh cá nhân chưa được chia sẻ. Với các nhánh dùng chung, nên ưu tiên merge để giữ nguyên lịch sử commit.

3. feature/* khác topic/* ra sao?

feature/*: Dùng để phát triển một chức năng mới của phần mềm, ví dụ feature/cart-print và feature/search-by-title trong Lab 02.

topic/*: Dùng để thực hiện một chủ đề hoặc công việc hỗ trợ quá trình phát triển, ví dụ topic/pr-template và topic/use-case-diagram.

Tóm lại, feature/* tập trung vào việc bổ sung chức năng cho sản phẩm, còn topic/* tập trung vào các công việc hỗ trợ như tài liệu, cấu hình hoặc tổ chức quy trình phát triển.
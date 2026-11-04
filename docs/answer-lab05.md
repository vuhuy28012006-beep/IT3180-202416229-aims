# Câu hỏi thảo luận Lab 05

## 1. Ưu, nhược điểm của upstream-first so với release-first?

Với upstream-first, sửa lỗi trước trên nhánh phát triển chính (`master`), sau đó cherry-pick bản sửa sang các nhánh release cần nhận hotfix. Cách này giữ `master` làm nguồn sửa lỗi chuẩn và giúp các phiên bản tương lai cũng có bản sửa. Đổi lại, người dùng các phiên bản đang phát hành có thể phải chờ bản sửa được lan truyền; mỗi nhánh release vẫn cần được cập nhật và kiểm tra, nên có thể phát sinh xung đột hoặc bị bỏ sót.

Với release-first, tạo hotfix từ nhánh release bị ảnh hưởng, sửa và phát hành bản vá ở đó trước, rồi cherry-pick bản sửa sang `master` và các release khác. Cách này ưu tiên khắc phục nhanh cho phiên bản đang được sử dụng và kiểm tra bản sửa trong đúng dòng mã phát hành. Nhược điểm là cùng một thay đổi phải được lan truyền qua nhiều nhánh; nếu quên cherry-pick hoặc chọn sai nhánh, các phiên bản sẽ không đồng nhất.

## 2. Nếu quên lan truyền bản sửa sang `release/lab05`, lệnh nào ở Phần F sẽ phát hiện?

Lệnh `git log --all --oneline --grep "cherry picked from commit <FIX_SHA>"` phải tìm thấy hai commit cherry-pick: một trên `master` và một trên `release/lab05`. Nếu chỉ thấy một commit, hotfix chưa được lan truyền tới một trong hai nhánh. Có thể kiểm tra cụ thể nhánh release bằng `git log origin/release/lab05 --oneline --grep "cherry picked from commit <FIX_SHA>"`.

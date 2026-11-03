# Thảo luận Lab 03

## 1. Merge base là gì?

Merge base là commit tổ tiên chung gần nhất của hai nhánh cần hợp nhất. Git dùng commit này làm mốc để xác định mỗi nhánh đã thay đổi những gì kể từ khi hai nhánh tách nhau, rồi kết hợp các thay đổi đó. Có thể xem mốc này bằng `git merge-base <nhánh-1> <nhánh-2>`.

## 2. Vì sao dùng `git revert` trên `master` và `release/*`?

`master` và `release/*` là các nhánh đã chia sẻ hoặc dùng làm baseline. `git reset` di chuyển con trỏ nhánh và có thể làm lịch sử đã chia sẻ biến mất, khiến các bản sao của cộng tác viên lệch nhau. `git revert` tạo một commit mới đảo ngược thay đổi cần bỏ, giữ nguyên lịch sử đã công bố và để lại dấu vết kiểm toán. Vì vậy, dùng `revert` cho lịch sử chung; chỉ dùng `reset` để sửa commit riêng chưa chia sẻ.

# Câu trả lời - Lab 04

## F. Ghi nhận trạng thái (Status Accounting)

Các kết quả dưới đây được ghi nhận sau khi PR #18 được merge vào `master`.

### Commit trên `master` nhưng chưa có trên `release/lab04`

Lệnh `git log --oneline release/lab04..master` cho thấy `master` đi trước baseline release với các commit:

- `50eb775` Merge pull request #18 — thêm chức năng sắp xếp giỏ hàng.
- `5f5753e` Thêm `sort_by_title()` và `sort_by_cost()` cùng kiểm thử.
- `5f3dd98` Merge pull request #17 — hoàn thiện CHANGELOG.
- `c155955` Hoàn thiện CHANGELOG cho bản 1.0.0.

Lệnh `git log --oneline master..release/lab04` không in kết quả. Nghĩa là hiện không có commit riêng chỉ nằm trên `release/lab04` mà thiếu ở `master`.

### So sánh các baseline và trạng thái hiện tại

`git diff --stat v0.3.0 v1.0.0`:

- `CHANGELOG.md`: 14 dòng thêm.
- `aims/__init__.py`: thêm phiên bản `1.0.0`.
- `main.py`: cập nhật thông tin phiên bản phát hành.
- Tổng: 17 dòng thêm, 3 dòng xóa trên 3 tệp.

`git diff --stat v1.0.0 master`:

- `CHANGELOG.md`: cập nhật mục Unreleased.
- `aims/cart.py`: thêm hai phương thức sắp xếp.
- `tests/test_cart.py`: thêm kiểm thử cho hai phương thức.
- Tổng: 36 dòng thêm, 1 dòng xóa trên 3 tệp.

`git describe --tags` trên `master` trả về `v1.0.0-4-g50eb775`: `master` đang ở bốn commit sau tag `v1.0.0`. `git log --oneline --no-merges v0.3.0..v1.0.0` cho thấy hai commit không phải merge: chuẩn bị release và cập nhật CHANGELOG trên nhánh release.

Theo quy tắc `A..B`, danh sách là các commit có trong B nhưng không có trong A.

## G. Tái tạo phiên bản cũ (Configuration Audit)

### Kiểm tra tag cũ bằng detached HEAD

Đã checkout `v0.2.0` ở detached HEAD tại commit `e26a64e`, chạy `python main.py`, sau đó chuyển lại `master`. Chương trình chạy thành công, tổng tiền giỏ hàng là `63.89 $`, gồm hai DVD. Checkout tag không tạo commit và nhánh `master` sau đó vẫn ở trạng thái sạch.

### Dựng lại bản phát hành 1.0.0 bằng worktree

Đã tạo worktree tạm tại tag `v1.0.0` (commit `1522687`), chạy `python -m unittest discover -s tests -v`: **4/4 kiểm thử đạt**. Worktree được gỡ sau khi kiểm tra.

Kiểm toán nội dung tag:

- `git show v1.0.0:aims/__init__.py` xác nhận `__version__ = "1.0.0"`.
- Cây tệp của tag không chứa `__pycache__`, `.pyc`, `.class` hoặc `.exe`.
- `git archive --format=zip --prefix=aims-1.0.0/ -o aims-1.0.0.zip v1.0.0` tạo được gói mã nguồn tái dựng từ tag.

## Thảo luận

### Vì sao không merge `release/*` ngược vào `master`?

`release/lab04` đóng băng baseline 1.0.0 để có thể tái tạo đúng bản phát hành. `master` tiếp tục nhận tính năng mới. Merge ngược toàn bộ nhánh release có thể đưa lịch sử hoặc thay đổi chỉ dành cho bảo trì release vào dòng phát triển chính. Khi có hotfix, nên áp dụng có kiểm soát lên từng dòng phiên bản bị ảnh hưởng; Lab 05 dùng `cherry-pick -x` để lưu dấu commit nguồn.

### Vì sao phát hành `1.0.0` thay vì `0.4.0`?

Theo quy ước trong bài, các phiên bản `0.y.z` biểu thị giai đoạn chưa ổn định. `1.0.0` đánh dấu baseline đầu tiên được xem là ổn định và phát hành chính thức sau Lab 01–03. Sau đó, tính năng tương thích có thể tăng MINOR (ví dụ `1.1.0`), còn sửa lỗi tương thích tăng PATCH (ví dụ `1.0.1`).

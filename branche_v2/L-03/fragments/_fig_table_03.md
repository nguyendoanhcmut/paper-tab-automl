    * **Bảng 3.** Hiệu suất trung bình của TOPOFE trên tất cả các tập dữ liệu phân loại và hồi quy dưới ba mô hình nền tảng LLM
      * <img src="assets/table_03_p11.png" alt="Bảng 3" />
      * **Bảng này chứng minh điều gì**
        * TOPOFE duy trì hiệu suất mạnh mẽ và ổn định trên cả tác vụ phân loại và hồi quy bất kể mô hình LLM nền tảng là mã nguồn mở hay thương mại, khẳng định tính độc lập với mô hình nền (backbone-agnostic).
      * **Từ đâu mà thấy được**
        * Hàng phân loại (Accuracy ↑) đạt 0.8371 (QwenCode-7B), 0.8403 (Qwen3-8B) và 0.8468 (GPT-4o-mini); hàng hồi quy (RMSE ↓) đạt 2.6790, 2.6928 và 2.6342, cho thấy độ biến thiên hiệu suất rất nhỏ giữa các mô hình khác biệt về năng lực.

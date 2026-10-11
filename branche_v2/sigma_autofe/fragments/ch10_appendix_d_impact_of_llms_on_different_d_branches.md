## Appendix D. Impact of LLMs on different datasets

- **Tác động của các mô hình LLM nền tảng (LLM Backbones)**:
  - Bảng 6 (Table 6) thực nghiệm so sánh tác động của các mô hình ngôn ngữ lớn (LLM) nền tảng khác nhau lên hiệu năng của SIGMA qua 16 bộ dữ liệu dạng bảng.
  - Các ký hiệu đặc tả tập dữ liệu gồm: $C$ là số lượng lớp (number of classes), $F$ là số lượng đặc trưng (number of features), và $N$ là số lượng mẫu (number of samples).
  - Ba mô hình LLM nền tảng được đánh giá: **Llama3.1-70B**, **Qwen3-4B** (Qwen3-4B-Instruct), và **Qwen3-Coder-Next**.
- **So sánh hiệu năng tổng thể**:
  - **Điểm F1 trung bình (Average F1-score)**:
    - Qwen3-4B đạt điểm cao nhất với $79.80 \pm 0.23$.
    - Qwen3-Coder-Next đạt $79.71 \pm 0.14$.
    - Llama3.1-70B đạt $79.54 \pm 0.08$.
  - **Thứ hạng trung bình (Avg Rank)**:
    - Qwen3-Coder-Next đạt thứ hạng tổng thể tốt nhất với $1.88$.
    - Llama3.1-70B đạt thứ hạng trung bình $2.00$.
    - Qwen3-4B đạt thứ hạng trung bình $2.12$.
- **Chi tiết kết quả F1-score trên từng bộ dữ liệu (Table 6: Impact of LLMs on each dataset of F1-score)**:
  - *eucalyptus* ($C = 5, F = 19, N = 736$): Llama3.1-70B đạt $65.15 \pm 2.35$; Qwen3-4B đạt $66.39 \pm 2.29$; Qwen3-Coder-Next đạt $65.43 \pm 2.45$.
  - *diabetes* ($C = 2, F = 8, N = 768$): Llama3.1-70B đạt $73.50 \pm 3.72$; Qwen3-4B đạt $74.82 \pm 3.16$; Qwen3-Coder-Next đạt $73.97 \pm 3.92$.
  - *credit-g* ($C = 2, F = 20, N = 1,000$): Llama3.1-70B đạt $73.33 \pm 2.70$; Qwen3-4B đạt $74.84 \pm 2.19$; Qwen3-Coder-Next đạt $73.84 \pm 2.00$.
  - *pc1* ($C = 2, F = 21, N = 1,109$): Llama3.1-70B đạt $92.70 \pm 1.04$; Qwen3-4B đạt $92.22 \pm 1.06$; Qwen3-Coder-Next đạt $92.32 \pm 1.06$.
  - *cmc* ($C = 3, F = 9, N = 1,473$): Llama3.1-70B đạt $51.66 \pm 2.65$; Qwen3-4B đạt $51.46 \pm 2.50$; Qwen3-Coder-Next đạt $51.14 \pm 3.16$.
  - *wine* ($C = 2, F = 11, N = 2,554$): Llama3.1-70B đạt $79.76 \pm 1.36$; Qwen3-4B đạt $79.13 \pm 0.89$; Qwen3-Coder-Next đạt $79.31 \pm 1.24$.
  - *MagicTelescope* ($C = 2, F = 10, N = 13,376$): Llama3.1-70B đạt $86.72 \pm 0.30$; Qwen3-4B đạt $86.58 \pm 0.46$; Qwen3-Coder-Next đạt $86.38 \pm 0.52$.
  - *house 16H* ($C = 2, F = 16, N = 13,488$): Llama3.1-70B đạt $87.94 \pm 0.50$; Qwen3-4B đạt $87.71 \pm 0.36$; Qwen3-Coder-Next đạt $87.77 \pm 0.54$.
  - *compass* ($C = 2, F = 17, N = 16,644$): Llama3.1-70B đạt $77.01 \pm 1.29$; Qwen3-4B đạt $77.97 \pm 1.00$; Qwen3-Coder-Next đạt $77.46 \pm 0.92$.
  - *electricity* ($C = 2, F = 8, N = 38,474$): Llama3.1-70B đạt $90.87 \pm 0.25$; Qwen3-4B đạt $90.77 \pm 0.31$; Qwen3-Coder-Next đạt $91.33 \pm 0.34$.
  - *jungle chess* ($C = 3, F = 6, N = 44,819$): Llama3.1-70B đạt $91.17 \pm 3.06$; Qwen3-4B đạt $92.62 \pm 2.12$; Qwen3-Coder-Next đạt $93.45 \pm 2.59$.
  - *airlines* ($C = 2, F = 7, N = 50,000$): Llama3.1-70B đạt $63.39 \pm 0.68$; Qwen3-4B đạt $63.31 \pm 0.53$; Qwen3-Coder-Next đạt $63.44 \pm 0.63$.
  - *covertype* ($C = 2, F = 54, N = 50,000$): Llama3.1-70B đạt $88.44 \pm 0.41$; Qwen3-4B đạt $88.29 \pm 0.43$; Qwen3-Coder-Next đạt $88.34 \pm 0.51$.
  - *jannis* ($C = 2, F = 54, N = 50,000$): Llama3.1-70B đạt $78.63 \pm 0.56$; Qwen3-4B đạt $78.84 \pm 0.26$; Qwen3-Coder-Next đạt $78.76 \pm 0.57$.
  - *MiniBooNE* ($C = 2, F = 50, N = 50,000$): Llama3.1-70B đạt $93.88 \pm 0.48$; Qwen3-4B đạt $93.92 \pm 0.49$; Qwen3-Coder-Next đạt $93.94 \pm 0.53$.
  - *road-safety* ($C = 2, F = 32, N = 50,000$): Llama3.1-70B đạt $78.54 \pm 0.77$; Qwen3-4B đạt $77.94 \pm 0.46$; Qwen3-Coder-Next đạt $78.40 \pm 0.73$.

| Dataset | $C$ | $F$ | $N$ | Llama3.1-70B | Qwen3-4B | Qwen3-Coder-Next |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| eucalyptus | 5 | 19 | 736 | $65.15 \pm 2.35$ | $66.39 \pm 2.29$ | $65.43 \pm 2.45$ |
| diabetes | 2 | 8 | 768 | $73.50 \pm 3.72$ | $74.82 \pm 3.16$ | $73.97 \pm 3.92$ |
| credit-g | 2 | 20 | 1,000 | $73.33 \pm 2.70$ | $74.84 \pm 2.19$ | $73.84 \pm 2.00$ |
| pc1 | 2 | 21 | 1,109 | $92.70 \pm 1.04$ | $92.22 \pm 1.06$ | $92.32 \pm 1.06$ |
| cmc | 3 | 9 | 1,473 | $51.66 \pm 2.65$ | $51.46 \pm 2.50$ | $51.14 \pm 3.16$ |
| wine | 2 | 11 | 2,554 | $79.76 \pm 1.36$ | $79.13 \pm 0.89$ | $79.31 \pm 1.24$ |
| MagicTelescope | 2 | 10 | 13,376 | $86.72 \pm 0.30$ | $86.58 \pm 0.46$ | $86.38 \pm 0.52$ |
| house 16H | 2 | 16 | 13,488 | $87.94 \pm 0.50$ | $87.71 \pm 0.36$ | $87.77 \pm 0.54$ |
| compass | 2 | 17 | 16,644 | $77.01 \pm 1.29$ | $77.97 \pm 1.00$ | $77.46 \pm 0.92$ |
| electricity | 2 | 8 | 38,474 | $90.87 \pm 0.25$ | $90.77 \pm 0.31$ | $91.33 \pm 0.34$ |
| jungle chess | 3 | 6 | 44,819 | $91.17 \pm 3.06$ | $92.62 \pm 2.12$ | $93.45 \pm 2.59$ |
| airlines | 2 | 7 | 50,000 | $63.39 \pm 0.68$ | $63.31 \pm 0.53$ | $63.44 \pm 0.63$ |
| covertype | 2 | 54 | 50,000 | $88.44 \pm 0.41$ | $88.29 \pm 0.43$ | $88.34 \pm 0.51$ |
| jannis | 2 | 54 | 50,000 | $78.63 \pm 0.56$ | $78.84 \pm 0.26$ | $78.76 \pm 0.57$ |
| MiniBooNE | 2 | 50 | 50,000 | $93.88 \pm 0.48$ | $93.92 \pm 0.49$ | $93.94 \pm 0.53$ |
| road-safety | 2 | 32 | 50,000 | $78.54 \pm 0.77$ | $77.94 \pm 0.46$ | $78.40 \pm 0.73$ |
| **Average** | - | - | - | $79.54 \pm 0.08$ | $79.80 \pm 0.23$ | $79.71 \pm 0.14$ |
| **Avg Rank** | - | - | - | 2.00 | 2.12 | 1.88 |

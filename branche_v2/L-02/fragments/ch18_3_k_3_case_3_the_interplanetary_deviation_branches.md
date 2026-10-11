### K.3 Case 3: The Interplanetary Deviation Risk Index

* **Các đặc trưng thô ban đầu (Raw features)**:
  * Biến $X_1$ đại diện cho hành tinh quê hương (`HomePlanet` - điểm xuất phát / *origin*).
  * Biến $X_4$ đại diện cho hành tinh đích đến (`Destination` - điểm đến).
  * Cả hai biến đều là các biến phân loại danh mục được mã hóa số bằng nhãn (*label-encoded categorical codes*).
* **Khám phá tương tác và hạn chế của hồi quy ký hiệu (Symbolic regression interactions & limitations)**:
  * Hồi quy ký hiệu (*symbolic regression - SR*) khảo sát các mối tương tác giữa $X_1$ (`HomePlanet`) và $X_4$ (`Destination`) thông qua các số hạng tích nhân (*multiplicative terms*), tiêu biểu như $\text{mul}(X_4, X_1)$.
  * **Tạo phẩm số học vô nghĩa về mặt vật lý (*numerical artifact devoid of physical meaning*)**:
    * Việc nhân hai mã phân loại danh mục với nhau (ví dụ: $\text{Earth} \times \text{TRAPPIST-1e} = 3$) chỉ tạo ra một tạo phẩm số học thuần túy không mang ý nghĩa vật lý.
    * Không một người đọc hay chuyên gia nào có thể diễn giải được tích số của hai hành tinh được mã hóa nhãn (*label-encoded product of two planets*) thực sự đại diện cho điều gì.
* **Đặc trưng do LLM tạo ra và công thức chỉ số rủi ro (LLM-generated feature & risk index formulation)**:
  * Mô hình ngôn ngữ lớn (*LLM*) đề xuất và sinh ra đặc trưng hiệu có hướng (*directed difference*):
    $$X_4 - X_1$$
  * **Cơ chế nắm bắt mối quan hệ định hướng (*directional relationship*)**:
    * Biểu thức $X_4 - X_1$ nắm bắt mối quan hệ định hướng giữa điểm xuất phát và đích đến.
    * Phần chú giải (*annotation*) của LLM định khung đây là một đặc trưng thể hiện mức độ mà mã hóa của điểm đến vượt quá mã hóa của hành tinh quê hương (*how much the destination encoding exceeds the home planet encoding*).
    * Đặc tính này mang ý nghĩa quyết định (*critical*) khi các biến tạo ra những tác động đối nghịch nhau (*opposing effects*) lên kết quả phân loại (*classification*).
* **Ngữ nghĩa vật lý và độ lệch quỹ đạo liên hành tinh (Cross-planetary trajectory deviations & physical semantics)**:
  * **Bối cảnh kịch bản tàu vũ trụ (*Spaceship scenario*)**:
    * Khi $\text{Destination} \neq \text{HomePlanet}$, hành khách bắt đầu một chuyến hành trình liên hành tinh (*interplanetary journey*).
    * Hành trình liên hành tinh kéo theo hàng loạt yếu tố rủi ro gia tăng: thời gian di chuyển dài hơn (*longer travel times*), đối mặt với các rủi ro môi trường xa lạ (*unfamiliar environmental risks*), và đòi hỏi công tác hỗ trợ hậu cần phức tạp hơn (*more complex logistical support*).
  * **Ý nghĩa độ lớn của hiệu số ($X_4 - X_1$)**:
    * Độ lớn của $X_4 - X_1$ mã hóa khoảng cách mà hành khách đã di chuyển cách xa thế giới quê hương (*how far the passenger has traveled from their home world*).
    * Độ lệch càng lớn ngụ ý các điểm đến càng xa xôi, hẻo lánh hơn (*more remote destinations*), dẫn đến xác suất sống sót (*survival probabilities*) bị dịch chuyển một cách có hệ thống (*systematically shifted*).
  * **Bảo toàn tính định hướng (*Directionality preservation*)**:
    * Điểm then chốt là phép trừ bảo toàn tính định hướng (*preserves directionality*): nó phân biệt rõ rệt giữa việc di chuyển hướng tới một điểm đến an toàn hơn (*safer destination*) so với việc di chuyển tới một điểm đến nguy hiểm hơn (*more hazardous destination*).
    * Đây là một thuộc tính cốt lõi hoàn toàn vắng bóng (*entirely absent*) trong số hạng tích nhân $\text{mul}(X_4, X_1)$ của hồi quy ký hiệu.
* **Bước tiến về khả năng diễn giải và xác thực hạ nguồn (Interpretability advances & downstream validation)**:
  * Khả năng diễn giải mô hình đạt bước tiến vượt bậc:
    * Chuyển đổi từ "một tích số của các mã danh mục" (*a product of categorical codes*) mờ đục và thiếu căn cứ ngữ nghĩa.
    * Trở thành "độ lệch rủi ro tương đối của chuyến du hành liên hành tinh" (*the relative risk deviation of interplanetary travel*) có cơ sở vật lý rõ ràng và giá trị dự báo cao cho bài toán phân loại.

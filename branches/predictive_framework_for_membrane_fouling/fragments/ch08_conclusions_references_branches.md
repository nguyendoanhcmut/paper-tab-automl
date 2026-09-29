## 4. Kết luận và Định hướng tương lai (Conclusions & Future Perspectives)

### 4.1 Kết luận tổng kết nghiên cứu (Study Conclusions & Core Syntheses)

#### 4.1.1 Hiệu năng của khung tích hợp học máy và tiền xử lý dữ liệu
- Khung làm việc tích hợp kỹ thuật trích xuất đặc trưng với mô hình học máy giải thích được (XAI).
- Nghiên cứu kiểm chứng mô hình trên hệ thống MBR quy mô công nghiệp xử lý nước thải thực phẩm với lưu lượng $200\text{ m}^3/\text{ngày}$.
- Kiểm định Shapiro-Wilk xác nhận 9 trong 10 thông số vận hành lệch khỏi phân phối chuẩn.
- Phương pháp Robust Scaling chuẩn hóa dữ liệu hiệu quả qua công thức $X_{scaled} = \frac{X - \text{median}}{Q_3 - Q_1}$. Phương pháp này triệt tiêu ảnh hưởng của các điểm dị biệt vận hành cực đoan.
- Bộ lọc trung bình trượt 5 ngày (MA-5) làm mịn nhiễu ngẫu nhiên từ cảm biến. Kỹ thuật này mô phỏng thời gian lưu sinh học và phản ánh sự tích tụ của lớp cặn màng.
- Thông số mục tiêu Specific Flux ($J_{spec} = \frac{J}{\text{TMP}}$) thay thế áp suất xuyên màng TMP thô. Chỉ số này phản ánh trực tiếp độ thấm màng và loại bỏ biến động lưu lượng tức thời.
- Việc bổ sung hiệu suất khử COD ($\text{Eff}_{\text{COD}}$) giúp mô hình liên kết chặt chẽ hoạt tính sinh học với tốc độ tắc nghẽn màng.

#### 4.1.2 Ưu thế vượt trội của thuật toán CatBoost
- Thuật toán CatBoost đạt độ chính xác cao nhất với hệ số xác định $R^2 = 0.8374$ trên tập kiểm tra.
- Kỹ thuật tiền xử lý dữ liệu giúp giảm sai số dự báo $27.8\%$ so với mô hình huấn luyện trên dữ liệu thô ($R^2 = 0.7317$).
- CatBoost vượt trội hoàn toàn so với bốn mô hình hồi quy tuyến tính cổ điển gồm Linear Regression, Ridge, Lasso và Elastic Net ($R^2 < 0.20$).
- CatBoost vượt qua mô hình XGBoost ($R^2 = 0.7186$) trên cả bốn trường hợp thử nghiệm.
- Cơ chế Ordered Boosting trong CatBoost ngăn chặn hiện tượng rò rỉ mục tiêu trên chuỗi dữ liệu thời gian thực.
- Cấu trúc cây quyết định đối xứng giúp CatBoost xử lý tốt các mối quan hệ phi tuyến phức tạp trong bể phản ứng màng.

#### 4.1.3 Thấu hiểu cơ chế tắc nghẽn qua kỹ thuật XAI
- Ba kỹ thuật giải thích gồm Built-in Importance, Permutation Importance và SHAP cho kết quả đánh giá thống nhất.
- Tỷ lệ thức ăn trên vi sinh vật trung bình trượt 5 ngày (F/M_MA5) chi phối mạnh nhất đến tốc độ tắc nghẽn màng với đóng góp SHAP đạt $26.17\%$.
- Nồng độ bùn hoạt tính lơ lửng MLSS giữ vị trí quan trọng thứ hai với mức đóng góp SHAP đạt $10.04\%$.
- Tỷ lệ F/M tăng cao kích thích vi khuẩn bài tiết nhiều polymer ngoại bào (EPS) và chất chuyển hóa hòa tan (SMP).
- Nồng độ MLSS cao kết hợp với chất keo sinh học đẩy nhanh quá trình lắng đọng lớp bánh bùn trên bề mặt sợi rỗng.
- Môi trường pH thấp làm suy giảm độ ổn định của bông bùn sinh học và làm tăng lực cản lọc qua màng.

### 4.2 Đóng góp cho vận hành công nghiệp (Industrial Operational Value)

#### 4.2.1 Kết nối giữa lý thuyết học thuật và thực tiễn vận hành
- Nghiên cứu giải quyết bài toán vận hành trên chuỗi dữ liệu 194 ngày liên tục từ nhà máy xử lý nước thải thực phẩm.
- Khung làm việc hoạt động ổn định trong các điều kiện dữ liệu không lý tưởng, chứa nhiều nhiễu và độ trễ sinh học.
- Quy trình chỉ yêu cầu các thông số đo lường cơ bản tại trạm xử lý như lưu lượng, TMP, COD, MLSS, pH, DO và nhiệt độ.
- Nhà máy không cần đầu tư các thiết bị phân tích đắt tiền như máy đo nồng độ EPS, SMP chuyên dụng hay kính hiển vi lực nguyên tử (AFM).
- Mô hình giúp kỹ sư trạm nắm bắt diễn biến tắc màng mà không cần gián đoạn quy trình công nghệ.

#### 4.2.2 Chuyển đổi mô hình bảo trì chủ động
- Phương pháp vận hành truyền thống áp dụng cơ chế bảo trì phản ứng. Trạm chỉ sục rửa khi áp suất TMP vượt ngưỡng cho phép.
- Cơ chế phản ứng làm gia tăng nguy cơ hình thành màng cặn không thể phục hồi (irreversible fouling). Tình trạng này làm giảm tuổi thọ của sợi màng.
- Khung làm việc dự báo sớm mức suy giảm Specific Flux trước nhiều ngày vận hành.
- Người vận hành chủ động kích hoạt chu kỳ rửa ngược hoặc tẩy rửa hóa chất nhẹ tại chỗ (maintenance cleaning).
- Quy trình giúp tối ưu hóa thời gian ngưng máy và kéo dài chu kỳ làm sạch sâu bằng hóa chất mạnh (CIP).

#### 4.2.3 Khả năng hiệp đồng với mô hình động học vật lý
- Mô hình học máy không nhằm thay thế hoàn toàn các mô hình cơ chế truyền thống.
- Khung dự báo bổ trợ dữ liệu thực nghiệm cho các mô phỏng động học màng sinh học (biofilm dynamics simulations).
- Sự kết hợp này bù đắp những thiếu sót của các cảm biến đo lường truyền thống tại nhà máy.
- Hệ thống hỗ trợ ra quyết định cung cấp dữ liệu đầu vào tin cậy để kỹ sư thiết lập kế hoạch vận hành tối ưu.

### 4.3 Các hạn chế của nghiên cứu (Study Limitations)

#### 4.3.1 Giới hạn về quy mô và tính đa dạng của dữ liệu
- Bộ dữ liệu thực nghiệm gồm 194 bản ghi ngày liên tục tại một hệ thống MBR duy nhất.
- Quy mô mẫu hạn chế khả năng tổng quát hóa mô hình cho các cấu hình màng khác như màng tấm phẳng (Flat Sheet) hay màng dạng ống (Tubular).
- Khoảng thời gian theo dõi chưa bao quát toàn bộ chu kỳ thời tiết bốn mùa để đánh giá biến động nhiệt độ dài hạn.
- Nghiên cứu tập trung vào nước thải chế biến thực phẩm nên các thông số động học vi sinh mang tính chất đặc thù ngành.

#### 4.3.2 Thiếu hụt dữ liệu về các biến cố vận hành cực đoan
- Bộ dữ liệu chưa ghi nhận đầy đủ chu kỳ phục hồi độ thấm sau các đợt tẩy rửa hóa chất phục hồi chuyên sâu (CIP).
- Tác động tích tụ của các hợp chất vô cơ khó rửa chưa được đánh giá đầy đủ qua chuỗi ngày thử nghiệm.
- Dữ liệu chưa trải qua các biến cố sốc tải thủy lực lớn hoặc sốc tải chất ô nhiễm hữu cơ bất thường do sự cố nhà máy.
- Mô hình xem hệ sinh thái vi sinh vật ở trạng thái giả định ổn định và chưa đo lường biến động thành phần chủng loài vi khuẩn.

### 4.4 Khả năng mở rộng phương pháp luận (Methodological Scalability & Transferability)

#### 4.4.1 Chuyển giao sang công nghệ lọc màng áp lực RO và FO
- Hiện tượng tắc màng trong hệ thống thẩm thấu ngược (RO) và thẩm thấu thuận (FO) cũng mang tính chất phụ thuộc thời gian.
- Tốc độ suy giảm thông lượng màng RO chịu tác động trực tiếp từ biến động áp suất và dao động lưu lượng cấp.
- Nguyên lý xây dựng thông số động Specific Flux ($J_{spec} = \frac{J}{\text{TMP}}$) và kỹ thuật trung bình trượt có thể áp dụng trực tiếp cho màng RO.
- Kỹ sư cần bổ sung các biến số đặc thù của quy trình như chỉ số bão hòa Langelier (LSI) và nồng độ ion khoáng gây đóng cặn (mineral scaling).
- Quy trình xử lý dữ liệu phân phối lệch và lọc nhiễu vận hành vẫn giữ nguyên giá trị cốt lõi trên các hệ thống FO-RO khử mặn.

#### 4.4.2 Ứng dụng cho các ngành xử lý nước thải công nghiệp khác
- Quy trình tiền xử lý Robust Scaling và MA-5 phù hợp với các nguồn nước thải công nghiệp có tính biến động mạnh.
- Phương pháp luận có thể chuyển giao hiệu quả sang các trạm MBR xử lý nước thải dệt nhuộm, hóa chất, dược phẩm và nước rỉ rác.
- Khung cấu trúc mô hình CatBoost cho phép tái sử dụng quy trình xử lý dữ liệu mà không cần tái cấu trúc từ đầu.
- Doanh nghiệp có thể điều chỉnh lại các trọng số đặc trưng thông qua kỹ thuật huấn luyện tinh chỉnh (fine-tuning).

### 4.5 Định hướng nghiên cứu và ứng dụng tương lai (Future Perspectives & Practical Roadmap)

#### 4.5.1 Tích hợp hệ thống IoT giám sát và điện toán biên
- Tích hợp mô hình dự báo CatBoost trực tiếp vào hệ thống điều khiển giám sát SCADA của nhà máy.
- Triển khai mô hình lên các thiết bị điện toán biên (Edge Computing) để giảm độ trễ xử lý dữ liệu.
- Kết nối dòng dữ liệu trực tuyến từ các cảm biến đo áp suất, lưu lượng, độ đục và COD online với tần suất cao.
- Xây dựng giao diện điều khiển hiển thị biểu đồ đóng góp SHAP thời gian thực cho kỹ sư giám sát trạm.

#### 4.5.2 Phát triển chiến lược điều khiển thích ứng vòng kín
- Ứng dụng dự báo suy giảm Specific Flux để điều khiển thích ứng lưu lượng khí cấp cho hệ thống sục khí màng.
- Giảm cường độ sục khí trong các giai đoạn rủi ro tắc màng thấp nhằm cắt giảm chi phí năng lượng điện tiêu thụ.
- Tăng cường độ bọt khí tức thời khi phát hiện nguy cơ lắng đọng bùn cao để gia tăng lực cắt bề mặt màng.
- Điều chỉnh linh hoạt tốc độ xả bùn dư để kiểm soát nồng độ MLSS và duy trì tỷ lệ F/M tối ưu theo khuyến nghị SHAP ($F/M \le 0.15\text{ kg COD/kg MLSS}\cdot\text{d}$).
- Tự động thay đổi tỷ lệ thời gian giữa chu kỳ hút lọc, chu kỳ nghỉ và chu kỳ rửa ngược dựa trên dự báo tốc độ tắc màng.

#### 4.5.3 Xây dựng cơ sở dữ liệu mở và học chuyển giao đa nhà máy
- Thiết lập các bộ dữ liệu đo đạc mở dài hạn từ nhiều nhà máy MBR với cấu hình sợi rỗng và tấm phẳng khác nhau.
- Áp dụng kỹ thuật học chuyển giao (Transfer Learning) để triển khai nhanh mô hình cho các trạm xử lý mới mà không cần tích lũy dữ liệu nhiều năm.
- Xây dựng các tiêu chuẩn chung về tiền xử lý dữ liệu và đánh giá độ tin cậy của mô hình AI trong ngành kỹ thuật môi trường nước.

### 4.6 Tổng hợp các công trình tham khảo trọng yếu (References & Analytical Synthesis)

#### 4.6.1 Phân loại các trụ cột nghiên cứu tham chiếu
- Nhóm cơ chế tắc nghẽn và mô hình sinh học trong MBR: Meng et al. (2009, 2017), Mannina et al. (2023), Iorhemen et al. (2016), Benyahia et al. (2024), Kim et al. (2011, 2013), Sandoval-García et al. (2025), Du et al. (2020), Al-Asheh et al. (2021).
- Nhóm giám sát chuỗi thời gian và công nghệ màng: Galinha et al. (2011), Fortunato et al. (2018), Paul (2011), Niu et al. (2022), Wang et al. (2023), Dagher et al. (2023).
- Nhóm ứng dụng học máy và trí tuệ nhân tạo dự đoán tắc nghẽn MBR: Niu et al. (2022, 2023), Shi et al. (2021), Frontistis et al. (2023a, 2023b), Abuwatfa et al. (2023), Schmitt et al. (2018), Hazrati et al. (2017), Viet & Jang (2021), Ahmad Yasmin et al. (2017), Li & Tao (2017), Wang et al. (2023), Zhong et al. (2022).
- Nhóm kỹ thuật giải thích mô hình AI (XAI) và phân tích thống kê dữ liệu: Rudin (2019), Savage (2022), Mersha et al. (2024), Zhang et al. (2023), Bourget (2023), Baarimah et al. (2024).
- Nhóm động học lọc, chế độ vận hành và công nghệ RO/FO: Miller et al. (2014), Hong et al. (2019), Yi et al. (2021), Goi & Liang (2025), Lim et al. (2025), Cirillo et al. (2021), Morales et al. (2024), Rahman et al. (2023), Burman & Sinha (2018), APHA (2017).

#### 4.6.2 Danh mục chi tiết 46 tài liệu tham khảo theo định dạng chuẩn
1. Meng, F.; Chae, S.-R.; Drews, A.; Kraume, M.; Shin, H.-S.; Yang, F. Recent advances in membrane bioreactors (MBRs): Membrane fouling and membrane material. *Water Res.* 2009, 43, 1489–1512. https://doi.org/10.1016/j.watres.2008.12.044
2. Shi, Y.; Wang, Z.; Du, X.; Gong, B.; Jegatheesan, V.; Haq, I.U. Recent advances in the prediction of fouling in membrane bioreactors. *Membranes* 2021, 11, 381. https://doi.org/10.3390/membranes11060381
3. Rahman, T.U.; Roy, H.; Islam, M.R.; Tahmid, M.; Fariha, A.; Mazumder, A.; Tasnim, N.; Pervez, M.N.; Cai, Y.; Naddeo, V. The advancement in membrane bioreactor (MBR) technology toward sustainable industrial wastewater management. *Membranes* 2023, 13, 181. https://doi.org/10.3390/membranes13020181
4. Burman, I.; Sinha, A. A review on membrane fouling in membrane bioreactors: Control and mitigation. In *Environmental Contaminants: Measurement, Modelling and Control*; Springer: Singapore, 2018; pp. 281–315. https://doi.org/10.1007/978-981-10-7332-8_13
5. Meng, F.; Zhang, S.; Oh, Y.; Zhou, Z.; Shin, H.-S.; Chae, S.-R. Fouling in membrane bioreactors: An updated review. *Water Res.* 2017, 114, 151–180. https://doi.org/10.1016/j.watres.2017.02.033
6. Kim, M.; Sankararao, B.; Yoo, C. Determination of MBR fouling and chemical cleaning interval using statistical methods applied on dynamic index data. *J. Membr. Sci.* 2011, 375, 345–353. https://doi.org/10.1016/j.memsci.2011.04.004
7. Iorhemen, O.T.; Hamza, R.A.; Tay, J.H. Membrane bioreactor (MBR) technology for wastewater treatment and reclamation: Membrane fouling. *Membranes* 2016, 6, 33. https://doi.org/10.3390/membranes6020033
8. Morales, N.; Mery-Araya, C.; Guerra, P.; Poblete, R.; Chacana-Olivares, J. Mitigation of Membrane Fouling in Membrane Bioreactors Using Granular and Powdered Activated Carbon: An Experimental Study. *Water* 2024, 16, 2556. https://doi.org/10.3390/w16182556
9. Lim, Y.J.; Goh, K.; Nadzri, N.; Wang, R. Thin-film composite (TFC) membranes for sustainable desalination and water reuse: A perspective. *Desalination* 2025, 599, 118451. https://doi.org/10.1016/j.desal.2024.118451
10. Mannina, G.; Ni, B.-J.; Makinia, J.; Harmand, J.; Alliet, M.; Brepols, C.; Ruano, M.V.; Robles, A.; Heran, M.; Gulhan, H. Biological processes modelling for MBR systems: A review of the state-of-the-art focusing on SMP and EPS. *Water Res.* 2023, 242, 120275. https://doi.org/10.1016/j.watres.2023.120275
11. Benyahia, B.; Charfi, A.; Lesage, G.; Heran, M.; Cherki, B.; Harmand, J. Coupling a simple and generic membrane fouling model with biological dynamics: Application to the modeling of an Anaerobic Membrane BioReactor (AnMBR). *Membranes* 2024, 14, 69. https://doi.org/10.3390/membranes14030069
12. Kim, M.; Sankararao, B.; Lee, S.; Yoo, C. Prediction and identification of membrane fouling mechanism in a membrane bioreactor using a combined mechanistic model. *Ind. Eng. Chem. Res.* 2013, 52, 17198–17205. https://doi.org/10.1021/ie4020977
13. Sandoval-García, V.; Ruano, M.; Alliet, M.; Brepols, C.; Comas, J.; Harmand, J.; Heran, M.; Mannina, G.; Rodriguez-Roda, I.; Smets, I. Modeling MBR fouling: A critical review analysis towards establishing a framework for good modeling practices. *Water Res.* 2025, 268, 122611. https://doi.org/10.1016/j.watres.2024.122611
14. Paul, P. Investigation of a MBR membrane fouling model based on time series analysis system identification methods. *Desalination Water Treat.* 2011, 35, 92–100. https://doi.org/10.5004/dwt.2011.3134
15. Galinha, C.; Carvalho, G.; Portugal, C.; Guglielmi, G.; Oliveira, R.; Crespo, J.; Reis, M. Real-time monitoring of membrane bioreactors with 2D-fluorescence data and statistically based models. *Water Sci. Technol.* 2011, 63, 1381–1388. https://doi.org/10.2166/wst.2011.378
16. Fortunato, L.; Pathak, N.; Rehman, Z.U.; Shon, H.; Leiknes, T. Real-time monitoring of membrane fouling development during early stages of activated sludge membrane bioreactor operation. *Process Saf. Environ. Prot.* 2018, 120, 313–320. https://doi.org/10.1016/j.psep.2018.09.014
17. Niu, B.; Yang, L.; Meng, S.; Liang, D.; Liu, H.; Yang, L.; Shen, L.; Zhao, Q. Time-dependent analysis of polysaccharide fouling by Hermia models: Reveal the structure of fouling layer. *Sep. Purif. Technol.* 2022, 302, 122093. https://doi.org/10.1016/j.seppur.2022.122093
18. Wang, Y.; Zheng, X.; Xiao, K.; Xue, J.; Ulbricht, M.; Zhang, Y. How and why does time matter-A comparison of fouling caused by organic substances on membranes over adsorption durations. *Sci. Total Environ.* 2023, 866, 160655. https://doi.org/10.1016/j.scitotenv.2022.160655
19. Ahmad Yasmin, N.S.; Abdul Wahab, N.; Yusuf, Z. Modeling of membrane bioreactor of wastewater treatment using support vector machine. In *Modeling, Design and Simulation of Systems, Proceedings of the 17th Asia Simulation Conference (AsiaSim 2017)*, Melaka, Malaysia, 27–29 August 2017; Proceedings, Part II 17; Springer: Singapore, 2017; pp. 485–495. https://doi.org/10.1007/978-981-10-6502-6_42
20. Niu, C.; Li, X.; Dai, R.; Wang, Z. Artificial intelligence-incorporated membrane fouling prediction for membrane-based processes in the past 20 years: A critical review. *Water Res.* 2022, 216, 118299. https://doi.org/10.1016/j.watres.2022.118299
21. Abuwatfa, W.H.; AlSawaftah, N.; Darwish, N.; Pitt, W.G.; Husseini, G.A. A review on membrane fouling prediction using artificial neural networks (ANNs). *Membranes* 2023, 13, 685. https://doi.org/10.3390/membranes13070685
22. Niu, C.; Li, B.; Wang, Z. Using artificial intelligence-based algorithms to identify critical fouling factors and predict fouling behavior in anaerobic membrane bioreactors. *J. Membr. Sci.* 2023, 687, 122076. https://doi.org/10.1016/j.memsci.2023.122076
23. Frontistis, Z.; Lykogiannis, G.; Sarmpanis, A. Artificial Neural Networks in Membrane Bioreactors: A Comprehensive Review—Overcoming Challenges and Future Perspectives. *Sci* 2023, 5, 31. https://doi.org/10.3390/sci5030031
24. Frontistis, Z.; Lykogiannis, G.; Sarmpanis, A. Machine learning implementation in membrane bioreactor systems: Progress, challenges, and future perspectives: A review. *Environments* 2023, 10, 127. https://doi.org/10.3390/environments10080127
25. Maere, T.; Villez, K.; Marsili-Libelli, S.; Naessens, W.; Nopens, I. Membrane bioreactor fouling behaviour assessment through principal component analysis and fuzzy clustering. *Water Res.* 2012, 46, 6132–6142. https://doi.org/10.1016/j.watres.2012.08.028
26. Wang, Z.; Zeng, J.; Shi, Y.; Ling, G. MBR membrane fouling diagnosis based on improved residual neural network. *J. Environ. Chem. Eng.* 2023, 11, 109742. https://doi.org/10.1016/j.jece.2023.109742
27. Zhong, H.; Yuan, Y.; Luo, L.; Ye, J.; Chen, M.; Zhong, C. Water quality prediction of MBR based on machine learning: A novel dataset contribution analysis method. *J. Water Process Eng.* 2022, 50, 103296. https://doi.org/10.1016/j.jwpe.2022.103296
28. Zhang, S.; Jin, Y.; Chen, W.; Wang, J.; Wang, Y.; Ren, H. Artificial intelligence in wastewater treatment: A data-driven analysis of status and trends. *Chemosphere* 2023, 336, 139163. https://doi.org/10.1016/j.chemosphere.2023.139163
29. Savage, N. Breaking into the black box of artificial intelligence. *Nature* 2022. https://doi.org/10.1038/d41586-022-00858-1
30. Rudin, C. Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead. *Nat. Mach. Intell.* 2019, 1, 206–215. https://doi.org/10.1038/s42256-019-0048-x
31. Mersha, M.; Lam, K.; Wood, J.; AlShami, A.K.; Kalita, J. Explainable artificial intelligence: A survey of needs, techniques, applications, and future direction. *Neurocomputing* 2024, 599, 128111. https://doi.org/10.1016/j.neucom.2024.128111
32. Bourget, G. Statistical analysis of wastewater treatment plant data. *SN Appl. Sci.* 2023, 5, 130. https://doi.org/10.1007/s42452-023-05353-8
33. Baarimah, A.O.; Bazel, M.A.; Alaloul, W.S.; Alazaiza, M.Y.; Al-Zghoul, T.M.; Almuhaya, B.; Khan, A.; Mushtaha, A.W. Artificial intelligence in wastewater treatment: Research trends and future perspectives through bibliometric analysis. *Case Stud. Chem. Environ. Eng.* 2024, 10, 100926. https://doi.org/10.1016/j.cscee.2024.100926
34. Cirillo, A.I.; Tomaiuolo, G.; Guido, S. Membrane fouling phenomena in microfluidic systems: From technical challenges to scientific opportunities. *Micromachines* 2021, 12, 820. https://doi.org/10.3390/mi12070820
35. Dagher, G.; Martin, A.; Galharret, J.M.; Moulin, L.; Croué, J.P.; Teychene, B. Forecasting multicycle hollow fiber ultrafiltration fouling using time series analysis. *J. Water Process Eng.* 2023, 56, 104441. https://doi.org/10.1016/j.jwpe.2023.104441
36. Goi, Y.; Liang, Y. A general modeling framework for FO spiral-wound membrane and its fouling impact on FO-RO desalination system. *Desalination* 2025, 593, 118236. https://doi.org/10.1016/j.desal.2024.118236
37. Hazrati, H.; Moghaddam, A.H.; Rostamizadeh, M. The influence of hydraulic retention time on cake layer specifications in the membrane bioreactor: Experimental and artificial neural network modeling. *J. Environ. Chem. Eng.* 2017, 5, 3005–3013. https://doi.org/10.1016/j.jece.2017.06.002
38. Schmitt, F.; Banu, R.; Yeom, I.-T.; Do, K.-U. Development of artificial neural networks to predict membrane fouling in an anoxic-aerobic membrane bioreactor treating domestic wastewater. *Biochem. Eng. J.* 2018, 133, 47–58. https://doi.org/10.1016/j.bej.2018.01.028
39. Viet, N.D.; Jang, A. Development of artificial intelligence-based models for the prediction of filtration performance and membrane fouling in an osmotic membrane bioreactor. *J. Environ. Chem. Eng.* 2021, 9, 105337. https://doi.org/10.1016/j.jece.2021.105337
40. Li, C.; Tao, Y. Application of support vector machine with simulated annealing algorithm in MBR membrane pollution prediction. In *Proceedings of the 2017 IEEE 15th International Conference on Software Engineering Research, Management and Applications (SERA)*, London, UK, 7–9 June 2017; pp. 211–217. https://doi.org/10.1109/SERA.2017.7965730
41. Miller, D.J.; Kasemset, S.; Paul, D.R.; Freeman, B.D. Comparison of membrane fouling at constant flux and constant transmembrane pressure conditions. *J. Membr. Sci.* 2014, 454, 505–515. https://doi.org/10.1016/j.memsci.2013.12.027
42. Hong, P.-N.; Noguchi, M.; Matsuura, N.; Honda, R. Mechanism of biofouling enhancement in a membrane bioreactor under constant trans-membrane pressure operation. *J. Membr. Sci.* 2019, 592, 117391. https://doi.org/10.1016/j.memsci.2019.117391
43. Yi, X.; Zhang, M.; Song, W.; Wang, X. Effect of Initial Water Flux on the Performance of Anaerobic Membrane Bioreactor: Constant Flux Mode versus Varying Flux Mode. *Membranes* 2021, 11, 203. https://doi.org/10.3390/membranes11030203
44. Du, X.; Shi, Y.; Jegatheesan, V.; Haq, I.U. A review on the mechanism, impacts and control methods of membrane fouling in MBR system. *Membranes* 2020, 10, 24. https://doi.org/10.3390/membranes10020024
45. Al-Asheh, S.; Bagheri, M.; Aidan, A. Membrane bioreactor for wastewater treatment: A review. *Case Stud. Chem. Environ. Eng.* 2021, 4, 100109. https://doi.org/10.1016/j.cscee.2021.100109
46. American Public Health Association (APHA). *Standard Methods for the Examination of Water and Wastewater*, 23rd ed.; APHA: Washington, DC, USA, 2017.

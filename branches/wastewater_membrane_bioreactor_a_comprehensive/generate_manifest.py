import json
import os
import tiktoken
import sys

sys.stdout.reconfigure(encoding='utf-8')
enc = tiktoken.get_encoding('cl100k_base')

out_dir = r"C:\antgravity workplace\ML\PAPER TAB AUTOML\branche\wastewater_membrane_bioreactor_a_comprehensive"
doc_slug = "wastewater_membrane_bioreactor_a_comprehensive"
manifest_path = os.path.join(out_dir, f"{doc_slug}_scout_manifest.json")

manifest = {
    "doc_slug": doc_slug,
    "doc_title": "Wastewater Membrane Bioreactors: A Comprehensive Review of Explainable Artificial Intelligence and Digital Twin Applications",
    "total_pages": 26,
    "total_estimated_tokens": 22323,
    "master_skeleton": [
        {
            "level": 1,
            "title": "Phần mở đầu và Tóm tắt tổng quan (Abstract and Frontmatter)",
            "start_page": 1,
            "end_page": 1,
            "word_count": 393,
            "has_exercises": False,
            "children": []
        },
        {
            "level": 1,
            "title": "Chương 1: Giới thiệu Tổng quan về MBR, Thách thức Vận hành và Hội tụ Công nghệ (1. Introduction)",
            "start_page": 1,
            "end_page": 4,
            "word_count": 1283,
            "has_exercises": False,
            "children": [
                {
                    "level": 2,
                    "title": "1.1 Bối cảnh phát triển và Ưu thế của công nghệ MBR (Development Context & Advantages of MBR)",
                    "start_page": 1,
                    "end_page": 2,
                    "word_count": 179,
                    "has_exercises": False,
                    "children": []
                },
                {
                    "level": 2,
                    "title": "1.2 Hai điểm nghẽn cố hữu: Tắc nghẽn màng và Tiêu hao năng lượng (Structural Liabilities: Membrane Fouling & High Energy Demand)",
                    "start_page": 2,
                    "end_page": 2,
                    "word_count": 268,
                    "has_exercises": False,
                    "children": []
                },
                {
                    "level": 2,
                    "title": "1.3 Tiềm năng của Học máy và Rào cản mô hình hộp đen (The Machine Learning Opportunity & Black-Box Opacity Barrier)",
                    "start_page": 2,
                    "end_page": 3,
                    "word_count": 166,
                    "has_exercises": False,
                    "children": []
                },
                {
                    "level": 2,
                    "title": "1.4 Chuỗi hội tụ ba tầng: Học máy, Trí tuệ nhân tạo giải thích được và Bản sao số (The Triad Convergence: ML, XAI & Digital Twins)",
                    "start_page": 3,
                    "end_page": 3,
                    "word_count": 330,
                    "has_exercises": False,
                    "children": []
                },
                {
                    "level": 2,
                    "title": "1.5 Mục tiêu bài tổng quan và Khung khái niệm tích hợp (Review Objectives & Conceptual Framework - Figure 1)",
                    "start_page": 3,
                    "end_page": 4,
                    "word_count": 340,
                    "has_exercises": False,
                    "children": []
                }
            ]
        },
        {
            "level": 1,
            "title": "Chương 2: Phương pháp luận và Tiêu chí Tổng quan Tài liệu (2. Methodology)",
            "start_page": 4,
            "end_page": 5,
            "word_count": 246,
            "has_exercises": False,
            "children": [
                {
                    "level": 2,
                    "title": "2.1 Chiến lược tìm kiếm và Cơ sở dữ liệu khoa học (Literature Search Strategy & Database Sources)",
                    "start_page": 4,
                    "end_page": 4,
                    "word_count": 159,
                    "has_exercises": False,
                    "children": []
                },
                {
                    "level": 2,
                    "title": "2.2 Tiêu chí chọn lọc và Đánh giá chất lượng thực nghiệm (Study Selection Criteria & Empirical Quality Safeguards)",
                    "start_page": 4,
                    "end_page": 5,
                    "word_count": 87,
                    "has_exercises": False,
                    "children": []
                }
            ]
        },
        {
            "level": 1,
            "title": "Chương 3: Ứng dụng Học máy trong Dự đoán Tắc nghẽn Màng (3. Machine Learning for Membrane Fouling Prediction)",
            "start_page": 5,
            "end_page": 11,
            "word_count": 3146,
            "has_exercises": False,
            "children": [
                {
                    "level": 2,
                    "title": "3.1 Cơ chế tắc nghẽn và Bối cảnh mô hình hóa (3.1. Fouling Mechanisms and Modelling Context)",
                    "start_page": 5,
                    "end_page": 6,
                    "word_count": 619,
                    "has_exercises": False,
                    "children": []
                },
                {
                    "level": 2,
                    "title": "3.2 Các mô hình học máy cơ bản và Dựa trên hạt nhân (3.2. Shallow and Kernel-Based ML Models)",
                    "start_page": 6,
                    "end_page": 7,
                    "word_count": 626,
                    "has_exercises": False,
                    "children": []
                },
                {
                    "level": 2,
                    "title": "3.3 Các phương pháp tập hợp và Học sâu (3.3. Ensemble Methods and Deep Learning)",
                    "start_page": 7,
                    "end_page": 9,
                    "word_count": 878,
                    "has_exercises": False,
                    "children": []
                },
                {
                    "level": 2,
                    "title": "3.4 Hạn chế của tập dữ liệu, Nguy cơ quá khớp và Khả năng tổng quát hóa liên cơ sở (3.4. Dataset Limitations, Overfitting Risk, and Cross-Site Generalization)",
                    "start_page": 9,
                    "end_page": 11,
                    "word_count": 1016,
                    "has_exercises": False,
                    "children": []
                }
            ]
        },
        {
            "level": 1,
            "title": "Chương 4: Trí tuệ Nhân tạo có thể Giải thích trong Hệ thống MBR (4. Explainable Artificial Intelligence in MBR Applications)",
            "start_page": 11,
            "end_page": 14,
            "word_count": 1850,
            "has_exercises": False,
            "children": [
                {
                    "level": 2,
                    "title": "4.1 Yêu cầu bắt buộc về tính khả giải trong hệ thống xử lý nước được quản lý nghiêm ngặt (4.1. The Explainability Imperative in Regulated Water Systems)",
                    "start_page": 11,
                    "end_page": 11,
                    "word_count": 272,
                    "has_exercises": False,
                    "children": []
                },
                {
                    "level": 2,
                    "title": "4.2 SHAP: Khung giải thích chủ đạo trong nghiên cứu MBR (4.2. SHAP: Dominant XAI Framework in MBR Studies)",
                    "start_page": 11,
                    "end_page": 13,
                    "word_count": 902,
                    "has_exercises": False,
                    "children": []
                },
                {
                    "level": 2,
                    "title": "4.3 LIME, Đồ thị phụ thuộc một phần (PDP) và Các phương pháp dựa trên gradient (4.3. LIME, Partial Dependence Plots, and Gradient-Based Methods)",
                    "start_page": 13,
                    "end_page": 14,
                    "word_count": 669,
                    "has_exercises": False,
                    "children": []
                }
            ]
        },
        {
            "level": 1,
            "title": "Chương 5: Tối ưu hóa Năng lượng Tiêu thụ trong Hệ thống MBR bằng Học máy (5. ML-Driven Energy Optimization in MBR Systems)",
            "start_page": 14,
            "end_page": 16,
            "word_count": 1066,
            "has_exercises": False,
            "children": [
                {
                    "level": 2,
                    "title": "5.1 Cấu trúc tiêu thụ năng lượng và Các mục tiêu tối ưu hóa (5.1. Energy Consumption Structure and Optimization Targets)",
                    "start_page": 14,
                    "end_page": 15,
                    "word_count": 358,
                    "has_exercises": False,
                    "children": []
                },
                {
                    "level": 2,
                    "title": "5.2 Bằng chứng thực nghiệm về giảm tiêu hao năng lượng và Khoảng trống nghiên cứu (5.2. Confirmed Energy Reduction Evidence and Research Gap)",
                    "start_page": 15,
                    "end_page": 16,
                    "word_count": 701,
                    "has_exercises": False,
                    "children": []
                }
            ]
        },
        {
            "level": 1,
            "title": "Chương 6: Khung Kiến trúc Bản sao Số cho Hệ thống MBR (6. Digital Twin Frameworks for MBR Systems)",
            "start_page": 16,
            "end_page": 19,
            "word_count": 1755,
            "has_exercises": False,
            "children": [
                {
                    "level": 2,
                    "title": "6.1 Kiến trúc, Các thành phần và Các bậc trưởng thành công nghệ (6.1. Architecture, Components, and Maturity Tiers)",
                    "start_page": 16,
                    "end_page": 17,
                    "word_count": 528,
                    "has_exercises": False,
                    "children": []
                },
                {
                    "level": 2,
                    "title": "6.2 Tích hợp XAI vào Kiến trúc Ra quyết định của Bản sao Số (6.2. XAI Integration in Digital Twin Decision Architecture)",
                    "start_page": 17,
                    "end_page": 19,
                    "word_count": 1220,
                    "has_exercises": False,
                    "children": []
                }
            ]
        },
        {
            "level": 1,
            "title": "Chương 7: Chín Khoảng trống Nghiên cứu Then chốt và Định hướng Tương lai (7. Research Gaps and Future Directions)",
            "start_page": 19,
            "end_page": 22,
            "word_count": 1505,
            "has_exercises": False,
            "children": [
                {
                    "level": 2,
                    "title": "7.1 Khoảng trống 1: Sự khan hiếm tập dữ liệu chuẩn mở đa cơ sở (Gap 1: Scarcity of Benchmark Datasets)",
                    "start_page": 20,
                    "end_page": 20,
                    "word_count": 374,
                    "has_exercises": False,
                    "children": []
                },
                {
                    "level": 2,
                    "title": "7.2 Khoảng trống 2: Thiếu hụt định lượng độ bất định trong dự đoán (Gap 2: Absence of Uncertainty Quantification - UQ)",
                    "start_page": 20,
                    "end_page": 20,
                    "word_count": 152,
                    "has_exercises": False,
                    "children": []
                },
                {
                    "level": 2,
                    "title": "7.3 Khoảng trống 3: Thiếu vắng triển khai Bản sao số tích hợp XAI ở quy mô thực tế (Gap 3: Lack of Full-Scale DT Deployments with Integrated XAI)",
                    "start_page": 20,
                    "end_page": 21,
                    "word_count": 155,
                    "has_exercises": False,
                    "children": []
                },
                {
                    "level": 2,
                    "title": "7.4 Khoảng trống 4: Hạn chế trong đặc tính hóa động học nước thải đầu vào (Gap 4: Dynamic Influent Characterization Limitations)",
                    "start_page": 21,
                    "end_page": 21,
                    "word_count": 144,
                    "has_exercises": False,
                    "children": []
                },
                {
                    "level": 2,
                    "title": "7.5 Khoảng trống 5: Rào cản và khung công nhận pháp lý cho XAI (Gap 5: Regulatory Dimension and Acceptance Frameworks for XAI)",
                    "start_page": 21,
                    "end_page": 21,
                    "word_count": 154,
                    "has_exercises": False,
                    "children": []
                },
                {
                    "level": 2,
                    "title": "7.6 Khoảng trống 6: Chi phí kinh tế phát triển và bảo trì mô hình ML (Gap 6: Economic Cost of ML Model Development and Retraining)",
                    "start_page": 21,
                    "end_page": 22,
                    "word_count": 233,
                    "has_exercises": False,
                    "children": []
                },
                {
                    "level": 2,
                    "title": "7.7 Khoảng trống 7: Yêu cầu về nguồn nhân lực vận hành hệ thống DT và XAI (Gap 7: Human Capital and Workforce Requirements)",
                    "start_page": 22,
                    "end_page": 22,
                    "word_count": 80,
                    "has_exercises": False,
                    "children": []
                },
                {
                    "level": 2,
                    "title": "7.8 Khoảng trống 8: Thiếu đối chuẩn hệ thống với các phương pháp điều khiển phi-ML (Gap 8: Inadequate Baselines and Benchmarking against Non-ML Alternatives)",
                    "start_page": 22,
                    "end_page": 22,
                    "word_count": 68,
                    "has_exercises": False,
                    "children": []
                },
                {
                    "level": 2,
                    "title": "7.9 Khoảng trống 9: Dấu chân carbon và tiêu hao năng lượng tính toán của AI (Gap 9: Carbon and Computational Energy Footprint of AI)",
                    "start_page": 22,
                    "end_page": 22,
                    "word_count": 76,
                    "has_exercises": False,
                    "children": []
                }
            ]
        },
        {
            "level": 1,
            "title": "Chương 8: Kết luận Tổng hợp và Khung Chiến lược Vận hành Thông minh (8. Conclusions & Strategic Roadmap)",
            "start_page": 22,
            "end_page": 23,
            "word_count": 548,
            "has_exercises": False,
            "children": [
                {
                    "level": 2,
                    "title": "8.1 Tổng kết 4 mục tiêu nghiên cứu và Đánh giá thực trạng công nghệ (Summary of Four Review Objectives & State of Technology)",
                    "start_page": 22,
                    "end_page": 23,
                    "word_count": 437,
                    "has_exercises": False,
                    "children": []
                },
                {
                    "level": 2,
                    "title": "8.2 Lộ trình chuyển đổi từ Nghiên cứu sang Triển khai Công nghiệp (Operational Transition Roadmap & Governance Safeguards)",
                    "start_page": 23,
                    "end_page": 23,
                    "word_count": 111,
                    "has_exercises": False,
                    "children": []
                }
            ]
        },
        {
            "level": 1,
            "title": "Tài liệu Tham khảo (References)",
            "start_page": 23,
            "end_page": 26,
            "word_count": 1977,
            "has_exercises": False,
            "children": []
        }
    ],
    "global_lexicon": {
        "core_thesis": "Hệ thống bể phản ứng màng sinh học (MBR) xử lý nước thải đối mặt hai thách thức lớn: hiện tượng tắc nghẽn màng làm tăng áp suất qua màng (TMP) và tiêu hao năng lượng sục khí cao (chiếm 60–75% tổng năng lượng). Chuỗi công nghệ tích hợp gồm Học máy (ML), Trí tuệ nhân tạo giải thích được (XAI) và Bản sao số (Digital Twin - DT) giải quyết triệt để hai thách thức này. ML cung cấp khả năng dự báo phi tuyến chính xác cao. XAI minh bạch hóa các quyết định hộp đen để vượt qua rào cản kiểm định pháp lý và tạo dựng niềm tin cho người vận hành. Digital Twin đóng vai trò nền tảng tích hợp thời gian thực giữa mô hình cơ chế sinh học (họ ASM) với mô hình dữ liệu để hướng tới điều khiển kê đơn tự động (Tier III). Mặc dù các mô hình tập hợp (Random Forest) và học sâu (LSTM) đạt độ chính xác cao trên dữ liệu tĩnh (R² = 0.85–0.99), việc triển khai vận hành thực tế tại trạm thương mại vẫn bị cản trở bởi 9 khoảng trống nghiên cứu then chốt, đặc biệt là sự khan hiếm tập dữ liệu chuẩn mở đa cơ sở, thiếu định lượng độ bất định (UQ) và chưa có kiểm chứng điều khiển vòng kín trực tiếp.",
        "key_terms": [
            {
                "term": "MBR (Membrane Bioreactor)",
                "definition": "Bể phản ứng màng sinh học. Hệ thống xử lý nước thải kết hợp bùn hoạt tính sinh học với quá trình phân tách màng vi lọc (MF) hoặc siêu lọc (UF)."
            },
            {
                "term": "Membrane Fouling (Tắc nghẽn màng)",
                "definition": "Hiện tượng tích tụ chất bẩn, polyme sinh học và hạt keo lên bề mặt hoặc bên trong lỗ rỗng của màng lọc, gây giảm lưu lượng thấm và tăng áp suất lọc."
            },
            {
                "term": "TMP (Transmembrane Pressure - Áp suất qua màng)",
                "definition": "Hiệu số áp suất thủy tĩnh giữa hai phía màng lọc, là thông số đo lường trực tiếp mức độ tắc nghẽn màng trong vận hành MBR."
            },
            {
                "term": "Permeate Flux (Lưu lượng thấm qua màng)",
                "definition": "Thể tích nước sau xử lý đi qua một đơn vị diện tích màng trong một đơn vị thời gian (đơn vị: L/(m²·h) hoặc LMH)."
            },
            {
                "term": "Critical Flux (Dòng tới hạn)",
                "definition": "Ngưỡng lưu lượng thấm mà dưới mức này tắc nghẽn diễn ra rất chậm và có thể đảo ngược; vượt qua ngưỡng này, tắc nghẽn không thể đảo ngược tăng tốc nhanh."
            },
            {
                "term": "EPS (Extracellular Polymeric Substances)",
                "definition": "Các chất polyme ngoại bào do vi sinh vật tiết ra (chứa protein, polysaccharide), gồm dạng liên kết (bound EPS) và dạng hòa tan (SMP), là tác nhân chính gây tắc nghẽn màng."
            },
            {
                "term": "SMP (Soluble Microbial Products)",
                "definition": "Sản phẩm vi sinh hòa tan giải phóng trong quá trình trao đổi chất hoặc tự phân hủy của bùn hoạt tính, dễ thâm nhập gây bít tắc các lỗ rỗng màng siêu nhỏ."
            },
            {
                "term": "MLSS (Mixed Liquor Suspended Solids)",
                "definition": "Nồng độ chất rắn lơ lửng trong bùn lỏng (g/L), quyết định độ nhớt của bùn và lượng chất bẩn tạo thành lớp bánh cặn trên bề mặt màng."
            },
            {
                "term": "SRT (Sludge Retention Time)",
                "definition": "Thời gian lưu bùn (tuổi bùn), chi phối tốc độ sinh trưởng của vi sinh vật, đặc tính sinh học của bùn và tốc độ phát sinh polyme ngoại bào EPS."
            },
            {
                "term": "HRT (Hydraulic Retention Time)",
                "definition": "Thời gian lưu nước trong bể sinh học, ảnh hưởng đến tải trọng thể tích và thời gian tiếp xúc của các chất ô nhiễm keo với màng."
            },
            {
                "term": "DO (Dissolved Oxygen)",
                "definition": "Nồng độ oxy hòa tan trong bể bùn hoạt tính (mg/L), chi phối quá trình chuyển hóa chất hữu cơ, nitrat hóa và thành phần sinh học của EPS."
            },
            {
                "term": "Membrane Aeration (Sục khí màng)",
                "definition": "Quá trình thổi khí bọt thô liên tục hoặc ngắt quãng ngay dưới mô-đun màng để tạo lực cắt thủy lực cọ rửa bề mặt, làm chậm quá trình tích tụ bánh cặn."
            },
            {
                "term": "CIP (Clean-in-Place - Rửa màng tại chỗ)",
                "definition": "Quy trình ngâm rửa màng bằng hóa chất (axit, kiềm, chất oxy hóa) trực tiếp trong bể để phục hồi độ thấm mà không cần tháo dỡ mô-đun màng."
            },
            {
                "term": "Resistance-in-Series Model (Mô hình dãy trở lực)",
                "definition": "Khung lý thuyết phân chia tổng trở lực màng thành trở lực màng sạch (Rm), trở lực bánh cặn đảo ngược được (Rc) và trở lực bít lỗ không đảo ngược (Rp)."
            },
            {
                "term": "ASM (Activated Sludge Models)",
                "definition": "Họ mô hình toán học cơ chế (ASM1, ASM2d, ASM3) do Hiệp hội Nước Quốc tế (IWA) phát triển để mô phỏng động học sinh hóa phân hủy hữu cơ và dưỡng chất."
            },
            {
                "term": "BSM-MBR (Benchmark Simulation Model for MBR)",
                "definition": "Mô hình chuẩn mô phỏng tích hợp quá trình sinh học bùn hoạt tính và tách lọc màng, dùng để đối sánh các thuật toán điều khiển và tiêu hao năng lượng."
            },
            {
                "term": "OMBR (Osmotic Membrane Bioreactor)",
                "definition": "Bể phản ứng sinh học màng thẩm thấu, kết hợp màng thẩm thấu thuận (FO) với xử lý sinh học, vận hành nhờ chênh lệch áp suất thẩm thấu thay vì áp suất cơ học."
            },
            {
                "term": "Random Forest (Rừng ngẫu nhiên)",
                "definition": "Thuật toán học máy tập hợp kết hợp nhiều cây quyết định, có độ bền vững cao với dữ liệu nhiễu, xử lý tốt quan hệ phi tuyến và cung cấp độ quan trọng của đặc trưng."
            },
            {
                "term": "LSTM (Long Short-Term Memory)",
                "definition": "Mạng nơ-ron hồi quy có cấu trúc cổng nhớ kiểm soát dòng thông tin, tối ưu hóa cho việc học các phụ thuộc chuỗi thời gian dài của áp suất TMP."
            },
            {
                "term": "LSSVM (Least Squares Support Vector Machine)",
                "definition": "Mô hình máy véc-tơ hỗ trợ bình phương tối thiểu, giải hệ phương trình đại số tuyến tính, đạt độ chính xác cao trên các tập dữ liệu phòng thí nghiệm quy mô nhỏ."
            },
            {
                "term": "XAI (Explainable Artificial Intelligence)",
                "definition": "Trí tuệ nhân tạo có thể giải thích. Các phương pháp toán học giúp làm sáng tỏ cơ chế ra quyết định của các mô hình học máy hộp đen đối với con người."
            },
            {
                "term": "SHAP (SHapley Additive exPlanations)",
                "definition": "Phương pháp giải thích mô hình dựa trên lý thuyết trò chơi hợp tác của Lloyd Shapley, phân bổ giá trị đóng góp công bằng của từng biến đầu vào cho kết quả dự đoán."
            },
            {
                "term": "LIME (Local Interpretable Model-agnostic Explanations)",
                "definition": "Phương pháp giải thích cục bộ độc lập mô hình, tạo mô hình thay thế tuyến tính xấp xỉ hành vi của mô hình hộp đen xung quanh một điểm dữ liệu xác định."
            },
            {
                "term": "PDP (Partial Dependence Plot) & ICE",
                "definition": "Biểu đồ phụ thuộc một phần (PDP) và đường kỳ vọng điều kiện cá thể (ICE), hiển thị tác động biên phi tuyến của một biến số lên kết quả dự báo."
            },
            {
                "term": "Integrated Gradients (Gradient tích phân)",
                "definition": "Kỹ thuật giải thích mô hình mạng nơ-ron bằng cách tính tích phân gradient dọc theo đường đi từ điểm dữ liệu cơ sở đến điểm quan sát thực tế."
            },
            {
                "term": "Digital Twin (Bản sao số)",
                "definition": "Mô hình ảo số hóa mô phỏng đồng bộ hai chiều theo thời gian thực với hệ thống vật lý thực tế, hỗ trợ giám sát, mô phỏng kịch bản và điều khiển tự động."
            },
            {
                "term": "Tier I Descriptive DT (Bản sao số bậc 1 - Mô tả)",
                "definition": "Cấp độ bản sao số hiển thị trạng thái vận hành, biểu đồ cảm biến SCADA và quản lý cảnh báo theo ngưỡng cố định, đã thương mại hóa phổ biến."
            },
            {
                "term": "Tier II Predictive DT (Bản sao số bậc 2 - Dự đoán)",
                "definition": "Cấp độ bản sao số dự báo trước biến trạng thái (TMP, chất lượng nước đầu ra) trước 12–72 giờ nhờ tích hợp mô hình học máy và mô hình cơ chế."
            },
            {
                "term": "Tier III Prescriptive DT (Bản sao số bậc 3 - Kê đơn/Chỉ dẫn)",
                "definition": "Cấp độ bản sao số điều khiển tự động vòng kín, tối ưu hóa điểm đặt sục khí và chu kỳ làm sạch, tích hợp XAI để giải thích quyết định cho người vận hành."
            },
            {
                "term": "UQ (Uncertainty Quantification - Định lượng độ bất định)",
                "definition": "Phương pháp ước tính khoảng tin cậy hoặc phân phối xác suất đi kèm dự đoán điểm của mô hình ML, đảm bảo an toàn cho các tác vụ điều khiển tự động."
            },
            {
                "term": "Concept Drift (Trôi dạt khái niệm)",
                "definition": "Sự thay đổi theo thời gian của mối quan hệ thống kê giữa biến đầu vào và biến mục tiêu do biến động mùa vụ, thành phần nước thải hoặc lão hóa màng."
            }
        ],
        "key_entities": [
            "Wael S. Al-Rashed",
            "Kovacs et al.",
            "Viet and Jang",
            "Hamedi et al.",
            "Sun et al.",
            "Verrecht et al.",
            "Krzeminski et al.",
            "Newhart et al.",
            "Meng et al.",
            "Judd",
            "SHAP (SHapley Additive exPlanations)",
            "TreeSHAP",
            "KernelSHAP",
            "LIME (Local Interpretable Model-agnostic Explanations)",
            "Partial Dependence Plots (PDP)",
            "Individual Conditional Expectation (ICE)",
            "Integrated Gradients",
            "Random Forest (RF)",
            "Support Vector Machines (SVM)",
            "Least Squares Support Vector Machines (LSSVM)",
            "Long Short-Term Memory (LSTM)",
            "XGBoost",
            "LightGBM",
            "CatBoost",
            "MBR-Net",
            "Transformer",
            "Activated Sludge Models (ASM1, ASM2d, ASM3)",
            "BSM-MBR Benchmark Simulation Model",
            "SCADA System",
            "MDPI Membranes"
        ]
    },
    "routing_table": [
        {
            "chunk_id": "chunk_01",
            "chapters": [
                "Phần mở đầu và Tóm tắt tổng quan (Abstract and Frontmatter)",
                "Chương 1: Giới thiệu Tổng quan về MBR, Thách thức Vận hành và Hội tụ Công nghệ (1. Introduction)",
                "Chương 2: Phương pháp luận và Tiêu chí Tổng quan Tài liệu (2. Methodology)"
            ],
            "start_page": 1,
            "end_page": 5,
            "estimated_tokens": 2750,
            "start_heading_level": 3,
            "depth_budget": 2
        },
        {
            "chunk_id": "chunk_02",
            "chapters": [
                "Chương 3 (Phần 1): Cơ chế Tắc nghẽn Màng và Các Mô hình Học máy Cơ bản (3.1 Fouling Mechanisms and Modelling Context & 3.2 Shallow and Kernel-Based ML Models)"
            ],
            "start_page": 5,
            "end_page": 7,
            "estimated_tokens": 1950,
            "start_heading_level": 3,
            "depth_budget": 2
        },
        {
            "chunk_id": "chunk_03",
            "chapters": [
                "Chương 3 (Phần 2): Các Phương pháp Tập hợp, Học sâu, Giới hạn Dữ liệu và Kiểm chuẩn Thực nghiệm (3.3 Ensemble Methods and Deep Learning & 3.4 Dataset Limitations, Overfitting Risk, Cross-Site Generalization, Tables 1 & 2)"
            ],
            "start_page": 7,
            "end_page": 11,
            "estimated_tokens": 3150,
            "start_heading_level": 3,
            "depth_budget": 2
        },
        {
            "chunk_id": "chunk_04",
            "chapters": [
                "Chương 4: Trí tuệ Nhân tạo có thể Giải thích trong Hệ thống MBR (4. Explainable Artificial Intelligence in MBR Applications: 4.1 Explainability Imperative, 4.2 SHAP Framework, 4.3 LIME, PDP, Gradient-Based Methods, Table 3)"
            ],
            "start_page": 11,
            "end_page": 14,
            "estimated_tokens": 2850,
            "start_heading_level": 3,
            "depth_budget": 2
        },
        {
            "chunk_id": "chunk_05",
            "chapters": [
                "Chương 5: Tối ưu hóa Năng lượng Tiêu thụ trong Hệ thống MBR bằng Học máy (5. ML-Driven Energy Optimization in MBR Systems: 5.1 Energy Consumption Structure and Targets, 5.2 Confirmed Energy Reduction Evidence, Table 4)"
            ],
            "start_page": 14,
            "end_page": 16,
            "estimated_tokens": 1750,
            "start_heading_level": 3,
            "depth_budget": 2
        },
        {
            "chunk_id": "chunk_06",
            "chapters": [
                "Chương 6: Khung Kiến trúc Bản sao Số cho Hệ thống MBR (6. Digital Twin Frameworks for MBR Systems: 6.1 Architecture, Components & Maturity Tiers, 6.2 XAI Integration in DT Decision Architecture, Table 5, Figure 3)"
            ],
            "start_page": 16,
            "end_page": 19,
            "estimated_tokens": 2750,
            "start_heading_level": 3,
            "depth_budget": 2
        },
        {
            "chunk_id": "chunk_07",
            "chapters": [
                "Chương 7: Chín Khoảng trống Nghiên cứu Then chốt và Định hướng Tương lai (7. Research Gaps and Future Directions: Gaps 1 to 9)"
            ],
            "start_page": 19,
            "end_page": 22,
            "estimated_tokens": 2450,
            "start_heading_level": 3,
            "depth_budget": 2
        },
        {
            "chunk_id": "chunk_08",
            "chapters": [
                "Chương 8: Kết luận Tổng hợp, Lộ trình Triển khai Thực tế và Tài liệu Tham khảo (8. Conclusions, Implementation Roadmap & References Overview)"
            ],
            "start_page": 22,
            "end_page": 26,
            "estimated_tokens": 4650,
            "start_heading_level": 3,
            "depth_budget": 2
        }
    ],
    "global_context_pack": """# Ngữ cảnh Toàn cục: MBR Thông minh

## 1. Bối cảnh và Thách thức Vận hành
Bể phản ứng màng sinh học (MBR) kết hợp bùn hoạt tính với màng UF/MF. Công nghệ tạo nước chất lượng cao nhưng có hai trở ngại:
- Tắc nghẽn màng: EPS và SMP bám vào màng. Quá trình làm tăng áp suất qua màng (TMP) và giảm lưu lượng thấm.
- Năng lượng cao: Tiêu thụ 0.4–1.5 kWh/m³. Sục khí màng chiếm 60–75% điện năng.

## 2. Chuỗi Giá trị: ML - XAI - Digital Twin
Ba công nghệ tạo thành chuỗi vận hành khép kín:
- Machine Learning (ML): Dự báo TMP, lưu lượng và chất lượng nước từ dữ liệu SCADA.
- Explainable AI (XAI): Phân rã mô hình hộp đen thành đóng góp thuộc tính. XAI giúp kỹ sư kiểm toán và tuân thủ quy định pháp lý.
- Digital Twin (DT): Bản sao ảo kết nối hai chiều với trạm xử lý. DT kết hợp mô hình bùn hoạt tính (ASM) với ML để điều khiển tự động (Tier III).

## 3. Hiệu năng Mô hình Học máy
- Mô hình cơ bản: ANN và LSSVM dự báo tốt trên tập dữ liệu nhỏ (LSSVM đạt R² = 0.990). LSSVM khó mở rộng cho dữ liệu lớn.
- Mô hình tập hợp và Học sâu: Random Forest (RF) đạt hiệu năng cao nhất ở quy mô thực tế (Kovacs et al., >80.000 mẫu SCADA, R² = 0.927–0.996, RMSE = 0.264–0.904 kPa). LSTM xử lý tốt chuỗi thời gian TMP.
- Hạn chế: Đa số nghiên cứu dùng dữ liệu đơn trạm, chia tách ngẫu nhiên gây rò rỉ thời gian.

## 4. Trí tuệ Nhân tạo Giải thích được (XAI)
- SHAP: Dựa trên lý thuyết trò chơi. SHAP xác định biến chi phối: MLSS, SRT, HRT và sục khí. Phân tích SHAP theo chu kỳ lọc phát hiện sớm lớp bánh cặn bị nén.
- LIME và PDP: LIME giải thích cục bộ nhanh. PDP chỉ ra ngưỡng chuyển tiếp của MLSS tại 10–12 g/L, khi bùn chuyển sang dạng phi Newton.
- Integrated Gradients: Phân tích mạng LSTM, chỉ ra 2–8 giờ trước sự cố quyết định mức tăng TMP.

## 5. Tối ưu hóa Năng lượng Vận hành
- Tiêu thụ chuẩn: Nằm trong khoảng 0.8–1.1 kWh/m³.
- Bằng chứng thực tế: Sun et al. giảm 20% điện sục khí (đạt 0.45 kWh/m³) bằng điều khiển PI trên mô hình ASM. Chưa có nghiên cứu công bố nào chứng minh mức tiết kiệm năng lượng trực tiếp từ ML tại nhà máy thực tế.

## 6. Khung Kiến trúc Bản sao Số
- Ba bậc trưởng thành: Tier I (Mô tả - SCADA), Tier II (Dự báo 12–72 giờ), Tier III (Kê đơn và điều khiển vòng kín - chưa triển khai ở quy mô thực tế).
- Quy trình 5 bước: (1) Thu thập SCADA; (2) Dự báo ML; (3) Tính giá trị SHAP; (4) Bảng điều khiển; (5) Điều khiển chấp hành và ghi nhật ký kiểm toán.

## 7. Chín Khoảng trống Nghiên cứu Then chốt
1. Khan hiếm tập dữ liệu chuẩn mở từ nhiều trạm thực tế.
2. Thiếu định lượng độ bất định (UQ) trong dự báo.
3. Chưa có trạm thực tế nào triển khai DT Tier III kết hợp XAI.
4. Cảm biến thông thường không đo kịp biến động nước thải đầu vào.
5. Thiếu khung pháp lý công nhận quyết định từ AI.
6. Chưa hạch toán đầy đủ chi phí xây dựng và bảo trì mô hình ML.
7. Thiếu hụt nhân lực có kỹ năng kép về kỹ thuật nước và MLOps.
8. Thiếu đối chuẩn trực tiếp với bộ điều khiển PID hoặc Fuzzy.
9. Chưa đo lường dấu chân carbon và điện năng tính toán của AI."""
}

with open(manifest_path, 'w', encoding='utf-8') as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

print(f"Successfully wrote manifest to: {manifest_path}")

# Verification
with open(manifest_path, 'r', encoding='utf-8') as f:
    loaded = json.load(f)

ctx_tokens = len(enc.encode(loaded['global_context_pack']))
print(f"Verification Summary:")
print(f"- File exists: {os.path.exists(manifest_path)}")
print(f"- File size: {os.path.getsize(manifest_path)} bytes")
print(f"- Master skeleton chapters: {len(loaded['master_skeleton'])}")
print(f"- Routing table chunks: {len(loaded['routing_table'])}")
print(f"- Total estimated tokens: {loaded['total_estimated_tokens']}")
print(f"- Global context pack tokens: {ctx_tokens} (budget <= 1500)")
print(f"- Key terms defined: {len(loaded['global_lexicon']['key_terms'])}")
print(f"- Key entities listed: {len(loaded['global_lexicon']['key_entities'])}")

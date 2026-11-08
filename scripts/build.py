#!/usr/bin/env python3
"""Dựng lại .claude-plugin/marketplace.json và README.md từ marketplace gốc của từng tác giả.

  python3 -I scripts/build.py          lấy lại danh sách từ kho gốc (cần mạng và git)
  python3 -I scripts/build.py check    cài thử từng plugin vào thư mục cấu hình tạm, ghi số skill vào scripts/inventory.json (cần Claude Code)
  python3 -I scripts/build.py check <tên>...   chỉ cài thử các plugin này, giữ nguyên số liệu của plugin khác
  python3 -I scripts/build.py readme   chỉ dựng lại README.md, không cần mạng

Thêm hoặc bớt plugin: sửa UP hoặc WRAP bên dưới, chạy lệnh đầu rồi lệnh check (hoặc check kèm tên các plugin vừa thêm).
"""
import json
import os
import posixpath
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
MARKET = ROOT / '.claude-plugin' / 'marketplace.json'
INV = ROOT / 'scripts' / 'inventory.json'
NAME = 'skill-theo-nganh'
REPO = 'DuongVuIT/skill-theo-nganh'
OWNER = 'Vũ Đại Dương'

CATS = {
    'xay-dung': 'Xây dựng & BIM',
    'phan-mem': 'Phần mềm & dữ liệu',
    'dien-tu': 'Điện tử, cơ khí & sản xuất',
    'design': 'Design & sáng tạo',
    'marketing': 'Marketing & bán hàng',
    'tai-chinh': 'Tài chính & kế toán',
    'phap-ly': 'Pháp lý',
    'quan-ly': 'Quản lý & vận hành',
    'giao-duc': 'Giáo dục',
    'khoa-hoc': 'Khoa học & y sinh',
    'y-khoa': 'Y khoa & y tế',
    'duoc': 'Dược & phát triển thuốc',
    'da-nganh': 'Văn phòng & đa ngành',
}

# README: biểu tượng và plugin nên thử trước của từng nhóm ngành
LOOK = {
    'xay-dung': ('🏗️', ['ddc-toolkit', 'ddc-cwicr']),
    'phan-mem': ('💻', ['engineering', 'frontend-design', 'data']),
    'dien-tu': ('⚙️', ['hardware', 'diode-pcb']),
    'design': ('🎨', ['design', 'figma', 'canva']),
    'marketing': ('📣', ['marketing', 'sales', 'brand-voice']),
    'tai-chinh': ('💰', ['finance', 'financial-analysis', 'model-builder']),
    'phap-ly': ('⚖️', ['legal', 'commercial-legal', 'law-student']),
    'quan-ly': ('📋', ['product-management', 'human-resources', 'customer-support']),
    'giao-duc': ('🎓', ['learn-with-coursera']),
    'khoa-hoc': ('🔬', ['bio-research']),
    'y-khoa': ('🩺', ['healthcare', 'biomcp']),
    'duoc': ('💊', ['tooluniverse']),
    'da-nganh': ('🗂️', ['document-skills', 'productivity']),
}

# Plugin lấy từ marketplace có sẵn: kho gốc -> {tên plugin: (ngành, mô tả)}
UP = {
    'anthropics/knowledge-work-plugins': {
        'engineering': ('phan-mem', 'Standup, review code, quyết định kiến trúc, thiết kế hệ thống, xử lý sự cố, checklist deploy, chiến lược test, nợ kỹ thuật, tài liệu kỹ thuật.'),
        'data': ('phan-mem', 'Viết SQL, khám phá dữ liệu, thống kê, vẽ biểu đồ và dashboard, biến số liệu thô thành câu chuyện dễ hiểu.'),
        'unity': ('phan-mem', 'Plugin chính chủ của Unity cho làm game: phát triển, kiếm tiền từ game, tối ưu hiệu năng.'),
        'design': ('design', 'Phê bình thiết kế, quản lý design system, viết UX copy, kiểm tra khả năng tiếp cận, tổng hợp nghiên cứu người dùng, bàn giao cho dev.'),
        'canva': ('design', 'Tạo, sửa, đổi kích thước và kiểm nhận diện thương hiệu cho thiết kế Canva. Cần tài khoản Canva.'),
        'adobe-for-creativity': ('design', 'Công cụ Adobe Creative Cloud cho ảnh, vector, thiết kế, video: sửa hàng loạt, chuyển đổi cho từng nền tảng, chạy chuỗi thao tác nhiều bước.'),
        'miro': ('design', 'Đọc bảng Miro, vẽ sơ đồ, sinh code từ bảng. Cần tài khoản Miro.'),
        'marketing': ('marketing', 'Soạn nội dung, lên kế hoạch chiến dịch, chuỗi email, SEO audit, brief đối thủ, rà giọng thương hiệu, báo cáo hiệu quả từng kênh.'),
        'sales': ('marketing', 'Chuẩn bị cuộc gọi, tóm tắt và follow-up, nghiên cứu khách hàng, review deal và pipeline, dự báo doanh số. Làm việc với CRM, email, lịch, chat.'),
        'brand-voice': ('marketing', 'Rút giọng thương hiệu từ tài liệu và hội thoại sẵn có, viết guideline áp dụng được, kiểm nội dung AI viết có đúng giọng không.'),
        'amazon-selling-partner': ('marketing', 'Kết nối Amazon Seller Central: hỏi doanh số, tồn kho, hiệu quả listing, nhận gợi ý từ dữ liệu của chính bạn. Cần tài khoản người bán.'),
        'finance': ('tai-chinh', 'Bút toán, đối chiếu, lập báo cáo tài chính, phân tích chênh lệch, chuẩn bị kiểm toán, khóa sổ cuối tháng.'),
        'intuit-quickbooks': ('tai-chinh', 'Đọc sức khỏe tài chính từ QuickBooks: lãi lỗ, dòng tiền, bảng cân đối, công nợ phải thu, so với ngành, chi phí lương. Cần tài khoản QuickBooks.'),
        'legal': ('phap-ly', 'Rà soát hợp đồng, phân loại NDA, quy trình tuân thủ cho pháp chế nội bộ, soạn tóm tắt pháp lý.'),
        'product-management': ('quan-ly', 'Viết spec tính năng, lập roadmap, lên sprint, brainstorm, tổng hợp nghiên cứu người dùng, cập nhật cho các bên liên quan, theo dõi đối thủ.'),
        'operations': ('quan-ly', 'Quản lý nhà cung cấp, viết tài liệu quy trình, quản lý thay đổi, hoạch định năng lực, theo dõi tuân thủ.'),
        'human-resources': ('quan-ly', 'Tuyển dụng, onboarding, đánh giá hiệu suất, phân tích lương thưởng, tư vấn chính sách nhân sự.'),
        'customer-support': ('quan-ly', 'Phân loại ticket, soạn câu trả lời, chuyển cấp xử lý, tìm bối cảnh khách hàng, biến ca đã xử lý thành bài tự trợ giúp.'),
        'small-business': ('quan-ly', 'Quy trình dựng sẵn để vận hành và phát triển doanh nghiệp nhỏ. Bước nào đụng đến tiền cũng chờ bạn duyệt.'),
        'learn-with-coursera': ('giao-duc', 'Hỏi 3 câu (chủ đề, trình độ, hình thức học) rồi tìm trong kho Coursera để đưa ra lộ trình học.'),
        'bio-research': ('khoa-hoc', 'Kết nối công cụ và cơ sở dữ liệu nghiên cứu tiền lâm sàng: tra tài liệu, phân tích hệ gen, xếp hạng đích điều trị.'),
        'maven-bio': ('duoc', 'Nghiên cứu ngành dược sinh học trên đồ thị tri thức của Maven Bio: pipeline của đối thủ, bức tranh theo chỉ định điều trị, hồ sơ từng hoạt chất, thương vụ và gọi vốn, tổng hợp bằng chứng có dẫn nguồn FDA, SEC, thử nghiệm lâm sàng. Cần tài khoản Maven Bio.'),
        'productivity': ('da-nganh', 'Quản lý việc, lên kế hoạch trong ngày, ghi nhớ bối cảnh công việc; đồng bộ với lịch, email, chat.'),
        'enterprise-search': ('da-nganh', 'Tìm trong email, chat, tài liệu và wiki của công ty từ một chỗ.'),
    },
    'anthropics/claude-plugins-official': {
        'frontend-design': ('phan-mem', 'Dựng giao diện web chỉn chu, có cá tính riêng, tránh kiểu giao diện AI na ná nhau.'),
        'expo': ('phan-mem', 'Skill chính chủ của Expo: build, deploy, nâng cấp, debug app React Native, dựng giao diện với Expo Router.'),
        'aws-startup-advisor': ('phan-mem', 'Gợi ý kiến trúc, chi phí và bảo mật AWS theo đúng giai đoạn của startup.'),
        'figma': ('design', 'Đọc file thiết kế, component và design token, chuyển thiết kế thành code. Cần tài khoản Figma.'),
        'superdesign': ('design', 'Thiết kế hoặc làm lại UI và ảnh marketing trên canvas vô hạn: đọc codebase lấy bối cảnh, dựng design system, tạo nhiều phương án.'),
    },
    'anthropics/skills': {
        'document-skills': ('da-nganh', 'Đọc, tạo và chỉnh file Word, Excel, PowerPoint, PDF. Có ích cho gần như mọi nghề.'),
        'example-skills': ('design', 'Bộ skill mẫu của Anthropic: canvas-design (poster, ảnh), brand-guidelines, theme-factory, algorithmic-art, slack-gif-creator, web-artifacts-builder, skill-creator…'),
    },
    'anthropics/financial-services': {
        'financial-analysis': ('tai-chinh', 'Nền tảng của bộ Financial Services: mô hình DCF, comps, LBO, 3 báo cáo tài chính, phân tích cạnh tranh, kiểm tra deck.'),
        'investment-banking': ('tai-chinh', 'Ngân hàng đầu tư: thông tin khách hàng và thị trường, dựng deck, phân tích tài chính, quản lý giao dịch.'),
        'equity-research': ('tai-chinh', 'Nghiên cứu cổ phiếu: phân tích kết quả kinh doanh, viết báo cáo khởi tạo.'),
        'private-equity': ('tai-chinh', 'Quỹ đầu tư tư nhân: tìm công ty mục tiêu, quản lý CRM, tiếp cận nhà sáng lập.'),
        'fund-admin': ('tai-chinh', 'Quản trị quỹ: đối chiếu sổ cái, truy chênh lệch, trích trước, roll-forward, khớp NAV.'),
        'pitch-agent': ('tai-chinh', 'Dựng pitch deck từ comps, giao dịch tiền lệ và LBO.'),
        'market-researcher': ('tai-chinh', 'Nghiên cứu thị trường: tổng quan ngành, bức tranh cạnh tranh, ý tưởng đầu tư.'),
        'earnings-reviewer': ('tai-chinh', 'Đọc cuộc gọi kết quả kinh doanh, cập nhật mô hình, viết nhận định.'),
        'meeting-prep-agent': ('tai-chinh', 'Soạn tài liệu chuẩn bị trước buổi gặp khách hàng.'),
        'model-builder': ('tai-chinh', 'Dựng mô hình DCF, LBO, 3 báo cáo, comps ngay trong Excel.'),
        'gl-reconciler': ('tai-chinh', 'Đối chiếu sổ cái: tìm chênh lệch, truy nguyên nhân, chuyển người duyệt.'),
        'kyc-screener': ('tai-chinh', 'KYC: đọc hồ sơ mở tài khoản, chạy bộ quy tắc, đánh dấu chỗ còn thiếu.'),
        'valuation-reviewer': ('tai-chinh', 'Rà định giá: từ hồ sơ của GP đến định giá và báo cáo cho LP.'),
        'month-end-closer': ('tai-chinh', 'Khóa sổ cuối tháng: trích trước, roll-forward, thuyết minh.'),
        'statement-auditor': ('tai-chinh', 'Rà sao kê gửi nhà đầu tư (LP) trước khi phát hành.'),
        'lseg': ('tai-chinh', 'Dùng dữ liệu LSEG: trái phiếu, đường cong lợi suất, FX carry, quyền chọn, dashboard vĩ mô.'),
        'sp-global': ('tai-chinh', 'Dùng dữ liệu S&P Global: tearsheet công ty, xem trước kết quả kinh doanh, tóm tắt giao dịch.'),
    },
    'anthropics/claude-for-legal': {
        'commercial-legal': ('phap-ly', 'Hợp đồng thương mại: hợp đồng nhà cung cấp, NDA, SaaS, theo dõi hạn gia hạn và hủy.'),
        'privacy-legal': ('phap-ly', 'Dữ liệu cá nhân: đánh giá tác động (PIA), thỏa thuận xử lý dữ liệu (DPA), yêu cầu truy cập dữ liệu (DSAR).'),
        'product-legal': ('phap-ly', 'Pháp lý sản phẩm: rủi ro khi ra mắt, kiểm các tuyên bố quảng cáo.'),
        'corporate-legal': ('phap-ly', 'Doanh nghiệp: thẩm định M&A, biên bản hội đồng quản trị.'),
        'employment-legal': ('phap-ly', 'Luật lao động theo từng bang của Mỹ.'),
        'regulatory-legal': ('phap-ly', 'Theo dõi quy định mới.'),
        'ai-governance-legal': ('phap-ly', 'Quản trị AI: rà use case AI, điều khoản trong hợp đồng nhà cung cấp AI.'),
        'litigation-legal': ('phap-ly', 'Tranh tụng: claim chart, niên biểu vụ việc, chuẩn bị lấy lời khai.'),
        'law-student': ('phap-ly', 'Cho sinh viên luật: hỏi đáp kiểu Socratic, tóm tắt án lệ, ôn thi.'),
        'legal-clinic': ('phap-ly', 'Cho phòng tư vấn pháp lý của trường luật.'),
        'legal-builder-hub': ('phap-ly', 'Tìm, đánh giá và cài skill pháp lý của cộng đồng, có bước rà bảo mật.'),
        'ip-legal': ('phap-ly', 'Sở hữu trí tuệ: nhãn hiệu, tự do vận hành (FTO), sáng chế, thư cảnh báo và DMCA, giấy phép mã nguồn mở.'),
        'cocounsel-legal': ('phap-ly', 'Westlaw Deep Research của Thomson Reuters. Cần tài khoản Thomson Reuters.'),
    },
    'anthropics/healthcare': {
        'healthcare': ('y-khoa', 'Bộ Claude for Healthcare: duyệt prior auth (xin tiền phê duyệt bảo hiểm), gán mã bệnh ICD-10-CM và mã thủ thuật CPT/HCPCS, trích dữ liệu từ ghi chú lâm sàng, soạn đề cương thử nghiệm lâm sàng, đọc hồ sơ bệnh án qua FHIR, sàng lọc gian lận bảo hiểm. Kết nối sẵn PubMed, ClinicalTrials.gov, ICD-10, CMS, NPI. Phần bảo hiểm và mã hóa theo hệ thống Mỹ.'),
    },
    'anthropics/life-sciences': {
        'binder-gauntlet': ('duoc', 'Kiểm chứng protein gắn đích (binder) thiết kế mới trước khi đặt tổng hợp DNA: dự đoán lại cấu trúc bằng công cụ độc lập, chạy đối chứng, đánh giá khả năng phát triển thành thuốc (developability), xuất hồ sơ ghi rõ phần nào chưa kiểm. Mọi kết quả đều là dự đoán tính toán.'),
    },
    'IHTSDO/snowstorm-mcp-server': {
        'snowstorm-mcp-server': ('y-khoa', 'Tra bộ thuật ngữ lâm sàng SNOMED CT: tìm khái niệm, kiểm mã, duyệt cây phân cấp, mở rộng value set, đủ các bản quốc tế, Mỹ, Anh, Úc. Máy chủ do chính SNOMED International vận hành, không cần cài. Dùng để tra cứu và tìm hiểu; đưa vào sản phẩm thì cần giấy phép SNOMED CT.'),
    },
    'genomoncology/biomcp': {
        'biomcp': ('y-khoa', 'Tra bằng chứng y sinh từ một chỗ: bài báo PubMed, thử nghiệm lâm sàng, gen và biến thể (ClinVar), thuốc, bệnh, pathway, protein. Chỉ đọc dữ liệu, không ghi gì. Cần cài biomcp-cli.'),
    },
    'mims-harvard/ToolUniverse': {
        'tooluniverse': ('duoc', 'Hơn 2.700 công cụ tra cứu (PubMed, PubChem, FAERS, ClinicalTrials.gov, UniProt…) kèm skill cho nghiên cứu thuốc, tương tác thuốc, phát hiện biến cố bất lợi, dự đoán ADMET, hồ sơ đăng ký thuốc, tái định vị thuốc, thẩm định đích tác dụng, cả hệ gen và lâm sàng. Cần cài uv. Hook chạy một lần để xóa skill tooluniverse-* cài kiểu cũ trong ~/.claude/skills (nếu có). Rất nặng: chiếm khoảng 24 nghìn token ngữ cảnh mỗi phiên, chỉ cài khi cần.'),
    },
    'novainsilico/jinko-skills': {
        'jinko': ('duoc', 'Dược lý hệ thống định lượng (QSP) trên nền tảng Jinkō: gom bằng chứng và dữ liệu, dựng và hiệu chỉnh mô hình, phân tích độ nhạy, tạo quần thể ảo, mô phỏng thử nghiệm lâm sàng in silico. Cần tài khoản Jinkō.'),
    },
    'fradser/dotclaude': {
        'hardware': ('dien-tu', 'use-kicad-cli: kiểm DRC/ERC và xuất file gia công từ KiCad. use-openscad: dựng mô hình 3D tham số bằng OpenSCAD.'),
    },
    'alirezarezvani/claude-skills': {
        'marketing-skills': ('marketing', 'Marketing chia 8 nhóm: nội dung, SEO và AEO, tối ưu chuyển đổi, kênh, tăng trưởng, phân tích thị trường, hỗ trợ bán hàng, tăng trưởng trên X. Kèm công cụ Python.'),
        'business-growth-skills': ('marketing', 'Tăng trưởng kinh doanh: customer success, kỹ sư bán hàng, revenue operations, soạn hợp đồng và đề xuất.'),
        'engineering-skills': ('phan-mem', 'Kỹ thuật phần mềm: kiến trúc, frontend, backend, fullstack, QA, DevOps, bảo mật, AI/ML, data engineering, Playwright, TDD, kiểm tra truy cập WCAG.'),
        'engineering-advanced-skills': ('phan-mem', 'Kỹ thuật nâng cao: thiết kế agent và RAG, thiết kế cơ sở dữ liệu, migration, observability, rà dependency, review API, changelog.'),
        'finance-skills': ('tai-chinh', 'Tài chính: phân tích chỉ số, định giá DCF, ngân sách và dự báo; chỉ số SaaS (ARR, MRR, churn, CAC, LTV); tư vấn đầu tư; khóa sổ cuối tháng.'),
        'c-level-skills': ('quan-ly', 'Cố vấn cấp lãnh đạo: hội đồng quản trị ảo gồm CEO, CTO, COO, CPO, CMO, CFO, CRO, CISO, CHRO, thêm cố vấn pháp lý, dữ liệu, AI.'),
        'product-skills': ('quan-ly', 'Quản lý sản phẩm kèm công cụ Python: vòng discovery liên tục và bộ công cụ cho product manager.'),
        'pm-skills': ('quan-ly', 'Quản lý dự án kèm công cụ Python: lấy dữ liệu Jira, đo luồng Kanban, dự báo tiến độ bằng Monte Carlo.'),
        'ra-qm-skills': ('y-khoa', 'Quy chuẩn và quản lý chất lượng cho thiết bị y tế: ISO 13485, MDR 2017/745, FDA 510(k)/PMA, GDPR, ISO 27001, CAPA, quản lý rủi ro, đánh giá lâm sàng, SOC 2.'),
    },
}

# Kho skill chưa có marketplace, bọc thành plugin, ghim theo commit lúc dựng:
# (tên, kho, thư mục, bỏ thư mục con, ngành, tác giả, mô tả)
DDC = 'datadrivenconstruction/DDC_Skills_for_AI_Agents_in_Construction'
WRAP = [
    ('ddc-toolkit', DDC, '1_DDC_Toolkit', 'CWICR-Database/', 'xay-dung', 'DataDrivenConstruction', 'Chuyển RVT/IFC/DWG sang dữ liệu, phân tích BIM, quản lý chi phí, tiến độ, hồ sơ tài liệu, mua sắm, hiện trường, nguồn lực, bàn giao, phát triển bền vững. Cần Python.'),
    ('ddc-cwicr', DDC, '1_DDC_Toolkit/CWICR-Database', None, 'xay-dung', 'DataDrivenConstruction', 'Dự toán bằng cơ sở dữ liệu đơn giá CWICR: tính chi phí, bóc khối lượng, phân tích giá thầu, phát sinh, nhân công, vật tư, rủi ro, báo cáo. Cần Python.'),
    ('ddc-book', DDC, '2_DDC_Book', None, 'xay-dung', 'DataDrivenConstruction', 'Theo từng chương sách Data-Driven Construction: chuẩn dữ liệu mở, phân tích bằng pandas và LLM, PDF/CAD sang dữ liệu, kiểm chất lượng dữ liệu, dự toán, bóc khối lượng tự động, 4D BIM và CO2, ETL, dashboard KPI, dự đoán chi phí bằng ML. Cần Python.'),
    ('ddc-insights', DDC, '3_DDC_Insights', None, 'xay-dung', 'DataDrivenConstruction', 'Tự động hóa quy trình, an toàn và chất lượng, tối ưu tiến độ, tự động hóa hiện trường, agent AI cho dự án xây dựng.'),
    ('ddc-curated', DDC, '4_DDC_Curated', None, 'xay-dung', 'DataDrivenConstruction', 'Hợp đồng và pháp lý, kiểm dữ liệu, sinh tài liệu, quản lý tài chính, viết prompt, đảm bảo chất lượng cho dự án xây dựng.'),
    ('ddc-innovative', DDC, '5_DDC_Innovative', None, 'xay-dung', 'DataDrivenConstruction', 'Hướng mới: digital twin, khảo sát bằng drone, phát hiện lỗi bằng AI, kiểm va chạm BIM, carbon hàm chứa và ESG, mô phỏng năng lượng, IoT theo dõi vật tư, tự động hóa bằng n8n.'),
    ('ddc-open-construction-erp', DDC, '6_OpenConstructionERP', None, 'xay-dung', 'DataDrivenConstruction', 'Làm việc với nền tảng OpenConstructionERP: bóc khối lượng từ BIM, dự toán và BOQ, đấu thầu, tiến độ 4D/5D, hiện trường, kết nối MCP.'),
    ('diode-pcb', 'diodeinc/pcb', 'skills', None, 'dien-tu', 'Diode', 'Thiết kế mạch in với công cụ pcb của Diode: nhập dự án KiCad, mô phỏng SPICE, tra registry linh kiện, quản lý thư viện, viết mạch bằng ngôn ngữ Zener.'),
    ('scientific-agent-skills', 'K-Dense-AI/scientific-agent-skills', 'skills', None, 'khoa-hoc', 'K-Dense', 'Nghiên cứu khoa học: tin sinh học và hệ gen, protein, hóa học, ảnh y khoa, máy tính lượng tử, học máy, vẽ hình khoa học, tra cứu tài liệu. Rất nặng: chiếm gần 20 nghìn token ngữ cảnh mỗi phiên, chỉ cài khi cần.'),
    # plugin.json gốc khai agents là thư mục, Claude Code không nhận nên cài lỗi; bọc riêng phần skill
    ('nlmixr2llm', 'nlmixr2/nlmixr2llm', 'inst/skills', None, 'duoc', 'nlmixr2', 'Mô hình dược động học, dược lực học quần thể (popPK/PD) với hệ nlmixr2 trong R: mô phỏng, ước lượng tham số, thiết kế nghiên cứu tối ưu, viết báo cáo, chuyển mô hình qua lại với NONMEM và Monolix. Cần R và các gói nlmixr2.'),
]

def get(url):
    # curl thay cho urllib: Python cài từ python.org trên macOS hay thiếu chứng chỉ SSL
    return json.loads(subprocess.run(['curl', '-fsSL', '-A', 'skill-theo-nganh-build', url],
                                     capture_output=True, check=True).stdout)


def head(repo):
    """(nhánh mặc định, commit) của kho."""
    out = subprocess.run(['git', 'ls-remote', '--symref', f'https://github.com/{repo}.git', 'HEAD'],
                         capture_output=True, text=True, check=True).stdout
    ref = sha = None
    for line in out.splitlines():
        a, _, b = line.partition('\t')
        if a.startswith('ref: refs/heads/'):
            ref = a[len('ref: refs/heads/'):]
        elif b == 'HEAD':
            sha = a
    assert ref and sha, repo
    return ref, sha


def from_upstream(repo, picks):
    m = get(f'https://raw.githubusercontent.com/{repo}/HEAD/.claude-plugin/marketplace.json')
    assert not (m.get('metadata') or {}).get('pluginRoot'), repo
    have = {p['name']: p for p in m['plugins']}
    for name, (cat, desc) in picks.items():
        p = dict(have[name])  # KeyError: kho gốc đã đổi tên hoặc bỏ plugin này
        if isinstance(p['source'], str):  # đường dẫn trong kho gốc -> trỏ thẳng vào thư mục đó
            path = '/'.join(x for x in p['source'].split('/') if x not in ('', '.'))
            page = path  # thư mục README trỏ tới
            if isinstance(p.get('skills'), list):
                # Trỏ vào thư mục cha chung của các skill được liệt kê, nếu không Claude Code
                # nạp luôn mọi skill trong skills/ của kho (document-skills thành 19 skill thay vì 4).
                sk = [posixpath.normpath(s) for s in p['skills']]
                base = posixpath.commonpath([posixpath.dirname(s) for s in sk])
                page = posixpath.join(path, posixpath.commonpath(sk))  # plugin một skill: trỏ thẳng vào thư mục skill
                if base:
                    path = posixpath.join(path, base)
                    p['skills'] = ['./' + posixpath.relpath(s, base) for s in sk]
            url = f'https://github.com/{repo}.git'
            p['source'] = {'source': 'git-subdir', 'url': url, 'path': path} if path else {'source': 'url', 'url': url}
            p.setdefault('homepage', f'https://github.com/{repo}' + (f'/tree/HEAD/{page}' if page else ''))
        if isinstance(p.get('author'), dict):
            p['author'] = {k: v for k, v in p['author'].items() if k != 'email'}
        p.update(description=desc, category=CATS[cat])
        yield p


def wrapped(name, repo, path, skip, cat, author, desc):
    ref, sha = head(repo)
    tree = get(f'https://api.github.com/repos/{repo}/git/trees/{sha}?recursive=1')
    assert not tree.get('truncated'), repo
    pre = path + '/'
    dirs = sorted(e['path'][len(pre):-len('/SKILL.md')] for e in tree['tree']
                  if e['path'].startswith(pre) and e['path'].endswith('/SKILL.md'))
    keep = []
    for d in dirs:
        if d and not (skip and d.startswith(skip)) and not any(d.startswith(k + '/') for k in keep):
            keep.append(d)
    assert keep, name
    return {
        'name': name,
        'description': f'{len(keep)} skill. {desc}',
        'author': {'name': author},
        'homepage': f'https://github.com/{repo}/tree/HEAD/{path}',
        'category': CATS[cat],
        'source': {'source': 'git-subdir', 'url': f'https://github.com/{repo}.git', 'path': path, 'ref': ref, 'sha': sha},
        'strict': False,
        'skills': [f'./{d}' for d in keep],
    }


def link(p):
    s = p['source']
    return p.get('homepage') or s['url'].removesuffix('.git') + (f"/tree/HEAD/{s['path']}" if s.get('path') else '')


def by(p):
    a = p.get('author')
    org = p['source']['url'].split('/')[3]  # chủ kho trên GitHub khi kho gốc không ghi tác giả
    name = (a if isinstance(a, str) else (a or {}).get('name')) or org
    return {'anthropics': 'Anthropic', 'Unity-Technologies': 'Unity', 'expo': 'Expo', 'canva-sdks': 'Canva', 'figma': 'Figma',
            'Superdesign dev, Inc.': 'Superdesign', 'intuit': 'Intuit', 'coursera': 'Coursera', 'IHTSDO': 'SNOMED International',
            'mims-harvard': 'Zitnik Lab, Harvard', 'MavenBio': 'Maven Bio', 'novainsilico': 'Nova In Silico'}.get(name, name)


def main():
    plugins = [p for repo, picks in UP.items() for p in from_upstream(repo, picks)] + [wrapped(*w) for w in WRAP]
    order = list(CATS.values())
    plugins.sort(key=lambda p: order.index(p['category']))
    names = [p['name'] for p in plugins]
    assert len(names) == len(set(names)), sorted({n for n in names if names.count(n) > 1})

    market = {
        'name': NAME,
        'owner': {'name': OWNER},
        'metadata': {'description': 'Plugin Claude Code theo ngành nghề, gom từ kho gốc của từng tác giả: xây dựng, phần mềm, điện tử, design, marketing, tài chính, pháp lý, quản lý, giáo dục, khoa học, y khoa, dược.'},
        'plugins': plugins,
    }
    MARKET.parent.mkdir(exist_ok=True)
    MARKET.write_text(json.dumps(market, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    write_readme()
    print(f'{len(plugins)} plugin ->', MARKET.relative_to(ROOT), '+ README.md')


def vn(n):
    return f'{n:,}'.replace(',', '.')  # 1283 -> 1.283, cách viết số của tiếng Việt


def badge(label, msg, color):
    q = lambda s: quote(s.replace('-', '--').replace('_', '__'))  # cú pháp huy hiệu tĩnh của shields.io
    return f'<img alt="{label}: {msg}" src="https://img.shields.io/badge/{q(label)}-{q(msg)}-{color}?style=flat-square">'


def write_readme():
    plugins = json.loads(MARKET.read_text(encoding='utf-8'))['plugins']
    inv = json.loads(INV.read_text(encoding='utf-8')) if INV.exists() else {}
    keys = [k for k in CATS if any(p['category'] == CATS[k] for p in plugins)]
    names = {p['name'] for p in plugins}
    assert all(n in names for k in keys for n in LOOK[k][1]), 'LOOK nhắc tới plugin không có trong danh sách'

    overview = ['| Nhóm ngành | Nên thử trước |', '|---|---|']  # 2 cột cho vừa màn hình điện thoại
    sections = []
    for k in keys:
        icon, picks = LOOK[k]
        ps = [p for p in plugins if p['category'] == CATS[k]]
        sk = vn(sum(inv.get(p['name'], {}).get('skills', 0) for p in ps))
        overview.append(f"| {icon} [**{CATS[k]}**](#{k})<br><sub>{len(ps)} plugin · {sk} skill</sub> | {' · '.join(f'`{n}`' for n in picks)} |")
        sections += [f'\n<a id="{k}"></a>\n\n### {icon} {CATS[k]}\n', f'<sub>{len(ps)} plugin · {sk} skill</sub>\n',
                     '| Plugin | Làm gì | Skill |', '|---|---|:-:|']
        for p in ps:
            n = inv.get(p['name'])
            name = f"[`{p['name']}`]({link(p)})" + (' ⚡' if n and n['hooks'] else '')
            desc = re.sub(r'^\d+ skill\. ', '', p['description']).replace('|', '/')  # số skill đã có cột riêng
            size = f"{n['skills']}&nbsp;{'🟢' if n['tokens'] < 1000 else '🟡' if n['tokens'] <= 3000 else '🔴'}" if n else '–'
            sections.append(f'| {name}<br><sub>{by(p)}</sub> | {desc} | {size} |')

    owner = REPO.split('/')[0]
    hooked = [f"`{p['name']}`" for p in plugins if inv.get(p['name'], {}).get('hooks')]
    notes = ['Dự án cộng đồng, không liên kết với Anthropic hay các hãng có tên trong danh sách.']
    if hooked:
        who = ', '.join(hooked[:-1]) + ' và ' + hooked[-1] if len(hooked) > 1 else hooked[0]
        notes.append(f'{who} có hook ⚡ tự chạy lệnh trên máy. Đọc kho gốc trước khi bật.')
    notes += [
        'Các plugin `ddc-*`, `diode-pcb` và `scientific-agent-skills` vốn là kho skill rời. Marketplace này bọc chúng thành plugin và ghim theo một commit cố định.',
        '`nlmixr2llm` gốc có file manifest mà Claude Code bản mới không nhận (trường `agents`), nên marketplace này chỉ bọc phần skill của nó, ghim theo một commit cố định, chưa kèm agent điều phối.',
        'Skill chỉ có trong app Claude không có ở đây. Plugin `operations` của bộ Financial Services trùng tên với `operations` của Knowledge Work nên không đưa vào.',
        '`clinical-trial-protocol` bản lẻ của Life Sciences cần MCP ClinicalTrials cài qua Claude Desktop, còn `clinical-trial-forecast` chỉ chạy trong Claude Science, nên cả hai không đưa vào. Skill soạn đề cương thử nghiệm lâm sàng đã có sẵn trong `healthcare`.',
    ]
    notes_md = '\n'.join('- ' + n for n in notes)
    badges = '\n  '.join([
        badge('plugin', str(len(plugins)), '2563eb'),
        badge('skill', vn(sum(v['skills'] for v in inv.values())), '7c3aed'),
        badge('nhóm ngành', str(len(keys)), '0d9488'),
        badge('dành cho', 'Claude Code', 'd97706'),
        badge('mô tả', 'tiếng Việt', 'dc2626'),
        f'<a href="https://github.com/{REPO}/commits/main"><img alt="Lần cập nhật gần nhất" '
        f'src="https://img.shields.io/github/last-commit/{REPO}?style=flat-square&label={quote("cập nhật")}"></a>',
    ])
    (ROOT / 'README.md').write_text(f'''<p align="center">
  <img src="assets/banner.svg" alt="Skill theo ngành: plugin Claude Code cho từng nghề, cài bằng một lệnh" width="100%">
</p>

<p align="center">
  {badges}
</p>

<p align="center">
  <b>{len(plugins)} plugin Claude Code chọn lọc cho {len(keys)} nhóm ngành, mô tả bằng tiếng Việt.</b><br>
  Thêm marketplace một lần, rồi chọn plugin hợp với nghề của bạn ngay trong menu <code>/plugin</code>.
</p>

<p align="center">
  <a href="#cai-dat">🚀 Cài đặt</a> &nbsp;·&nbsp;
  <a href="#chon-theo-nganh">🧭 Chọn theo ngành</a> &nbsp;·&nbsp;
  <a href="#danh-sach">📚 Danh sách</a> &nbsp;·&nbsp;
  <a href="#hoi-dap">💬 Hỏi đáp</a> &nbsp;·&nbsp;
  <a href="#luu-y">🛡️ Lưu ý</a>
</p>

<a id="cai-dat"></a>

## 🚀 Cài trong 3 bước

**1. Thêm marketplace**, chỉ cần làm một lần. Chạy trong Terminal:

```bash
claude plugin marketplace add {REPO}
```

Đang ở trong Claude Code thì gõ `/plugin marketplace add {REPO}` cũng được.

**2. Chọn plugin.** Gõ `/plugin` trong Claude Code để duyệt cả {len(plugins)} plugin bằng menu, hoặc cài thẳng bằng tên:

```bash
claude plugin install document-skills@{NAME}
```

**3. Mở phiên Claude Code mới** là dùng được.

> [!TIP]
> Chưa biết bắt đầu từ đâu? Cài `document-skills` trước để Claude đọc, tạo và sửa file Word, Excel, PowerPoint, PDF. Plugin này hợp với gần như mọi nghề. Sau đó chọn thêm plugin của ngành bạn ở bảng dưới.

<a id="chon-theo-nganh"></a>

## 🧭 Chọn theo ngành

{chr(10).join(overview)}

<a id="danh-sach"></a>

## 📚 Danh sách đầy đủ

Bấm tên plugin để xem kho gốc. Cột **Skill** là số skill đếm được khi cài thử, kèm chấm màu cho biết plugin chiếm sẵn bao nhiêu ngữ cảnh của Claude ở mỗi phiên:

🟢 dưới 1.000 token &nbsp;·&nbsp; 🟡 1.000 đến 3.000 token &nbsp;·&nbsp; 🔴 trên 3.000 token &nbsp;·&nbsp; ⚡ có hook tự chạy lệnh trên máy
{chr(10).join(sections)}

<a id="hoi-dap"></a>

## 💬 Hỏi đáp

<details>
<summary><b>Cài xong mà Claude chưa dùng tới plugin?</b></summary>
<br>

Mở phiên Claude Code mới sau khi cài, rồi gõ `/plugin` xem plugin đã bật chưa. Skill tự kích hoạt khi việc bạn nhờ khớp với mô tả của nó. Muốn chắc ăn thì nhắc thẳng tên skill trong câu nhờ.

</details>

<details>
<summary><b>Cập nhật và gỡ plugin thế nào?</b></summary>
<br>

```bash
claude plugin marketplace update {NAME}
claude plugin uninstall document-skills@{NAME}
```

Lệnh đầu lấy danh sách mới nhất, lệnh sau gỡ một plugin.

</details>

<details>
<summary><b>Cài nhiều plugin có sao không?</b></summary>
<br>

Mỗi plugin chiếm sẵn một phần ngữ cảnh ở mọi phiên, xem chấm màu ở cột Skill. Cài càng nhiều thì Claude càng ít chỗ cho việc chính, nên chỉ cài thứ bạn dùng. Xem chi tiết một plugin bằng `claude plugin details <tên>@{NAME}`.

</details>

<details>
<summary><b>Plugin đòi đăng nhập Slack, Notion, Canva…?</b></summary>
<br>

Nhiều plugin khai sẵn kết nối MCP tới dịch vụ ngoài. Gõ `/mcp` trong Claude Code để đăng nhập dịch vụ bạn dùng, dịch vụ không dùng thì cứ bỏ qua. Plugin ghi "Cần tài khoản" chỉ chạy được khi bạn có tài khoản dịch vụ đó.

</details>

<details>
<summary><b>Bộ pháp lý có theo luật Việt Nam không?</b></summary>
<br>

Không. Các plugin `*-legal` chủ yếu theo luật Mỹ. Dùng để tham khảo cách làm việc, không thay cho tư vấn của luật sư tại Việt Nam.

</details>

<details>
<summary><b>Plugin y khoa, dược có dùng để chẩn đoán hay kê đơn được không?</b></summary>
<br>

Không. Đây là công cụ hỗ trợ tra cứu, nghiên cứu và làm hồ sơ, phần lớn theo chuẩn của Mỹ và quốc tế (FDA, CMS, ICD-10-CM, SNOMED CT), không theo quy định của Bộ Y tế Việt Nam. Chẩn đoán, điều trị và dùng thuốc vẫn do bác sĩ, dược sĩ quyết định. Đừng đưa thông tin định danh bệnh nhân vào Claude khi nơi bạn làm việc chưa cho phép.

</details>

<a id="luu-y"></a>

## 🛡️ Lưu ý

> [!IMPORTANT]
> Repo này chỉ chứa danh sách. Khi cài, Claude Code tải plugin thẳng từ kho gốc của từng tác giả. Plugin có thể chạy lệnh, script và kết nối dịch vụ trên máy bạn, nên hãy xem kho gốc trước khi cài, nhất là plugin của cộng đồng.

{notes_md}

## 🤝 Đóng góp

Biết plugin hay mà chưa có trong danh sách? [Mở issue](https://github.com/{REPO}/issues/new) kèm link kho gốc và nhóm ngành phù hợp.

Danh sách và README được dựng tự động bằng `scripts/build.py`:

```bash
python3 -I scripts/build.py              # lấy lại danh sách từ marketplace gốc của từng tác giả
python3 -I scripts/build.py check        # cài thử từng plugin trong thư mục tạm, cập nhật cột Skill
python3 -I scripts/build.py check <tên>  # chỉ cài thử vài plugin vừa thêm hoặc sửa
python3 -I scripts/build.py readme       # chỉ dựng lại README
```

---

<p align="center">
  <sub>Chọn lọc và viết mô tả tiếng Việt: <a href="https://github.com/{owner}">{OWNER}</a> · Plugin thuộc về tác giả của từng kho gốc</sub><br>
  <sub>Thấy có ích thì tặng repo một ⭐ để nhiều người tìm thấy hơn</sub>
</p>
''', encoding='utf-8')


def check(only=()):
    """Cài thử từng plugin vào thư mục cấu hình tạm (không đụng ~/.claude), ghi số skill, agent, hook, MCP và token.
    Có tên plugin thì chỉ cài thử những plugin đó, số liệu của các plugin khác giữ nguyên."""
    plugins = json.loads(MARKET.read_text(encoding='utf-8'))['plugins']
    unknown = set(only) - {p['name'] for p in plugins}
    assert not unknown, 'Không có plugin: ' + ', '.join(sorted(unknown))
    old = json.loads(INV.read_text(encoding='utf-8')) if only and INV.exists() else {}
    inv, bad = {}, []
    with tempfile.TemporaryDirectory() as cfg:
        env = dict(os.environ, CLAUDE_CONFIG_DIR=cfg)

        def claude(*args):
            return subprocess.run(['claude', 'plugin', *args], env=env, capture_output=True, text=True)

        assert claude('marketplace', 'add', str(ROOT)).returncode == 0, 'không thêm được marketplace từ thư mục này'
        for p in plugins:
            if only and p['name'] not in only:
                if p['name'] in old:
                    inv[p['name']] = old[p['name']]
                continue
            ref = f"{p['name']}@{NAME}"
            ok = claude('install', ref).returncode == 0
            d = claude('details', ref).stdout
            n = {k: int(v) for k, v in re.findall(r'(Skills|Agents|Hooks|MCP servers) \((\d+)\)', d)}
            tok = re.search(r'Always-on:\s+~([\d,]+) tok', d)
            if not (ok and tok and any(n.values())):  # cài lỗi hoặc cài xong mà không nạp được gì
                bad.append(ref)
                continue
            inv[p['name']] = {'skills': n.get('Skills', 0), 'agents': n.get('Agents', 0), 'hooks': n.get('Hooks', 0),
                              'mcp': n.get('MCP servers', 0), 'tokens': int(tok[1].replace(',', ''))}
            print(ref, inv[p['name']], flush=True)
    INV.write_text('{\n' + ',\n'.join(f'  {json.dumps(k)}: {json.dumps(v)}' for k, v in inv.items()) + '\n}\n',
                   encoding='utf-8')
    write_readme()
    if bad:
        sys.exit('Cài lỗi hoặc không nạp được gì: ' + ', '.join(bad))


if __name__ == '__main__':
    cmd, *names = sys.argv[1:] or ['build']
    if cmd == 'check':
        check(names)
    else:
        {'build': main, 'readme': write_readme}[cmd]()

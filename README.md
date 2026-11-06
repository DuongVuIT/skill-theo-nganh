<p align="center">
  <img src="assets/banner.svg" alt="Skill theo ngành: plugin Claude Code cho từng nghề, cài bằng một lệnh" width="100%">
</p>

<p align="center">
  <img alt="plugin: 79" src="https://img.shields.io/badge/plugin-79-2563eb?style=flat-square">
  <img alt="skill: 1.283" src="https://img.shields.io/badge/skill-1.283-7c3aed?style=flat-square">
  <img alt="nhóm ngành: 11" src="https://img.shields.io/badge/nh%C3%B3m%20ng%C3%A0nh-11-0d9488?style=flat-square">
  <img alt="dành cho: Claude Code" src="https://img.shields.io/badge/d%C3%A0nh%20cho-Claude%20Code-d97706?style=flat-square">
  <img alt="mô tả: tiếng Việt" src="https://img.shields.io/badge/m%C3%B4%20t%E1%BA%A3-ti%E1%BA%BFng%20Vi%E1%BB%87t-dc2626?style=flat-square">
  <a href="https://github.com/DuongVuIT/skill-theo-nganh/commits/main"><img alt="Lần cập nhật gần nhất" src="https://img.shields.io/github/last-commit/DuongVuIT/skill-theo-nganh?style=flat-square&label=c%E1%BA%ADp%20nh%E1%BA%ADt"></a>
</p>

<p align="center">
  <b>79 plugin Claude Code chọn lọc cho 11 nhóm ngành, mô tả bằng tiếng Việt.</b><br>
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
claude plugin marketplace add DuongVuIT/skill-theo-nganh
```

Đang ở trong Claude Code thì gõ `/plugin marketplace add DuongVuIT/skill-theo-nganh` cũng được.

**2. Chọn plugin.** Gõ `/plugin` trong Claude Code để duyệt cả 79 plugin bằng menu, hoặc cài thẳng bằng tên:

```bash
claude plugin install document-skills@skill-theo-nganh
```

**3. Mở phiên Claude Code mới** là dùng được.

> [!TIP]
> Chưa biết bắt đầu từ đâu? Cài `document-skills` trước để Claude đọc, tạo và sửa file Word, Excel, PowerPoint, PDF. Plugin này hợp với gần như mọi nghề. Sau đó chọn thêm plugin của ngành bạn ở bảng dưới.

<a id="chon-theo-nganh"></a>

## 🧭 Chọn theo ngành

| Nhóm ngành | Nên thử trước |
|---|---|
| 🏗️ [**Xây dựng & BIM**](#xay-dung)<br><sub>7 plugin · 238 skill</sub> | `ddc-toolkit` · `ddc-cwicr` |
| 💻 [**Phần mềm & dữ liệu**](#phan-mem)<br><sub>8 plugin · 171 skill</sub> | `engineering` · `frontend-design` · `data` |
| ⚙️ [**Điện tử, cơ khí & sản xuất**](#dien-tu)<br><sub>2 plugin · 7 skill</sub> | `hardware` · `diode-pcb` |
| 🎨 [**Design & sáng tạo**](#design)<br><sub>7 plugin · 60 skill</sub> | `design` · `figma` · `canva` |
| 📣 [**Marketing & bán hàng**](#marketing)<br><sub>6 plugin · 118 skill</sub> | `marketing` · `sales` · `brand-voice` |
| 💰 [**Tài chính & kế toán**](#tai-chinh)<br><sub>20 plugin · 174 skill</sub> | `finance` · `financial-analysis` · `model-builder` |
| ⚖️ [**Pháp lý**](#phap-ly)<br><sub>14 plugin · 160 skill</sub> | `legal` · `commercial-legal` · `law-student` |
| 📋 [**Quản lý & vận hành**](#quan-ly)<br><sub>8 plugin · 139 skill</sub> | `product-management` · `human-resources` · `customer-support` |
| 🎓 [**Giáo dục**](#giao-duc)<br><sub>1 plugin · 1 skill</sub> | `learn-with-coursera` |
| 🔬 [**Khoa học & y sinh**](#khoa-hoc)<br><sub>3 plugin · 202 skill</sub> | `bio-research` · `ra-qm-skills` |
| 🗂️ [**Văn phòng & đa ngành**](#da-nganh)<br><sub>3 plugin · 13 skill</sub> | `document-skills` · `productivity` |

<a id="danh-sach"></a>

## 📚 Danh sách đầy đủ

Bấm tên plugin để xem kho gốc. Cột **Skill** là số skill đếm được khi cài thử, kèm chấm màu cho biết plugin chiếm sẵn bao nhiêu ngữ cảnh của Claude ở mỗi phiên:

🟢 dưới 1.000 token &nbsp;·&nbsp; 🟡 1.000 đến 3.000 token &nbsp;·&nbsp; 🔴 trên 3.000 token &nbsp;·&nbsp; ⚡ có hook tự chạy lệnh trên máy

<a id="xay-dung"></a>

### 🏗️ Xây dựng & BIM

<sub>7 plugin · 238 skill</sub>

| Plugin | Làm gì | Skill |
|---|---|:-:|
| [`ddc-toolkit`](https://github.com/datadrivenconstruction/DDC_Skills_for_AI_Agents_in_Construction/tree/HEAD/1_DDC_Toolkit)<br><sub>DataDrivenConstruction</sub> | Chuyển RVT/IFC/DWG sang dữ liệu, phân tích BIM, quản lý chi phí, tiến độ, hồ sơ tài liệu, mua sắm, hiện trường, nguồn lực, bàn giao, phát triển bền vững. Cần Python. | 54&nbsp;🟡 |
| [`ddc-cwicr`](https://github.com/datadrivenconstruction/DDC_Skills_for_AI_Agents_in_Construction/tree/HEAD/1_DDC_Toolkit/CWICR-Database)<br><sub>DataDrivenConstruction</sub> | Dự toán bằng cơ sở dữ liệu đơn giá CWICR: tính chi phí, bóc khối lượng, phân tích giá thầu, phát sinh, nhân công, vật tư, rủi ro, báo cáo. Cần Python. | 31&nbsp;🟡 |
| [`ddc-book`](https://github.com/datadrivenconstruction/DDC_Skills_for_AI_Agents_in_Construction/tree/HEAD/2_DDC_Book)<br><sub>DataDrivenConstruction</sub> | Theo từng chương sách Data-Driven Construction: chuẩn dữ liệu mở, phân tích bằng pandas và LLM, PDF/CAD sang dữ liệu, kiểm chất lượng dữ liệu, dự toán, bóc khối lượng tự động, 4D BIM và CO2, ETL, dashboard KPI, dự đoán chi phí bằng ML. Cần Python. | 67&nbsp;🟡 |
| [`ddc-insights`](https://github.com/datadrivenconstruction/DDC_Skills_for_AI_Agents_in_Construction/tree/HEAD/3_DDC_Insights)<br><sub>DataDrivenConstruction</sub> | Tự động hóa quy trình, an toàn và chất lượng, tối ưu tiến độ, tự động hóa hiện trường, agent AI cho dự án xây dựng. | 20&nbsp;🟢 |
| [`ddc-curated`](https://github.com/datadrivenconstruction/DDC_Skills_for_AI_Agents_in_Construction/tree/HEAD/4_DDC_Curated)<br><sub>DataDrivenConstruction</sub> | Hợp đồng và pháp lý, kiểm dữ liệu, sinh tài liệu, quản lý tài chính, viết prompt, đảm bảo chất lượng cho dự án xây dựng. | 20&nbsp;🟢 |
| [`ddc-innovative`](https://github.com/datadrivenconstruction/DDC_Skills_for_AI_Agents_in_Construction/tree/HEAD/5_DDC_Innovative)<br><sub>DataDrivenConstruction</sub> | Hướng mới: digital twin, khảo sát bằng drone, phát hiện lỗi bằng AI, kiểm va chạm BIM, carbon hàm chứa và ESG, mô phỏng năng lượng, IoT theo dõi vật tư, tự động hóa bằng n8n. | 34&nbsp;🟡 |
| [`ddc-open-construction-erp`](https://github.com/datadrivenconstruction/DDC_Skills_for_AI_Agents_in_Construction/tree/HEAD/6_OpenConstructionERP)<br><sub>DataDrivenConstruction</sub> | Làm việc với nền tảng OpenConstructionERP: bóc khối lượng từ BIM, dự toán và BOQ, đấu thầu, tiến độ 4D/5D, hiện trường, kết nối MCP. | 12&nbsp;🟢 |

<a id="phan-mem"></a>

### 💻 Phần mềm & dữ liệu

<sub>8 plugin · 171 skill</sub>

| Plugin | Làm gì | Skill |
|---|---|:-:|
| [`engineering`](https://github.com/anthropics/knowledge-work-plugins/tree/HEAD/engineering)<br><sub>Anthropic</sub> | Standup, review code, quyết định kiến trúc, thiết kế hệ thống, xử lý sự cố, checklist deploy, chiến lược test, nợ kỹ thuật, tài liệu kỹ thuật. | 10&nbsp;🟢 |
| [`data`](https://github.com/anthropics/knowledge-work-plugins/tree/HEAD/data)<br><sub>Anthropic</sub> | Viết SQL, khám phá dữ liệu, thống kê, vẽ biểu đồ và dashboard, biến số liệu thô thành câu chuyện dễ hiểu. | 10&nbsp;🟢 |
| [`unity`](https://unity.com)<br><sub>Unity</sub> | Plugin chính chủ của Unity cho làm game: phát triển, kiếm tiền từ game, tối ưu hiệu năng. | 31&nbsp;🔴 |
| [`frontend-design`](https://github.com/anthropics/claude-plugins-public/tree/main/plugins/frontend-design)<br><sub>Anthropic</sub> | Dựng giao diện web chỉn chu, có cá tính riêng, tránh kiểu giao diện AI na ná nhau. | 1&nbsp;🟢 |
| [`expo`](https://github.com/expo/skills/blob/main/plugins/expo/README.md) ⚡<br><sub>Expo</sub> | Skill chính chủ của Expo: build, deploy, nâng cấp, debug app React Native, dựng giao diện với Expo Router. | 24&nbsp;🟡 |
| [`aws-startup-advisor`](https://github.com/aws/agent-toolkit-for-aws) ⚡<br><sub>Amazon Web Services</sub> | Gợi ý kiến trúc, chi phí và bảo mật AWS theo đúng giai đoạn của startup. | 13&nbsp;🔴 |
| [`engineering-skills`](https://github.com/alirezarezvani/claude-skills/tree/HEAD/engineering-team)<br><sub>Alireza Rezvani</sub> | Kỹ thuật phần mềm: kiến trúc, frontend, backend, fullstack, QA, DevOps, bảo mật, AI/ML, data engineering, Playwright, TDD, kiểm tra truy cập WCAG. | 35&nbsp;🟡 |
| [`engineering-advanced-skills`](https://github.com/alirezarezvani/claude-skills/tree/HEAD/engineering)<br><sub>Alireza Rezvani</sub> | Kỹ thuật nâng cao: thiết kế agent và RAG, thiết kế cơ sở dữ liệu, migration, observability, rà dependency, review API, changelog. | 47&nbsp;🔴 |

<a id="dien-tu"></a>

### ⚙️ Điện tử, cơ khí & sản xuất

<sub>2 plugin · 7 skill</sub>

| Plugin | Làm gì | Skill |
|---|---|:-:|
| [`hardware`](https://github.com/FradSer/dotclaude/tree/main/hardware)<br><sub>Frad LEE</sub> | use-kicad-cli: kiểm DRC/ERC và xuất file gia công từ KiCad. use-openscad: dựng mô hình 3D tham số bằng OpenSCAD. | 2&nbsp;🟢 |
| [`diode-pcb`](https://github.com/diodeinc/pcb/tree/HEAD/skills)<br><sub>Diode</sub> | Thiết kế mạch in với công cụ pcb của Diode: nhập dự án KiCad, mô phỏng SPICE, tra registry linh kiện, quản lý thư viện, viết mạch bằng ngôn ngữ Zener. | 5&nbsp;🟢 |

<a id="design"></a>

### 🎨 Design & sáng tạo

<sub>7 plugin · 60 skill</sub>

| Plugin | Làm gì | Skill |
|---|---|:-:|
| [`design`](https://github.com/anthropics/knowledge-work-plugins/tree/HEAD/design)<br><sub>Anthropic</sub> | Phê bình thiết kế, quản lý design system, viết UX copy, kiểm tra khả năng tiếp cận, tổng hợp nghiên cứu người dùng, bàn giao cho dev. | 7&nbsp;🟢 |
| [`canva`](https://www.canva.com)<br><sub>Canva</sub> | Tạo, sửa, đổi kích thước và kiểm nhận diện thương hiệu cho thiết kế Canva. Cần tài khoản Canva. | 6&nbsp;🟢 |
| [`adobe-for-creativity`](https://github.com/adobe/skills/tree/main/plugins/creative-cloud/adobe-for-creativity)<br><sub>Adobe</sub> | Công cụ Adobe Creative Cloud cho ảnh, vector, thiết kế, video: sửa hàng loạt, chuyển đổi cho từng nền tảng, chạy chuỗi thao tác nhiều bước. | 15&nbsp;🟡 |
| [`miro`](https://github.com/miroapp/miro-ai/tree/HEAD/claude-plugins/miro)<br><sub>Miro</sub> | Đọc bảng Miro, vẽ sơ đồ, sinh code từ bảng. Cần tài khoản Miro. | 3&nbsp;🟢 |
| [`figma`](https://github.com/figma/mcp-server-guide)<br><sub>Figma</sub> | Đọc file thiết kế, component và design token, chuyển thiết kế thành code. Cần tài khoản Figma. | 16&nbsp;🟡 |
| [`superdesign`](https://superdesign.dev)<br><sub>Superdesign</sub> | Thiết kế hoặc làm lại UI và ảnh marketing trên canvas vô hạn: đọc codebase lấy bối cảnh, dựng design system, tạo nhiều phương án. | 1&nbsp;🟢 |
| [`example-skills`](https://github.com/anthropics/skills/tree/HEAD/skills)<br><sub>Anthropic</sub> | Bộ skill mẫu của Anthropic: canvas-design (poster, ảnh), brand-guidelines, theme-factory, algorithmic-art, slack-gif-creator, web-artifacts-builder, skill-creator… | 12&nbsp;🟢 |

<a id="marketing"></a>

### 📣 Marketing & bán hàng

<sub>6 plugin · 118 skill</sub>

| Plugin | Làm gì | Skill |
|---|---|:-:|
| [`marketing`](https://github.com/anthropics/knowledge-work-plugins/tree/HEAD/marketing)<br><sub>Anthropic</sub> | Soạn nội dung, lên kế hoạch chiến dịch, chuỗi email, SEO audit, brief đối thủ, rà giọng thương hiệu, báo cáo hiệu quả từng kênh. | 8&nbsp;🟢 |
| [`sales`](https://github.com/anthropics/knowledge-work-plugins/tree/HEAD/sales)<br><sub>Anthropic</sub> | Chuẩn bị cuộc gọi, tóm tắt và follow-up, nghiên cứu khách hàng, review deal và pipeline, dự báo doanh số. Làm việc với CRM, email, lịch, chat. | 36&nbsp;🔴 |
| [`brand-voice`](https://github.com/anthropics/knowledge-work-plugins/tree/HEAD/partner-built/brand-voice)<br><sub>Tribe AI</sub> | Rút giọng thương hiệu từ tài liệu và hội thoại sẵn có, viết guideline áp dụng được, kiểm nội dung AI viết có đúng giọng không. | 6&nbsp;🟡 |
| [`amazon-selling-partner`](https://github.com/amzn/selling-partner-agentic-toolkit)<br><sub>Amazon</sub> | Kết nối Amazon Seller Central: hỏi doanh số, tồn kho, hiệu quả listing, nhận gợi ý từ dữ liệu của chính bạn. Cần tài khoản người bán. | 14&nbsp;🟡 |
| [`marketing-skills`](https://github.com/alirezarezvani/claude-skills/tree/HEAD/marketing-skill)<br><sub>Alireza Rezvani</sub> | Marketing chia 8 nhóm: nội dung, SEO và AEO, tối ưu chuyển đổi, kênh, tăng trưởng, phân tích thị trường, hỗ trợ bán hàng, tăng trưởng trên X. Kèm công cụ Python. | 49&nbsp;🟡 |
| [`business-growth-skills`](https://github.com/alirezarezvani/claude-skills/tree/HEAD/business-growth)<br><sub>Alireza Rezvani</sub> | Tăng trưởng kinh doanh: customer success, kỹ sư bán hàng, revenue operations, soạn hợp đồng và đề xuất. | 5&nbsp;🟢 |

<a id="tai-chinh"></a>

### 💰 Tài chính & kế toán

<sub>20 plugin · 174 skill</sub>

| Plugin | Làm gì | Skill |
|---|---|:-:|
| [`finance`](https://github.com/anthropics/knowledge-work-plugins/tree/HEAD/finance)<br><sub>Anthropic</sub> | Bút toán, đối chiếu, lập báo cáo tài chính, phân tích chênh lệch, chuẩn bị kiểm toán, khóa sổ cuối tháng. | 8&nbsp;🟢 |
| [`intuit-quickbooks`](https://github.com/intuit/quickbooks-claude-plugin)<br><sub>Intuit</sub> | Đọc sức khỏe tài chính từ QuickBooks: lãi lỗ, dòng tiền, bảng cân đối, công nợ phải thu, so với ngành, chi phí lương. Cần tài khoản QuickBooks. | 10&nbsp;🟡 |
| [`financial-analysis`](https://github.com/anthropics/financial-services/tree/HEAD/plugins/vertical-plugins/financial-analysis)<br><sub>Anthropic</sub> | Nền tảng của bộ Financial Services: mô hình DCF, comps, LBO, 3 báo cáo tài chính, phân tích cạnh tranh, kiểm tra deck. | 20&nbsp;🟡 |
| [`investment-banking`](https://github.com/anthropics/financial-services/tree/HEAD/plugins/vertical-plugins/investment-banking)<br><sub>Anthropic</sub> | Ngân hàng đầu tư: thông tin khách hàng và thị trường, dựng deck, phân tích tài chính, quản lý giao dịch. | 16&nbsp;🟡 |
| [`equity-research`](https://github.com/anthropics/financial-services/tree/HEAD/plugins/vertical-plugins/equity-research)<br><sub>Anthropic</sub> | Nghiên cứu cổ phiếu: phân tích kết quả kinh doanh, viết báo cáo khởi tạo. | 18&nbsp;🟡 |
| [`private-equity`](https://github.com/anthropics/financial-services/tree/HEAD/plugins/vertical-plugins/private-equity)<br><sub>Anthropic</sub> | Quỹ đầu tư tư nhân: tìm công ty mục tiêu, quản lý CRM, tiếp cận nhà sáng lập. | 20&nbsp;🟡 |
| [`fund-admin`](https://github.com/anthropics/financial-services/tree/HEAD/plugins/vertical-plugins/fund-admin)<br><sub>Anthropic</sub> | Quản trị quỹ: đối chiếu sổ cái, truy chênh lệch, trích trước, roll-forward, khớp NAV. | 6&nbsp;🟢 |
| [`pitch-agent`](https://github.com/anthropics/financial-services/tree/HEAD/plugins/agent-plugins/pitch-agent)<br><sub>Anthropic</sub> | Dựng pitch deck từ comps, giao dịch tiền lệ và LBO. | 11&nbsp;🟡 |
| [`market-researcher`](https://github.com/anthropics/financial-services/tree/HEAD/plugins/agent-plugins/market-researcher)<br><sub>Anthropic</sub> | Nghiên cứu thị trường: tổng quan ngành, bức tranh cạnh tranh, ý tưởng đầu tư. | 5&nbsp;🟢 |
| [`earnings-reviewer`](https://github.com/anthropics/financial-services/tree/HEAD/plugins/agent-plugins/earnings-reviewer)<br><sub>Anthropic</sub> | Đọc cuộc gọi kết quả kinh doanh, cập nhật mô hình, viết nhận định. | 6&nbsp;🟢 |
| [`meeting-prep-agent`](https://github.com/anthropics/financial-services/tree/HEAD/plugins/agent-plugins/meeting-prep-agent)<br><sub>Anthropic</sub> | Soạn tài liệu chuẩn bị trước buổi gặp khách hàng. | 4&nbsp;🟢 |
| [`model-builder`](https://github.com/anthropics/financial-services/tree/HEAD/plugins/agent-plugins/model-builder)<br><sub>Anthropic</sub> | Dựng mô hình DCF, LBO, 3 báo cáo, comps ngay trong Excel. | 6&nbsp;🟢 |
| [`gl-reconciler`](https://github.com/anthropics/financial-services/tree/HEAD/plugins/agent-plugins/gl-reconciler)<br><sub>Anthropic</sub> | Đối chiếu sổ cái: tìm chênh lệch, truy nguyên nhân, chuyển người duyệt. | 4&nbsp;🟢 |
| [`kyc-screener`](https://github.com/anthropics/financial-services/tree/HEAD/plugins/agent-plugins/kyc-screener)<br><sub>Anthropic</sub> | KYC: đọc hồ sơ mở tài khoản, chạy bộ quy tắc, đánh dấu chỗ còn thiếu. | 3&nbsp;🟢 |
| [`valuation-reviewer`](https://github.com/anthropics/financial-services/tree/HEAD/plugins/agent-plugins/valuation-reviewer)<br><sub>Anthropic</sub> | Rà định giá: từ hồ sơ của GP đến định giá và báo cáo cho LP. | 4&nbsp;🟢 |
| [`month-end-closer`](https://github.com/anthropics/financial-services/tree/HEAD/plugins/agent-plugins/month-end-closer)<br><sub>Anthropic</sub> | Khóa sổ cuối tháng: trích trước, roll-forward, thuyết minh. | 5&nbsp;🟢 |
| [`statement-auditor`](https://github.com/anthropics/financial-services/tree/HEAD/plugins/agent-plugins/statement-auditor)<br><sub>Anthropic</sub> | Rà sao kê gửi nhà đầu tư (LP) trước khi phát hành. | 3&nbsp;🟢 |
| [`lseg`](https://github.com/anthropics/financial-services/tree/HEAD/plugins/partner-built/lseg)<br><sub>Anthropic</sub> | Dùng dữ liệu LSEG: trái phiếu, đường cong lợi suất, FX carry, quyền chọn, dashboard vĩ mô. | 16&nbsp;🟢 |
| [`sp-global`](https://github.com/anthropics/financial-services/tree/HEAD/plugins/partner-built/spglobal)<br><sub>Anthropic</sub> | Dùng dữ liệu S&P Global: tearsheet công ty, xem trước kết quả kinh doanh, tóm tắt giao dịch. | 3&nbsp;🟢 |
| [`finance-skills`](https://github.com/alirezarezvani/claude-skills/tree/HEAD/finance)<br><sub>Alireza Rezvani</sub> | Tài chính: phân tích chỉ số, định giá DCF, ngân sách và dự báo; chỉ số SaaS (ARR, MRR, churn, CAC, LTV); tư vấn đầu tư; khóa sổ cuối tháng. | 6&nbsp;🟢 |

<a id="phap-ly"></a>

### ⚖️ Pháp lý

<sub>14 plugin · 160 skill</sub>

| Plugin | Làm gì | Skill |
|---|---|:-:|
| [`legal`](https://github.com/anthropics/knowledge-work-plugins/tree/HEAD/legal)<br><sub>Anthropic</sub> | Rà soát hợp đồng, phân loại NDA, quy trình tuân thủ cho pháp chế nội bộ, soạn tóm tắt pháp lý. | 9&nbsp;🟢 |
| [`commercial-legal`](https://github.com/anthropics/claude-for-legal/tree/HEAD/commercial-legal)<br><sub>Anthropic</sub> | Hợp đồng thương mại: hợp đồng nhà cung cấp, NDA, SaaS, theo dõi hạn gia hạn và hủy. | 12&nbsp;🟡 |
| [`privacy-legal`](https://github.com/anthropics/claude-for-legal/tree/HEAD/privacy-legal)<br><sub>Anthropic</sub> | Dữ liệu cá nhân: đánh giá tác động (PIA), thỏa thuận xử lý dữ liệu (DPA), yêu cầu truy cập dữ liệu (DSAR). | 9&nbsp;🟢 |
| [`product-legal`](https://github.com/anthropics/claude-for-legal/tree/HEAD/product-legal)<br><sub>Anthropic</sub> | Pháp lý sản phẩm: rủi ro khi ra mắt, kiểm các tuyên bố quảng cáo. | 7&nbsp;🟢 |
| [`corporate-legal`](https://github.com/anthropics/claude-for-legal/tree/HEAD/corporate-legal)<br><sub>Anthropic</sub> | Doanh nghiệp: thẩm định M&A, biên bản hội đồng quản trị. | 13&nbsp;🟡 |
| [`employment-legal`](https://github.com/anthropics/claude-for-legal/tree/HEAD/employment-legal)<br><sub>Anthropic</sub> | Luật lao động theo từng bang của Mỹ. | 20&nbsp;🟡 |
| [`regulatory-legal`](https://github.com/anthropics/claude-for-legal/tree/HEAD/regulatory-legal)<br><sub>Anthropic</sub> | Theo dõi quy định mới. | 9&nbsp;🟢 |
| [`ai-governance-legal`](https://github.com/anthropics/claude-for-legal/tree/HEAD/ai-governance-legal)<br><sub>Anthropic</sub> | Quản trị AI: rà use case AI, điều khoản trong hợp đồng nhà cung cấp AI. | 10&nbsp;🟡 |
| [`litigation-legal`](https://github.com/anthropics/claude-for-legal/tree/HEAD/litigation-legal)<br><sub>Anthropic</sub> | Tranh tụng: claim chart, niên biểu vụ việc, chuẩn bị lấy lời khai. | 19&nbsp;🟡 |
| [`law-student`](https://github.com/anthropics/claude-for-legal/tree/HEAD/law-student)<br><sub>Anthropic</sub> | Cho sinh viên luật: hỏi đáp kiểu Socratic, tóm tắt án lệ, ôn thi. | 13&nbsp;🟢 |
| [`legal-clinic`](https://github.com/anthropics/claude-for-legal/tree/HEAD/legal-clinic)<br><sub>Anthropic</sub> | Cho phòng tư vấn pháp lý của trường luật. | 16&nbsp;🟡 |
| [`legal-builder-hub`](https://github.com/anthropics/claude-for-legal/tree/HEAD/legal-builder-hub)<br><sub>Anthropic</sub> | Tìm, đánh giá và cài skill pháp lý của cộng đồng, có bước rà bảo mật. | 10&nbsp;🟢 |
| [`ip-legal`](https://github.com/anthropics/claude-for-legal/tree/HEAD/ip-legal)<br><sub>Anthropic</sub> | Sở hữu trí tuệ: nhãn hiệu, tự do vận hành (FTO), sáng chế, thư cảnh báo và DMCA, giấy phép mã nguồn mở. | 12&nbsp;🟡 |
| [`cocounsel-legal`](https://github.com/anthropics/claude-for-legal/tree/HEAD/external_plugins/cocounsel-legal)<br><sub>Thomson Reuters</sub> | Westlaw Deep Research của Thomson Reuters. Cần tài khoản Thomson Reuters. | 1&nbsp;🟢 |

<a id="quan-ly"></a>

### 📋 Quản lý & vận hành

<sub>8 plugin · 139 skill</sub>

| Plugin | Làm gì | Skill |
|---|---|:-:|
| [`product-management`](https://github.com/anthropics/knowledge-work-plugins/tree/HEAD/product-management)<br><sub>Anthropic</sub> | Viết spec tính năng, lập roadmap, lên sprint, brainstorm, tổng hợp nghiên cứu người dùng, cập nhật cho các bên liên quan, theo dõi đối thủ. | 9&nbsp;🟢 |
| [`operations`](https://github.com/anthropics/knowledge-work-plugins/tree/HEAD/operations)<br><sub>Anthropic</sub> | Quản lý nhà cung cấp, viết tài liệu quy trình, quản lý thay đổi, hoạch định năng lực, theo dõi tuân thủ. | 9&nbsp;🟢 |
| [`human-resources`](https://github.com/anthropics/knowledge-work-plugins/tree/HEAD/human-resources)<br><sub>Anthropic</sub> | Tuyển dụng, onboarding, đánh giá hiệu suất, phân tích lương thưởng, tư vấn chính sách nhân sự. | 9&nbsp;🟢 |
| [`customer-support`](https://github.com/anthropics/knowledge-work-plugins/tree/HEAD/customer-support)<br><sub>Anthropic</sub> | Phân loại ticket, soạn câu trả lời, chuyển cấp xử lý, tìm bối cảnh khách hàng, biến ca đã xử lý thành bài tự trợ giúp. | 5&nbsp;🟢 |
| [`small-business`](https://github.com/anthropics/knowledge-work-plugins/tree/HEAD/small-business)<br><sub>Anthropic</sub> | Quy trình dựng sẵn để vận hành và phát triển doanh nghiệp nhỏ. Bước nào đụng đến tiền cũng chờ bạn duyệt. | 44&nbsp;🔴 |
| [`c-level-skills`](https://github.com/alirezarezvani/claude-skills/tree/HEAD/c-level-advisor)<br><sub>Alireza Rezvani</sub> | Cố vấn cấp lãnh đạo: hội đồng quản trị ảo gồm CEO, CTO, COO, CPO, CMO, CFO, CRO, CISO, CHRO, thêm cố vấn pháp lý, dữ liệu, AI. | 34&nbsp;🟡 |
| [`product-skills`](https://github.com/alirezarezvani/claude-skills/tree/HEAD/product-team)<br><sub>Alireza Rezvani</sub> | Quản lý sản phẩm kèm công cụ Python: vòng discovery liên tục và bộ công cụ cho product manager. | 17&nbsp;🟡 |
| [`pm-skills`](https://github.com/alirezarezvani/claude-skills/tree/HEAD/project-management)<br><sub>Alireza Rezvani</sub> | Quản lý dự án kèm công cụ Python: lấy dữ liệu Jira, đo luồng Kanban, dự báo tiến độ bằng Monte Carlo. | 12&nbsp;🟢 |

<a id="giao-duc"></a>

### 🎓 Giáo dục

<sub>1 plugin · 1 skill</sub>

| Plugin | Làm gì | Skill |
|---|---|:-:|
| [`learn-with-coursera`](https://github.com/coursera/skills/tree/HEAD/skills)<br><sub>Coursera</sub> | Hỏi 3 câu (chủ đề, trình độ, hình thức học) rồi tìm trong kho Coursera để đưa ra lộ trình học. | 1&nbsp;🟢 |

<a id="khoa-hoc"></a>

### 🔬 Khoa học & y sinh

<sub>3 plugin · 202 skill</sub>

| Plugin | Làm gì | Skill |
|---|---|:-:|
| [`bio-research`](https://github.com/anthropics/knowledge-work-plugins/tree/HEAD/bio-research)<br><sub>Anthropic</sub> | Kết nối công cụ và cơ sở dữ liệu nghiên cứu tiền lâm sàng: tra tài liệu, phân tích hệ gen, xếp hạng đích điều trị. | 6&nbsp;🟢 |
| [`ra-qm-skills`](https://github.com/alirezarezvani/claude-skills/tree/HEAD/ra-qm-team)<br><sub>Alireza Rezvani</sub> | Quy chuẩn và quản lý chất lượng cho thiết bị y tế: ISO 13485, MDR 2017/745, FDA 510(k)/PMA, GDPR, ISO 27001, CAPA, quản lý rủi ro, đánh giá lâm sàng, SOC 2. | 19&nbsp;🟡 |
| [`scientific-agent-skills`](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills)<br><sub>K-Dense</sub> | Nghiên cứu khoa học: tin sinh học và hệ gen, protein, hóa học, ảnh y khoa, máy tính lượng tử, học máy, vẽ hình khoa học, tra cứu tài liệu. Rất nặng: chiếm gần 20 nghìn token ngữ cảnh mỗi phiên, chỉ cài khi cần. | 177&nbsp;🔴 |

<a id="da-nganh"></a>

### 🗂️ Văn phòng & đa ngành

<sub>3 plugin · 13 skill</sub>

| Plugin | Làm gì | Skill |
|---|---|:-:|
| [`productivity`](https://github.com/anthropics/knowledge-work-plugins/tree/HEAD/productivity)<br><sub>Anthropic</sub> | Quản lý việc, lên kế hoạch trong ngày, ghi nhớ bối cảnh công việc; đồng bộ với lịch, email, chat. | 4&nbsp;🟢 |
| [`enterprise-search`](https://github.com/anthropics/knowledge-work-plugins/tree/HEAD/enterprise-search)<br><sub>Anthropic</sub> | Tìm trong email, chat, tài liệu và wiki của công ty từ một chỗ. | 5&nbsp;🟢 |
| [`document-skills`](https://github.com/anthropics/skills/tree/HEAD/skills)<br><sub>Anthropic</sub> | Đọc, tạo và chỉnh file Word, Excel, PowerPoint, PDF. Có ích cho gần như mọi nghề. | 4&nbsp;🟢 |

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
claude plugin marketplace update skill-theo-nganh
claude plugin uninstall document-skills@skill-theo-nganh
```

Lệnh đầu lấy danh sách mới nhất, lệnh sau gỡ một plugin.

</details>

<details>
<summary><b>Cài nhiều plugin có sao không?</b></summary>
<br>

Mỗi plugin chiếm sẵn một phần ngữ cảnh ở mọi phiên, xem chấm màu ở cột Skill. Cài càng nhiều thì Claude càng ít chỗ cho việc chính, nên chỉ cài thứ bạn dùng. Xem chi tiết một plugin bằng `claude plugin details <tên>@skill-theo-nganh`.

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

<a id="luu-y"></a>

## 🛡️ Lưu ý

> [!IMPORTANT]
> Repo này chỉ chứa danh sách. Khi cài, Claude Code tải plugin thẳng từ kho gốc của từng tác giả. Plugin có thể chạy lệnh, script và kết nối dịch vụ trên máy bạn, nên hãy xem kho gốc trước khi cài, nhất là plugin của cộng đồng.

- Dự án cộng đồng, không liên kết với Anthropic hay các hãng có tên trong danh sách.
- `expo` và `aws-startup-advisor` có hook ⚡ tự chạy lệnh trên máy. Đọc kho gốc trước khi bật.
- Các plugin `ddc-*`, `diode-pcb` và `scientific-agent-skills` vốn là kho skill rời. Marketplace này bọc chúng thành plugin và ghim theo một commit cố định.
- Skill chỉ có trong app Claude không có ở đây. Plugin `operations` của bộ Financial Services trùng tên với `operations` của Knowledge Work nên không đưa vào.

## 🤝 Đóng góp

Biết plugin hay mà chưa có trong danh sách? [Mở issue](https://github.com/DuongVuIT/skill-theo-nganh/issues/new) kèm link kho gốc và nhóm ngành phù hợp.

Danh sách và README được dựng tự động bằng `scripts/build.py`:

```bash
python3 -I scripts/build.py          # lấy lại danh sách từ marketplace gốc của từng tác giả
python3 -I scripts/build.py check    # cài thử từng plugin trong thư mục tạm, cập nhật cột Skill
python3 -I scripts/build.py readme   # chỉ dựng lại README
```

---

<p align="center">
  <sub>Chọn lọc và viết mô tả tiếng Việt: <a href="https://github.com/DuongVuIT">Vũ Đại Dương</a> · Plugin thuộc về tác giả của từng kho gốc</sub><br>
  <sub>Thấy có ích thì tặng repo một ⭐ để nhiều người tìm thấy hơn</sub>
</p>

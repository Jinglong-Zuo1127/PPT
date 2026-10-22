# LLM Agent代表性工作演进路线

- **LLM_Agent_Timeline.pptx**：一页16:9可编辑PPT。
- **LLM_Agent_Timeline.png**：2881×1620高清预览。
- **LLM_Agent_Timeline.pdf**：备用PDF。
- **references.md**：逐项日期、贡献、来源、原图纠错及素材链接。
- **assets/**：实际使用的官方图片及裁剪前原始素材。
- **generate_ppt.py**：生成脚本；所有文字、时间轴、竖线和标签为基础原生对象。
- **validate_ppt.py / validation_report.json**：包结构、关系、渲染文字边界与重叠检查。

重新生成：

```bash
python -m pip install -r requirements.txt
python generate_ppt.py
```

本机已安装LibreOffice和PyMuPDF时，可以重新导出PDF和PNG：

```bash
python generate_ppt.py --render
python validate_ppt.py
```

Windows/WPS常见环境可使用微软雅黑。Linux导出预览时，附带fontconfig.conf将微软雅黑映射至Noto Sans CJK SC，不修改系统字体配置。

说明：月份按预印本v1与官方演示区分；横轴非等比例，方法长期并行。期刊PDF受代理403限制，来源身份通过作者官方仓库核对；具体核实范围在references.md中说明。

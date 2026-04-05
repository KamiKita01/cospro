import weasyprint

# HTML 파일 경로
html_file = 'cospro_guide.html'

# 출력 PDF 파일 경로
pdf_file = 'cospro_guide.pdf'

# HTML을 PDF로 변환
weasyprint.HTML(html_file).write_pdf(pdf_file)

print(f"PDF 생성 완료: {pdf_file}")
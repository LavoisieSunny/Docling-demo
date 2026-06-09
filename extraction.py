from docling.document_converter import DocumentConverter
from utiles.sitemap import get_sitemap_urls

converter = DocumentConverter()

#Basic PDF Extraction

result = converter.convert("pdfs/MA_20_2026.pdf")

document = result.document
markdown_output = document.export_to_markdown()
json_output = document.export_to_dict()

print(json_output)
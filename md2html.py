#!/usr/bin/env python3
"""
将subtopic目录中的Markdown文件转换为HTML格式，保持与主网站相同的样式。
"""

import os
import re
import markdown
import glob
from bs4 import BeautifulSoup

# 获取当前目录
base_dir = os.path.dirname(os.path.abspath(__file__))
subtopic_dir = os.path.join(base_dir, 'subtopic')
output_dir = os.path.join(base_dir, 'subtopic_html')

# 创建输出目录（如果不存在）
os.makedirs(output_dir, exist_ok=True)

# HTML模板
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Awesome LLM-Safety</title>
    <link rel="stylesheet" href="../style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        .markdown-content {{
            padding: 20px;
        }}
        .markdown-content h1 {{
            font-size: 2rem;
            color: var(--primary-color);
            margin-bottom: 1.5rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid var(--border-color);
        }}
        .markdown-content h2 {{
            font-size: 1.6rem;
            color: var(--secondary-color);
            margin-top: 2rem;
            margin-bottom: 1rem;
        }}
        .markdown-content table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            font-size: 0.9rem;
        }}
        .markdown-content th, .markdown-content td {{
            padding: 12px 15px;
            border: 1px solid var(--border-color);
        }}
        .markdown-content th {{
            background-color: var(--primary-color);
            color: white;
            font-weight: bold;
            text-align: left;
        }}
        .markdown-content tr:nth-child(even) {{
            background-color: var(--light-bg);
        }}
        .markdown-content tr:hover {{
            background-color: #ddd;
        }}
        .back-to-home {{
            display: inline-block;
            margin: 20px 0;
            padding: 10px 15px;
            background-color: var(--primary-color);
            color: white;
            border-radius: 4px;
            text-decoration: none;
            font-weight: bold;
        }}
        .back-to-home:hover {{
            background-color: var(--secondary-color);
            color: white;
        }}
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h1>🛡️ Awesome LLM-Safety 🛡️</h1>
            <div class="language-switch">
                <a href="../index.html">English</a> | 
                <a href="../index_cn.html">中文</a>
            </div>
        </div>
    </header>

    <div class="container">
        <a href="../index.html" class="back-to-home">
            <i class="fas fa-arrow-left"></i> Back to Home
        </a>
        
        <div class="markdown-content">
            {content}
        </div>
        
        <a href="../index.html" class="back-to-home">
            <i class="fas fa-arrow-left"></i> Back to Home
        </a>
    </div>

    <footer>
        <div class="container">
            <div class="footer-content">
                <p>Created by <a href="https://github.com/ydyjya">ydyjya</a></p>
                <p>Contact: zhouzhenhong@bupt.edu.cn</p>
            </div>
            <div class="footer-links">
                <a href="https://github.com/ydyjya/Awesome-LLM-Safety" target="_blank">
                    <i class="fab fa-github"></i> GitHub Repository
                </a>
            </div>
        </div>
    </footer>
</body>
</html>
"""

# 自定义Markdown转HTML的扩展，用于处理表格等特殊格式
markdown_extensions = [
    'tables',
    'fenced_code',
    'codehilite',
    'nl2br',
    'attr_list',
    'def_list',
    'footnotes',
    'md_in_html'
]

def convert_md_to_html(md_file, html_file):
    """将单个Markdown文件转换为HTML文件"""
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # 使用Python-Markdown库将Markdown转换为HTML
    html_content = markdown.markdown(md_content, extensions=markdown_extensions)
    
    # 提取标题
    title_match = re.search(r'^# (.+?)$', md_content, re.MULTILINE)
    title = title_match.group(1) if title_match else os.path.basename(md_file).replace('.md', '')
    
    # 使用模板生成完整的HTML文件
    complete_html = html_template.format(title=title, content=html_content)
    
    # 使用BeautifulSoup美化HTML
    soup = BeautifulSoup(complete_html, 'html.parser')
    beautified_html = soup.prettify()
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(beautified_html)
    
    print(f"转换完成: {md_file} -> {html_file}")

def main():
    """处理subtopic目录中的所有Markdown文件"""
    md_files = glob.glob(os.path.join(subtopic_dir, '*.md'))
    
    for md_file in md_files:
        basename = os.path.basename(md_file)
        html_file = os.path.join(output_dir, basename.replace('.md', '.html'))
        convert_md_to_html(md_file, html_file)
    
    print(f"共转换了 {len(md_files)} 个文件")

if __name__ == "__main__":
    main() 
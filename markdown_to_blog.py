#!/usr/bin/env python3

import os
import re
import markdown
from datetime import datetime
import argparse

def create_blog_html(title, date, content, math=True):
    """Create HTML blog post matching the existing format"""
    
    # MathJax script if math is enabled
    mathjax_script = '''
    <!-- MathJax Configuration -->
    <script>
        MathJax = {
            tex: {
                inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
                displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']]
            }
        };
    </script>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>''' if math else ''
    
    html_template = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Raymond Luo</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">{mathjax_script}
</head>
<body>
    <div class="container">
        <header>
            <h1>Raymond Luo</h1>
            <nav>
                <a href="index.html">About</a>
                <a href="projects.html">Projects</a>
                <a href="blog.html">Blog</a>
            </nav>
        </header>

        <main>
            <section>
                <div class="blog-nav">
                    <a href="blog.html">← Back to Blog</a>
                </div>
                
                <article class="blog-post-full">
                    <h1>{title}</h1>
                    <p class="blog-date">{date}</p>
                    
                    <div class="blog-content">
                        {content}
                    </div>
                </article>
            </section>
        </main>

        <footer>
            <div class="contact-buttons">
                <a href="mailto:rayluo@mit.edu" class="btn btn-email" title="Email">✉</a>
                <a href="https://www.linkedin.com/in/raymondlu0/" target="_blank" class="btn btn-linkedin" title="LinkedIn">in</a>
            </div>
        </footer>
    </div>
</body>
</html>'''
    
    return html_template

def parse_markdown_file(filepath):
    """Parse markdown file with YAML front matter"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract YAML front matter
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            front_matter = parts[1].strip()
            markdown_content = parts[2].strip()
        else:
            front_matter = ""
            markdown_content = content
    else:
        front_matter = ""
        markdown_content = content
    
    # Parse front matter
    metadata = {}
    for line in front_matter.split('\n'):
        if ':' in line and not line.strip().startswith('#'):
            key, value = line.split(':', 1)
            metadata[key.strip()] = value.strip().strip('"')
    
    return metadata, markdown_content

def convert_markdown_to_html(markdown_content):
    """Convert markdown to HTML with math support"""
    # Configure markdown with math support
    md = markdown.Markdown(extensions=['extra', 'codehilite'])
    html_content = md.convert(markdown_content)
    return html_content

def create_blog_post_from_markdown(markdown_file):
    """Convert a markdown file to an HTML blog post"""
    metadata, markdown_content = parse_markdown_file(markdown_file)
    
    title = metadata.get('title', 'Untitled Post')
    date = metadata.get('date', datetime.now().strftime('%B %d, %Y'))
    math = metadata.get('math', 'true').lower() == 'true'
    
    # Convert markdown to HTML
    html_content = convert_markdown_to_html(markdown_content)
    
    # Create full HTML page
    full_html = create_blog_html(title, date, html_content, math)
    
    # Generate filename from title only
    slug = re.sub(r'[^a-zA-Z0-9\s]', '', title).strip().replace(' ', '-').lower()
    filename = f"blog-post-{slug}.html"
    
    return filename, full_html

def update_blog_index(title, date, filename, excerpt):
    """Update blog.html to include the new post"""
    try:
        with open('blog.html', 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_post_html = f'''                <div class="blog-post">
                    <h3><a href="{filename}">{title}</a></h3>
                    <p class="blog-date">{date}</p>
                    <p>{excerpt}</p>
                    <p><a href="{filename}">Read more</a></p>
                </div>
                
'''
        
        # Insert after the opening <section> tag
        section_pattern = r'(<section>\s*)'
        replacement = f'\\1{new_post_html}'
        updated_content = re.sub(section_pattern, replacement, content, count=1)
        
        with open('blog.html', 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print(f"Updated blog.html to include {title}")
        
    except Exception as e:
        print(f"Warning: Could not update blog.html: {e}")

def main():
    parser = argparse.ArgumentParser(description='Convert markdown blog post to HTML')
    parser.add_argument('markdown_file', help='Path to markdown file')
    parser.add_argument('--update-index', action='store_true', help='Update blog.html index')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.markdown_file):
        print(f"Error: File {args.markdown_file} not found")
        return
    
    try:
        filename, html_content = create_blog_post_from_markdown(args.markdown_file)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"Created {filename}")
        
        if args.update_index:
            # Extract metadata for index
            metadata, markdown_content = parse_markdown_file(args.markdown_file)
            title = metadata.get('title', 'Untitled Post')
            date = metadata.get('date', datetime.now().strftime('%B %d, %Y'))
            
            # Create excerpt from first paragraph (clean up markdown)
            lines = markdown_content.split('\n')
            excerpt = next((line for line in lines if line.strip() and not line.startswith('#')), "")
            # Clean up markdown formatting for excerpt
            excerpt = re.sub(r'\*\*(.*?)\*\*', r'\1', excerpt)  # Remove bold
            excerpt = re.sub(r'\*(.*?)\*', r'\1', excerpt)      # Remove italic
            excerpt = excerpt[:150]
            
            update_blog_index(title, date, filename, excerpt)
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main() 
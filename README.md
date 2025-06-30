# Raymond Luo's Personal Website

This is my personal website with a hybrid blogging system. You can write blog posts in **markdown** (much easier!) while keeping all your existing HTML blog functionality intact.

## 🎯 What This Setup Gives You

✅ **Your existing blog works exactly as before**  
✅ **Write new posts in markdown instead of HTML**  
✅ **Automatic conversion to your blog's HTML format**  
✅ **LaTeX math support**  
✅ **Keep your exact styling and layout**

## 🚀 Quick Start - Writing a New Blog Post

### Method 1: Easy Script (Recommended)
```bash
# Create a new post
ruby new_post.rb "My Amazing New Post"

# Edit the created markdown file
# Then convert it to HTML and update your blog:
python3 markdown_to_blog.py 2024-12-29-my-amazing-new-post.md --update-index
```

### Method 2: Manual Creation
1. Create a markdown file with this format:
```markdown
---
title: "Your Post Title"
date: December 29, 2024
math: true
---

Your content here in **markdown**!

You can use math: $E = mc^2$

And display equations:
$$\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}$$
```

2. Convert to HTML:
```bash
python3 markdown_to_blog.py your-post.md --update-index
```

## 📝 Markdown Features You Can Use

- **Headers**: `## Section`, `### Subsection`
- **Bold**: `**bold text**`
- **Italic**: `*italic text*`
- **Links**: `[text](URL)`
- **Math**: `$inline$` or `$$display$$`
- **Code**: `` `inline code` `` or triple backticks for blocks
- **Lists**: Use `-` or `1.` for bullets/numbers

## 🔧 Setup (One-time)

1. **Install dependencies:**
   ```bash
   # Install Jekyll (optional, for development server)
   bundle install --path vendor/bundle
   
   # Install Python markdown (required for conversion)
   pip3 install markdown
   ```

2. **Make scripts executable:**
   ```bash
   chmod +x new_post.rb markdown_to_blog.py
   ```

## 🛠️ How It Works

1. **Your existing blog** (`blog-post-1.html`, `blog-post-2.html`, `blog.html`) works unchanged
2. **New posts** are written in markdown, then converted to HTML matching your exact format
3. **Blog index** (`blog.html`) is automatically updated with new posts
4. **Everything** uses your existing CSS and styling

## 📁 File Structure

```
raymondluo.github.io/
├── blog-post-1.html          # Your existing posts (unchanged)
├── blog-post-2.html          # Your existing posts (unchanged)
├── blog.html                 # Blog index (auto-updated)
├── index.html                # Your main pages (unchanged)
├── projects.html             # Your main pages (unchanged)
├── style.css                 # Your styling (unchanged)
├── new_post.rb               # Helper to create markdown posts
├── markdown_to_blog.py       # Converter script
└── 2024-12-29-post-name.md   # Your new markdown posts
```

## 🧪 Testing

To test locally with Jekyll:
```bash
bundle exec jekyll serve --port 4000
# Visit http://localhost:4000
```

## ✨ Example Workflow

```bash
# 1. Create new post
ruby new_post.rb "Solving a Cool Math Problem"

# 2. Edit the created file (2024-12-29-solving-a-cool-math-problem.md)
# Add your content in markdown...

# 3. Convert and publish
python3 markdown_to_blog.py 2024-12-29-solving-a-cool-math-problem.md --update-index

# Done! Your blog now has a new post in your exact format
```

## 🚀 Deployment

Just commit and push to GitHub as usual. GitHub Pages will serve your HTML files directly.
import os

# Define the folder structure
folders = [
    "blog_site/app/static/css",
    "blog_site/app/static/js",
    "blog_site/app/static/images",
    "blog_site/app/templates",
    "blog_site/database"
]

files = {
    "blog_site/app/__init__.py": "",
    "blog_site/app/routes.py": "",
    "blog_site/app/models.py": "",
    "blog_site/app/forms.py": "",
    "blog_site/config.py": "# Configuration settings like SECRET_KEY, DB URI\n",
    "blog_site/run.py": "# Entry point for the Flask app\n",
    "blog_site/requirements.txt": "flask\n",
    "blog_site/app/static/css/styles.css": "/* Add your CSS here */\n",
    "blog_site/app/static/js/scripts.js": "// Add your JS here\n"
}

# Template HTML files
template_files = [
    "base.html",
    "index.html",           # Main landing page (blog list)
    "blog.html",            # Blog details
    "videos.html",          # Video page
    "audios.html",          # Audio page
    "news.html",            # News page
    "admin_login.html",     # Admin login
    "admin_dashboard.html", # Admin CRUD dashboard
    "add_blog.html",
    "edit_blog.html"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files with content
for file_path, content in files.items():
    with open(file_path, "w") as f:
        f.write(content)

# Create HTML templates
for html_file in template_files:
    with open(f"blog_site/app/templates/{html_file}", "w") as f:
        f.write(f"<!-- {html_file} template -->\n")

print("✅ Folder structure and base files created successfully!")

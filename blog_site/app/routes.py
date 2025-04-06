from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.models import Blog, db  # ✅ make sure db is imported
from config import ADMIN_USERNAME, ADMIN_PASSWORD

main = Blueprint('main', __name__)

@main.route('/')
def home():
    latest_post = Blog.query.order_by(Blog.created_at.desc()).first()
    return render_template('index.html', post=latest_post)


@main.route('/blogs')
def blogs():
    posts = Blog.query.filter_by(category='blogs').order_by(Blog.created_at.desc()).all()
    return render_template('blog.html', posts=posts)

@main.route('/videos')
def videos():
    posts = Blog.query.filter_by(category='videos').order_by(Blog.created_at.desc()).all()
    return render_template('videos.html', posts=posts)

@main.route('/audios')
def audios():
    posts = Blog.query.filter_by(category='audios').order_by(Blog.created_at.desc()).all()
    return render_template('audios.html', posts=posts)

@main.route('/news')
def news():
    posts = Blog.query.filter_by(category='news').order_by(Blog.created_at.desc()).all()
    return render_template('news.html', posts=posts)

@main.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            flash('Login successful!', 'success')
            return redirect(url_for('main.admin_dashboard'))
        else:
            flash('Invalid credentials', 'danger')
    return render_template('admin_login.html')

@main.route('/admin/logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    flash('Logged out successfully.', 'info')
    return redirect(url_for('main.admin_login'))

@main.route('/admin/dashboard')
def admin_dashboard():
    if not session.get('admin_logged_in'):
        flash('You must be logged in.', 'warning')
        return redirect(url_for('main.admin_login'))
    
    posts = Blog.query.order_by(Blog.created_at.desc()).all()
    return render_template('admin_dashboard.html', posts=posts)

@main.route('/admin/add', methods=['GET', 'POST'])
def add_blog():
    if not session.get('admin_logged_in'):
        flash('Please login as admin.', 'warning')
        return redirect(url_for('main.admin_login'))

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        category = request.form['category']

        new_post = Blog(title=title, content=content, category=category)
        db.session.add(new_post)
        db.session.commit()
        flash('Blog post added!', 'success')
        return redirect(url_for('main.admin_dashboard'))

    return render_template('add_blog.html')


@main.route('/admin/edit/<int:blog_id>', methods=['GET', 'POST'])
def edit_blog(blog_id):
    if not session.get('admin_logged_in'):
        flash('Please login as admin.', 'warning')
        return redirect(url_for('main.admin_login'))

    post = Blog.query.get_or_404(blog_id)

    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        post.category = request.form['category']
        db.session.commit()
        flash('Post updated successfully!', 'success')
        return redirect(url_for('main.admin_dashboard'))

    return render_template('edit_blog.html', post=post)





@main.route('/admin/delete/<int:blog_id>', methods=['POST'])
def delete_blog(blog_id):
    if not session.get('admin_logged_in'):
        flash('Please login as admin.', 'warning')
        return redirect(url_for('main.admin_login'))

    post = Blog.query.get_or_404(blog_id)
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted successfully!', 'info')
    return redirect(url_for('main.admin_dashboard'))

@main.route('/blog/<int:blog_id>')
def view_blog(blog_id):
    post = Blog.query.get_or_404(blog_id)
    return render_template('view_blog.html', post=post)


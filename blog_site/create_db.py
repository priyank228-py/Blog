from app import create_app
from app.models import db, Blog

# Create app instance
app = create_app()

# Activate app context to use the db
with app.app_context():
    db.create_all()  # This creates the database tables
    print("✅ Database and tables created!")

    # Optional: Add dummy data if no posts exist yet
    if not Blog.query.first():
        sample_posts = [
            Blog(title="Welcome to My Blog", content="This is a blog post.", category="blogs"),
            Blog(title="Intro Video", content="This is a video post.", category="videos"),
            Blog(title="Relaxing Podcast", content="This is an audio post.", category="audios"),
            Blog(title="Today’s Headline", content="This is a news article.", category="news"),
        ]
        db.session.bulk_save_objects(sample_posts)
        db.session.commit()
        print("✅ Sample blog data inserted!")

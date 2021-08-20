from app.models import Post
from app import app, db
from app.models import User, Post


@app.shell_context_processor
def makde_shell_context():
    return {'db':db, 'User':User, 'Post':Post}
if __name__ == "__main__":
    app.run(debug=True)
from blog_app import app,db
from blog_app.models import BlogPost,User
from flask import render_template, redirect,request

from blog_app.admin import admin_con


app.register_blueprint(admin_con)

@app.route('/')
def hello():
   return render_template('index.html')


@app.route('/posts', methods=['GET', 'POST'])
def posts():
    '''
    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        author = request.form['author']
        new_post = BlogPost(
            title=post_title, content=post_content, author=author)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
        return render_template('posts.html', posts=all_posts)
    '''
    all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
    return render_template('posts.html', posts=all_posts)

@app.route('/posts/delete/<int:id>')
def delete(id):
   post = BlogPost.query.get_or_404(id)
   db.session.delete(post)
   db.session.commit()
   return redirect('/posts')


@app.route('/posts/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    post = BlogPost.query.get_or_404(id)
    if request.method == 'POST':
       post.title = request.form['title']
       post.content = request.form['content']
       post.author = request.form['author']
       db.session.commit()
       return redirect('/posts/read_more/'+str(post.id))
    
    else:
        return render_template('edit.html', post=post)

@app.route('/posts/new_post', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        author = request.form['author']
        new_post = BlogPost(
            title=post_title, content=post_content, author=author)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
        return render_template('new_post.html', posts=all_posts)
@app.route('/posts/read_more/<int:id>')
def read_more(id):
    post = BlogPost.query.get_or_404(id)
    return render_template('read_more.html',post=post)




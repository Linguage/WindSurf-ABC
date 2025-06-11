from flask import Flask, jsonify, request, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from .config import Config

# 初始化应用
app = Flask(__name__, 
            template_folder='templates',
            static_folder='static',
            static_url_path='/static')
app.config.from_object(Config)
db = SQLAlchemy(app)

# 数据库模型
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    deadline = db.Column(db.DateTime, nullable=False)
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'deadline': self.deadline.isoformat(),
            'completed': self.completed,
            'created_at': self.created_at.isoformat()
        }

# 创建数据库表
with app.app_context():
    db.create_all()

# 路由
@app.route('/')
def index():
    return render_template('index.html')

# API 路由
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = Todo.query.order_by(Todo.deadline).all()
    return jsonify([task.to_dict() for task in tasks])

@app.route('/api/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if not data or 'title' not in data or 'deadline' not in data:
        return jsonify({'error': 'Missing required fields'}), 400
    
    try:
        deadline = datetime.fromisoformat(data['deadline'].replace('Z', '+00:00'))
        task = Todo(
            title=data['title'],
            deadline=deadline,
            completed=data.get('completed', False)
        )
        db.session.add(task)
        db.session.commit()
        return jsonify(task.to_dict()), 201
    except ValueError:
        return jsonify({'error': 'Invalid date format'}), 400

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Todo.query.get_or_404(task_id)
    data = request.get_json()
    
    if 'title' in data:
        task.title = data['title']
    if 'deadline' in data:
        try:
            task.deadline = datetime.fromisoformat(data['deadline'].replace('Z', '+00:00'))
        except ValueError:
            return jsonify({'error': 'Invalid date format'}), 400
    if 'completed' in data:
        task.completed = data['completed']
    
    db.session.commit()
    return jsonify(task.to_dict())

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Todo.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)

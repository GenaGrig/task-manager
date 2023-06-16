from taskmanager import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    tasks = db.relationship(
        "Task", backref="category", cascade="all, delete", lazy=True
        )

    def __repr__(self):
        return f"Category('{self.category_name}')"


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, nullable=False, default=False)
    due_date = db.Column(db.Date, nullable=False)
    category_id = db.Column(
        db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"),
        nullable=False
        )

    def __repr__(self):
        return f"Task('{self.task_name}','{self.task_description}','{self.task_due_date}','{self.is_urgent}','{self.category_id}')"

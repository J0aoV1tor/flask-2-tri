class BaseUser(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f'<BaseUser {self.name}>'

class Admin(BaseUser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adicione mais atributos ou métodos específicos para Admin

    def has_admin_privileges(self):
        return True

class RegularUser(BaseUser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adicione mais atributos ou métodos específicos para RegularUser

    def has_admin_privileges(self):
        return False

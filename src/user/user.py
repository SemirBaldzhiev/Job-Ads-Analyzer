from hashlib import sha256
from src.dbsqlite.db_worker import save_user_db, check_password_username

class User:
    '''
    Class for creating and managing users
    '''
    
    def __init__(self, first_name, last_name, username, email, password, skills) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = sha256(password.encode()).hexdigest()
        self.skills = skills
        
    
    @staticmethod
    def valid_credentials(username, password) -> bool:
        '''
        Method for user login
        '''
        if check_password_username(username, sha256(password.encode()).hexdigest()):
            return True
        return False
    
    def change_password(self, old_password, new_password) -> bool:
        '''
        Method for changing user password
        '''
        if self.password == sha256(old_password.encode()).hexdigest():
            self.password = sha256(new_password.encode()).hexdigest()
            return True
        return False

    
    def save(self) -> None:
        '''
        Method for saving user to the database
        '''
        save_user_db((self.first_name, self.last_name, self.username, self.email, self.password, self.skills))
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} <{self.email}>'
    
    def __repr__(self) -> str:
        return f'User({self.first_name}, {self.last_name}, {self.username}, {self.email}, {self.password})'
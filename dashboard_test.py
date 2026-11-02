password = "admin123"
api_key = "key-abc-123"

def login(username):
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    cursor.execute(query)

def hash_password(pw):
    return hashlib.md5(pw.encode()).hexdigest()

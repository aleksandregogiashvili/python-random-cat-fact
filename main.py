import requests
import json
import sqlite3

api_url = 'https://catfact.ninja/fact'
response = requests.get(api_url)

data = response.json()
# print(data)

# print(f"Status code: {response.status_code}")

with open("catfact.json", "w") as cats:
    json.dump(data, cats, indent= 4)

with open("catfact.json", "r") as cats:
    cat_data = json.load(cats)

fact = data.get('fact')
print(f"Random fact: {fact}")
length = data.get('length')
print(f"Length: {length}")

conn = sqlite3.connect('cat_facts.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS cat_facts (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	fact TEXT,
	length INTEGER
)
''')

cursor.execute('''
INSERT INTO cat_facts (fact, length) VALUES (?, ?)
''', (fact, length))

conn.commit()
conn.close()



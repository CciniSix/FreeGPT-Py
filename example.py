import requests
import json

fulltext = ""
while True:
    mess = input("Your Message: ")
    with requests.post("http://127.0.0.1:8000/v1/chat/completions", params={"message": mess}, stream=True) as session:
        for chunk in session.iter_lines():
            line = chunk.decode("utf-8")
            if line == "[DONE]": break
            else: data = json.loads(line)
            try:
                fulltext = data["choices"][0]["message"]["content"]
            except Exception as e:
                pass
    print(fulltext+"\n")
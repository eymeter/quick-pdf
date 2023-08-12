import requests

key = "sec_MCrZJrSCdUjCqwIRFEjX8nvrO1wJGoXi"
site = "https://api.chatpdf.com/v1"
pdf = "https://dev-eym.me/summarize.pdf"
started = True

def chat():
  headers = {"x-api-key": key}
  response = requests.post(f"{site}/sources/add-url",
                                   headers=headers,
                                   json={"url": pdf})
  response_data = response.json()
  source_id = response_data["sourceId"]

  while started:
    user = input("+ ")
    chat_response = requests.post(f"{site}/chats/message",
                                  headers=headers,
                                  json={
                                    "sourceId":
                                    source_id,
                                    "messages": [{
                                      "role": "user",
                                      "content": user
                                    }]
                                  })
    chat_data = chat_response.json()
    print(f"- {chat_data['content']}")

def main():
  chat()


if __name__ == "__main__":
  main()

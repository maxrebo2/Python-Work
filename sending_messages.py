messages = ["Hello World", "Guten Tag", "Where's my dingus", "What's up dog"]
sent_messages = []


def send_messages():
	while messages:
		sending_message = messages.pop()
		print(f"Sending Message: {sending_message}")
		sent_messages.append(sending_message)
		print("Message has been sent")

def show_sent_messages():
		print(sent_messages)
		print("All your messages have been sent.")
		
send_messages()
show_sent_messages()

print(messages)
print(sent_messages)
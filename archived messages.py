def show_messages(messages):
	print("showin all messages:")
	for message in messages:
		print(message)


def send_message(messages, sent_messages):
	print("\nSending all messages:")
	while messages:
		current_message = messages.pop()
		print(current_message)
		sent_messages.append(current_message)


messages = ["hello there", "how are u?", ":)"]
show_messages(messages)

sent_messages = []
send_message(messages[:], sent_messages)


print("\nFinal lists:")
print(messages)
print(sent_messages)
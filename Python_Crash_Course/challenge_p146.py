message = ['Hello, how are you?', 'Have a nice day!', 'What is your dna cell stem?', 'How you doing?']
sent_messages = []


def show_messages(values):
    print("\nFollowing messages are in the list.")
    for show_message in values:
        print(f"\t{show_message}")


def send_messages(messages, send_to):
    print(f"\n message -> sent message")
    while messages:
        removed_message = messages.pop()
        print(f"\tMessage sent. {removed_message}")
        sent_messages.append(removed_message)

    print("\nFollowing messages are send off.")
    for sended in sent_messages:
        print(f"\t{sended}")

    return show_messages(send_to)


send_messages(message[:], sent_messages)



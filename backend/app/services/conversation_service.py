from collections import defaultdict

# conversation_id -> messages
_conversations = defaultdict(list)


def add_message(conversation_id: str, role: str, content: str):
    _conversations[conversation_id].append(
        {
            "role": role,
            "content": content,
        }
    )


def get_history(conversation_id: str):
    return _conversations[conversation_id]


def clear_conversation(conversation_id: str):
    _conversations.pop(conversation_id, None)
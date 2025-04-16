
from utils import get_nested_value
def parse_json(data):
    snippet = get_nested_value(data, 'data.node.bot_response_message.snippet')
    return snippet
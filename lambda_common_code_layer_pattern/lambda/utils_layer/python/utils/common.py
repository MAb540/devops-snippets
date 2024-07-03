from typing import Any


def event_processor(event: Any):
    print("event from common utils: ",event)
    object_name = event.get('detail').get('object').get('key')
    return object_name


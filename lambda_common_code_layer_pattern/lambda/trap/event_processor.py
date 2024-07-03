from typing import Any


def event_processor(event: Any):
    print("event: ",event)
    object_name = event.get('detail').get('object').get('key')
    return object_name


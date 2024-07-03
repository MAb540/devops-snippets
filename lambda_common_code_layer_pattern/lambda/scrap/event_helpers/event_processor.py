from typing import Any

event = {
    "version": "0",
    "id": "2f8310a4-dcb2-4da5-2745-75a54cd62865",
    "detail-type": "Object Created",
    "source": "aws.s3",
    "account": "485686783262",
    "time": "2024-06-26T13:38:15Z",
    "region": "us-east-1",
    "resources": ["arn:aws:s3:::test-54-buck-tech"],
    "detail": {
        "version": "0",
        "bucket": {"name": "test-54-buck-tech"},
        "object": {
            "key": "test/cheatSheet.jpg",
            "size": 162144,
            "etag": "1ba6971944d06c6962d174b42a9c2a29",
            "sequencer": "00667C19C7482616BE",
        },
        "request-id": "EZZG4J110R734WH5",
        "requester": "485686783262",
        "source-ip-address": "223.123.104.160",
        "reason": "PutObject",
    },
}

def event_processor(event: Any):
    print("event: ",event)
    object_name = event.get('detail').get('object').get('key')
    return object_name


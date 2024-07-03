
# from event_processor import event_processor



from utils.common import event_processor

def handler(event, _context):

    print("trap handler invoked")

    object_name = event_processor(event)
    print("object_name: ",object_name)

    return {
        "status":"200"
    }
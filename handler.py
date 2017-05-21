import sys
import os
sys.path.insert(0, './lib')
import pydash
import notify_slack
import receive_events

# FIXME: make this a database lookup rather than being hardcoded
whitelist = set([])

def sentry(event, context):
    problems = receive_events.check_bucket_creation(event, whitelist)
    for problem in problems:
        notify_slack.bad_things(
            problem["error_title"],
            problem["error_body"],
            os.getenv("WEBHOOK_URL")
        )

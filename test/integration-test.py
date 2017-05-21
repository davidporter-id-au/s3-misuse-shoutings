import os
import sys
sys.path.append(os.path.abspath(__file__ + "/../.."))
import receive_events
import handler

import sample_events

handler.sentry(sample_events.bucket_being_made_public_to_the_world, {})

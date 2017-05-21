import sys
sys.path.insert(0, './lib')
import json
import requests

def bad_things_payload(heading, details_string):
    return json.dumps({
        "attachments": [
            {
                "fallback": details_string,
                "color": "#F00",
                "author_name": "A angry bot",
                "author_link": "https://github.com/davidporter-id-au/s3-misuse-shoutings",
                "title": heading,
                "fields": [
                    {
                        "value": details_string,
                        "short": False
                    }
                ]
            }
        ]
    })

def bad_things(heading, details_string, url):
    payload = bad_things_payload(heading, details_string)
    result = requests.post(url, payload)
    if result.status_code != 200:
        raise Exception("An error occured attempting to notify slack, Status code:",
              result.status_code,
              "Response:",
              result.text
        )

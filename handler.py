import sys
sys.path.insert(0, './lib')
import pydash

get = pydash.objects.get

def check_bucket_creation_for_problems(ev):
    problems = []
    bucket_grants = get(ev, "detail.requestParameters.AccessControlPolicy.AccessControlList.Grant")

    for grant in bucket_grants:
        if get(grant, "Grantee.URI") == "http://acs.amazonaws.com/groups/global/AllUsers":
            problems.append({
                "bucket_name": get(ev, "detail.requestParameters.bucketName"),
                "person_responsible": get(ev, "detail.userIdentity.principalId"),
                "region": get(ev, "detail.awsRegion"),
                "account": get(ev, "account"),
                "bucket_grants": get(ev, "detail.requestParameters.AccessControlPolicy.AccessControlList.Grant"),
                "error": "All users flagged in bucket policy",
                "debug": grant
            })

    return problems

def sentry(event, context):
    problems = check_bucket_creation_for_problems(event)
    if problems:
        print(problems)

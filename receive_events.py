import sys
sys.path.insert(0, './lib')
import pydash

get = pydash.objects.get

# a stupidly simple example check: Does this bucket
# contain permissions for "All users or All Authenticated users?"
def check_bucket_creation(ev, whitelist):
    problems = []
    bucket_name = get(ev, "detail.requestParameters.bucketName")
    bucket_grants = get(ev, "detail.requestParameters.AccessControlPolicy.AccessControlList.Grant")

    if bucket_name in whitelist:
        return

    if not bucket_grants:
        return

    for grant in bucket_grants:

        person_responsible = get(ev, "detail.userIdentity.principalId")
        region = get(ev, "detail.awsRegion")
        aws_account = get(ev, "account")

        if (get(grant, "Grantee.URI") == "http://acs.amazonaws.com/groups/global/AllUsers"):
            problems.append({
                "bucket_name": bucket_name,
                "person_responsible": person_responsible,
                "region": region,
                "account": aws_account,
                "error": "Bucket is open for all users",
                "error_title": "Security warning for s3 bucket: " + bucket_name,
                "error_body": open_bucket_report_string(
                    person_responsible,
                    aws_account,
                    region,
                    bucket_name
                )
            })

        if(get(grant, "Grantee.URI") == "http://acs.amazonaws.com/groups/global/AuthenticatedUsers"):
            problems.append({
                "bucket_name": bucket_name,
                "person_responsible": person_responsible,
                "region": region,
                "account": aws_account,
                "error": "A Bucket is open to all authenticated users",
                "error_title": "Security warning for s3 bucket: " + bucket_name,
                "error_body": open_bucket_report_string(
                    person_responsible,
                    aws_account,
                    region,
                    bucket_name
                )
            })
    return problems

def open_bucket_report_string(person_responsible, account, region, bucket_name):
        return (
            "This bucket has been created whose ACL represents a security risk."
            + "\n\n"
            + "\nWho?: " + person_responsible
            + "\nBucket: " + bucket_name
            + "\nAccount: " + account
            + "\nRegion : " + region
            + "\n\nEither:"
            +" \n - Remove permissions giving access to 'Everyone'\'Authenticated users'"
            + "\n - or whitelist this bucket"
        )


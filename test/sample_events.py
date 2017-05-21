
bucket_being_made_public_to_the_world = {
  "detail": {
    "eventType": "AwsApiCall",
    "eventID": "some-id",
    "requestID": "some-id",
    "requestParameters": {
      "acl": [
        ""
      ],
      "AccessControlPolicy": {
        "Owner": {
          "ID": "some-guid",
          "DisplayName": "aws_account"
        },
        "xmlns": "http:\/\/s3.amazonaws.com\/doc\/2006-03-01\/",
        "AccessControlList": {
          "Grant": [
            {
              "Permission": "FULL_CONTROL",
              "Grantee": {
                "ID": "some-guid",
                "xmlns:xsi": "http:\/\/www.w3.org\/2001\/XMLSchema-instance",
                "DisplayName": "some-account",
                "xsi:type": "CanonicalUser"
              }
            },
            {
              "Permission": "READ",
              "Grantee": {
                "URI": "http://acs.amazonaws.com/groups/global/AllUsers",
                "xmlns:xsi": "http:\/\/www.w3.org\/2001\/XMLSchema-instance",
                "xsi:type": "Group"
              }
            }
          ]
        }
      },
      "bucketName": "some-bucket-name"
    },
    "userAgent": "[aws-internal\/3, S3Console\/0.4]",
    "sourceIPAddress": "AWS Internal",
    "awsRegion": "ap-southeast-2",
    "eventName": "PutBucketAcl",
    "eventSource": "s3.amazonaws.com",
    "eventTime": "2017-05-19T14:11:28Z",
    "userIdentity": {
      "sessionContext": {
        "sessionIssuer": {
          "userName": "some-session",
          "accountId": "some-account-id",
          "arn": "arn:aws:iam::accountid:role\/role",
          "principalId": "some-principal-id",
          "type": "Role"
        },
        "attributes": {
          "creationDate": "2017-05-19T12:43:02Z",
          "mfaAuthenticated": "false"
        }
      },
      "accountId": "some-account-id",
      "arn": "arn:aws:sts::account-id:assumed-role\/group\/user@domain.org",
      "principalId": "some-principal:user@domain.org",
      "type": "AssumedRole"
    },
    "eventVersion": "1.04"
  },
  "resources": [],
  "region": "ap-southeast-2",
  "time": "2017-05-19T14:11:28Z",
  "account": "some-account-id",
  "source": "aws.s3",
  "detail-type": "AWS API Call via CloudTrail",
  "id": "some-guid",
  "version": "0"
}

bucket_is_cool = {
  "detail": {
    "eventtype": "awsapicall",
    "requestparameters": {
      "bucketname": "bucket1",
      "createbucketconfiguration": {
        "xmlns": "http://s3.amazonaws.com/doc/2006-03-01/",
        "locationconstraint": "ap-southeast-2"
      }
    },
    "useragent": "[aws-internal/3, s3console/0.4]",
    "sourceipaddress": "aws internal",
    "awsregion": "ap-southeast-2",
    "eventname": "createbucket",
    "eventsource": "s3.amazonaws.com",
    "eventtime": "2017-05-20t16:19:50z",
    "useridentity": {
      "sessioncontext": {
        "sessionissuer": {
          "username": "some-role",
          "accountid": "some-account-id",
          "arn": "arn:aws:iam::some-account-id:role/some-role",
          "principalid": "some-principal-id",
          "type": "role"
        },
        "attributes": {
          "creationdate": "2017-05-20t13:45:22z",
          "mfaauthenticated": "false"
        }
      },
      "accountid": "some-account-id",
      "arn": "arn:aws:sts::some-account-id:assumed-role/some-role/user@domain.test",
      "principalid": "some-principal-id:user@domain.test",
      "type": "assumedrole"
    },
    "eventversion": "1.04"
  },
  "resources": [],
  "region": "ap-southeast-2",
  "time": "2017-05-20t16:19:50z",
  "account": "some-account-id",
  "source": "aws.s3",
  "detail-type": "aws api call via cloudtrail",
  "id": "some-guid",
  "version": "0"
}

_clearly we all need yet another slack message to solve problems_
-- nobody ever

## S3 Misuse shouty-bot 

(not even a real bot, just spams your slack channels)

This is a spike to use [AWS cloudwatch event rules](http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html) to prevent users from making silly security mistakes such as leaving their aws s3 buckets wide open to the world. It's a spike only and ought to be slightly modified for a multi-account environment setup.

#### what does it do? 

It's triggered by cloudtrail events, firing when "CreateBucket" or "PutBucketAcl" events are detected.

It scans bucket creation and ACL modification events for bad behaviour. If detected, it presently notifies slack, but it could just as easily trigger pagerduty or something similar. 

#### What does it check for? 

This version only looks for bucket-level permissions being granted to either 'all users' or 'authenticated users', neither of which are appropriate without good reason.

#### What if I have a good reason?

There's a whitelist for the bot

#### Is this doing the same thing as ...?

Probably, there's almost certainly real products covering this use-case. This is some shitty glue-code for demonstration only.

#### What about permissions of items within a bucket?

It would probably be infeasible to monitor item-level permissions within a bucket. This doesn't attempt to. It's an attempt at helping users, not a cover-all-problems solution.

### Requirements:

- nodeJS some reasonably up to date version
- [serverless](https://serverless.com)
- python3

### to deploy:

```
export WEBHOOK_URL=<some slack integration url>
sls deploy
```

### Interesting bits

Nearly all of the python is utterly disinteresting glue. The only interesting bit is the cloudformation for the cloudwatch events in `serverless.yml` which specify the events to watch for.

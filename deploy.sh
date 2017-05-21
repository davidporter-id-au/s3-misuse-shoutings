#!/bin/bash -eu

cd $(dirname $0)

if [[ -z "$(which sls)" ]]; then
    echo "This project has an implicit dependency on the Serverless framework:"
    echo "install nodeJS and then install https://serverless.com/:"
    exit 1
fi

sls deploy

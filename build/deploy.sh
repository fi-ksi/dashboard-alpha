#!/bin/bash

export LC_ALL=C.UTF-8

echo -e "Content-type: text/html\n"

OUTPUT+=$(cd .. && ./kleobis-deploy.sh 2>&1)$'\n\n'
echo "$OUTPUT" | mail "me@apophis.cz" -s "[ksi-monitoring] Deploy status"

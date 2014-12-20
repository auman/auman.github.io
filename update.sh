#!/bin/sh
git add .  && python ./gen.py > ./index.html && git commit -m 'generic update new proofs' -a && git push origin master


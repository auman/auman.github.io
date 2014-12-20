#!/bin/sh
python ./gen.py > ./index.html && git add . && git commit -m 'generic update new proofs' -a && git push origin master


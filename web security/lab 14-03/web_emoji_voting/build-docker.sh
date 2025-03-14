#!/bin/bash
docker build --tag=web_emoji_voting .
docker run -d -p 5203:1337 --rm --name=web_emoji_voting -it web_emoji_voting

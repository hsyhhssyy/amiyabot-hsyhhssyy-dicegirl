#!/bin/sh

zip -q -r amiyabot-hsyhhssyy-dicegirl-1.0.zip *
rm -rf ../../amiya-bot-v6/plugins/amiyabot-hsyhhssyy-dicegirl-1_0
mv amiyabot-hsyhhssyy-dicegirl-1.0.zip ../../amiya-bot-v6/plugins/
docker restart amiya-bot 
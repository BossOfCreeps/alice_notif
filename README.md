python3 manage.py runsslserver 0.0.0.0:443 --certificate fullchain.pem --key privkey.pem

py .\manage.py dumpdata --exclude contenttypes.contenttype --exclude auth.permission > fix.json

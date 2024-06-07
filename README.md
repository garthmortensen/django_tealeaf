# tealeafdjangoproj

[![Django CI](https://github.com/garthmortensen/django_tealeaf/actions/workflows/django-tests.yml/badge.svg)](https://github.com/garthmortensen/django_tealeaf/actions/workflows/django-tests.yml)

[![codecov](https://codecov.io/gh/garthmortensen/django_tealeaf/branch/main/graph/badge.svg)](https://codecov.io/gh/garthmortensen/django_tealeaf)

This is a rebuild of tealeaf using django as backend, in order to reduce future maintenance cost.

Check history.log for details, but it uses `venv`, `docker` (podman), `django`.

Tree just wanted files:
```bash
tree -I '__pycache__|venv|.git|db.sqlite3|static|media|node_modules'
```

http://127.0.0.1:8000/category/food/

backup db sometimes:
cp ~/develop/django_tealeaf/db.sqlite3 ~/develop/django_tealeaf/db_backup_$(date +%Y%m%d).sqlite3


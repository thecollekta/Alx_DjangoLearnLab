# library_management_system/__init__.py

# Import PyMySQL as MySQL
import pymysql
pymysql.install_as_MySQLdb()

# Import Celery
from .celery import app as celery_app

__all__ = ("celery_app",)
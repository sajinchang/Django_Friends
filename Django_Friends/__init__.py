import pymysql
pymysql.install_as_MySQLdb()

from libs.orm import patch_model

patch_model()


# http://zetcode.com/db/sqlalchemy/orm/
from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

params = quote_plus("DRIVER={SQL Server};SERVER=NASQLDB7\SQLDB7;DATABASE=Budget_Glick;Trusted_Connection=yes;")
eng = create_engine("mssql+pyodbc:///?odbc_connect=" + params)

Base = declarative_base()
Base.metadata.bind = eng

class PackageConfig(Base):

    __tablename__ = "package_config"

    config_id = Column(Integer, primary_key=True)
    config_name = Column(String)
    config_value = Column(String)

Session = sessionmaker(bind=eng)
ses = Session()

rs = ses.query(PackageConfig).filter(PackageConfig.config_id.in_([1, 2, 3,4 , 5]))

for p in rs:
    print(p.config_name)


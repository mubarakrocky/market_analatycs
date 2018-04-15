from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Boolean, Date, Float
from sqlalchemy.orm import relationship
from db_connection import Base


class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    sector_id = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class ListedCompany(Base):
    __tablename__ = 'listed_companies'
    id = Column(Integer, primary_key=True)
    symbol = Column(String)
    exchange = Column(Integer)
    company_id = Column(Integer, ForeignKey('companies.id'))
    company = relationship("Company")
    external_reference = Column(String)
    active = Column(Boolean)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

class CompanyHistory(Base):
    __tablename__ = 'company_histories'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    value = Column(Float(precision=2))
    listed_company_id = Column(Integer, ForeignKey('listed_companies.id'))
    listed_company = relationship("ListedCompany")
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    volume = Column(String)
    
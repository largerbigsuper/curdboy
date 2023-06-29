
import datetime
from sqlalchemy import Boolean, Column, Integer, String, DateTime
from database.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(150), unique=True, index=True, comment="账号名")
    nickname = Column(String(150), nullable=True, comment="昵称")
    gender = Column(String(150), nullable=True, comment="性别")
    avatar = Column(String(150), nullable=True, comment="头像")
    email = Column(String(50), nullable=True, unique=True, index=True, comment="邮箱")
    password = Column(String(100), comment="密码")
    is_superuser = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    created_by = Column(Integer, comment="创建人")
    created_time = Column(DateTime(timezone=True), default=datetime.datetime.utcnow, comment="创建时间")
    updated_by = Column(Integer, comment="更新人")
    updated_time = Column(DateTime(timezone=True), default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow, comment="更新时间")
    last_login = Column(DateTime, comment="最后登录时间")
    

class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), unique=True, index=True, comment="名称")
    avatar = Column(String(150), nullable=True, comment="头像")
    sort = Column(Integer, default=99, comment="排序")
    created_by = Column(Integer, comment="创建人")
    created_time = Column(DateTime(timezone=True), default=datetime.datetime.utcnow, comment="创建时间")
    updated_by = Column(Integer, comment="更新人")
    updated_time = Column(DateTime(timezone=True), default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow, comment="更新时间")
    is_active = Column(Boolean, default=True)


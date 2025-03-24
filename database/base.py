import datetime
from typing import Optional

from sqlalchemy import ForeignKey, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from database.session import Model


# from db.session import Model



class Lvl(Model):
    __tablename__ = "lvl"

    id: Mapped[int] = mapped_column(primary_key=True)
    level: Mapped[int] = mapped_column(default=0)
    cotel: Mapped[float] = mapped_column(default=0)
    count_user: Mapped[int] = mapped_column(default=0)
    # session_id: Mapped[Optional[int]] = mapped_column(ForeignKey("session.id"))
    # session: Mapped["Session"] = relationship("Session", back_populates="lvls")
    users: Mapped[list["UserOrm"]] = relationship("UserOrm", back_populates="lvl", cascade="save-update, delete")
    status: Mapped[Optional[str]] = mapped_column() #need pay #always pay # pay


# class Session(Model):
#     __tablename__ = "session"
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     count_user: Mapped[int] = mapped_column()
#     lvls: Mapped[list["Lvl"]] = relationship("Lvl", back_populates="session")


# class users_token(Model):
#     __tablename__ = "users_token"
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     tg_id: Mapped[str] = mapped_column(unique=True)
#     name: Mapped[str] = mapped_column()
#
#     # Связь один-к-одному с таблицей UserOrm
#     user: Mapped["UserOrm"] = relationship("UserOrm", back_populates="token", uselist=False)


class UserOrm(Model):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    balance: Mapped[float] = mapped_column()
    gifter: Mapped[bool] = mapped_column(default=False)
    pay_time: Mapped[Optional[datetime.datetime]] = mapped_column(nullable=True)
    paid_status: Mapped[str] = mapped_column(default='need pay') #need pay, pay, wait pay
    lvl_id: Mapped[Optional[int]] = mapped_column(ForeignKey("lvl.id"), nullable=True)
    lvl: Mapped["Lvl"] = relationship("Lvl", back_populates="users")
    level_user: Mapped[Optional[int]] = mapped_column(default=1, nullable=True)

    # Внешний ключ для связи с users_token
    tg_id: Mapped[Optional[str]] = mapped_column(unique=True, nullable=False)

    # Связь один-к-одному с таблицей users_token
    # token: Mapped["users_token"] = relationship("users_token", back_populates="user", uselist=False)

    referal_id: Mapped[Optional[int]] = mapped_column(ForeignKey("user.id"), nullable=True)

    # Связь один-ко-многим с самим собой для рефералов
    referrer: Mapped["UserOrm"] = relationship("UserOrm", remote_side=[id], back_populates="referrals")
    referrals: Mapped[list["UserOrm"]] = relationship("UserOrm", back_populates="referrer")
    referal_promo: Mapped[Optional[str]] = mapped_column(nullable=True, unique=True)


class Transaction(Model):
    __tablename__ = "trans"
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column()  # trans_balance, trans_cotel, trans_end_game, trans_ref, trans_withdrawal
    amount: Mapped[float] = mapped_column()
    trans_time: Mapped[datetime.datetime] = mapped_column(server_default=func.now())


class Curse(Model):
    __tablename__ = "curse"
    id: Mapped[int] = mapped_column(primary_key=True)
    rubles: Mapped[float] = mapped_column()
    usd: Mapped[float] = mapped_column()
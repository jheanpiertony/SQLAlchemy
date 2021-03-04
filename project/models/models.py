from datetime import datetime

from sqlalchemy import\
    Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class SongModel(Base):

    __tablename__ = 'songs'

    def __init__(self,
                 name: str,
                 state: bool = True):
        self.name = name
        self.state = state

    id = Column(Integer, primary_key=True)
    name = Column(String)
    state = Column(Boolean)
    id_album = Column(Integer, ForeignKey('albums.id'), primary_key=True)


class AlbumModel(Base):

    __tablename__ = 'albums'

    def __init__(self,
                 name: str,
                 state: bool = True,
                 songs: list[SongModel] = None):
        self.name = name
        self.state = state
        if songs is not None and len(songs) > 0:
            self.songs.extend(songs)

    id = Column(Integer, primary_key=True)
    name = Column(String)
    state = Column(Boolean)
    id_musician = Column(Integer, ForeignKey('musicians.id'), primary_key=True)
    songs = relationship("SongModel")


class MusicianModel(Base):

    __tablename__ = 'musicians'

    def __init__(self,
                 name: str,
                 state: bool = True,
                 albums: list[AlbumModel] = None):
        self.name = name
        self.state = state
        if albums is not None and len(albums) > 0:
            self.albums.extend(albums)

    id = Column(Integer, primary_key=True)
    name = Column(String)
    state = Column(Boolean)
    albums = relationship("AlbumModel")


class LogModel(Base):

    __tablename__ = 'logs'

    def __init__(self,
                 message: str,
                 level: str,
                 date_stamp: datetime):
        self.message = message
        self.level = level
        self.date_stamp = date_stamp

    id = Column(Integer, primary_key=True)
    message = Column(String)
    level = Column(String)
    date_stamp = Column(DateTime)

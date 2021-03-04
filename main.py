from project.configuration_manager import ConfigurationManager
from project.infrastructure.contexts.postgre_sql_context import\
    PostgreSqlContext
from project.infrastructure.repositories.album_repository import\
    AlbumRepository
from project.infrastructure.repositories.musician_repository import\
    MusicianRepository
from project.infrastructure.repositories.song_repository import\
    SongRepository
from project.logs.system_log import SystemLog
from project.models.models import AlbumModel, MusicianModel, SongModel


database_connection_name = "DATABASE_POSTGRES_41"
database_api = "pg8000"
database_context = PostgreSqlContext(
    database_connection_name,
    database_api)

database_session = database_context.get_session()


system_log = SystemLog(database_session)


def get_app_name():
    app_name = "Unknown"
    try:
        app_name = ConfigurationManager.get_config("APP_NAME")

    except Exception as error:
        system_log.add(
            message=str(error))

    return app_name


app_name = get_app_name()
print(app_name)


try:
    musician_repository = MusicianRepository(database_session)
    album_repository = AlbumRepository(database_session)
    song_repository = SongRepository(database_session)

except SystemError as error:
    system_log.add(
        message=str(error))

musician_name = "ABD"

musician = MusicianModel(musician_name)

musician_repository.add(musician)

album_a = AlbumModel(
    name=f"Album A de {musician_name}")
album_b = AlbumModel(
    name=f"Album B de {musician_name}")

musician.albums.extend([album_a, album_b])

song_1 = SongModel(f"Song 1 Album A de {musician_name}")
song_2 = SongModel(f"Song 2 Album A de {musician_name}")
song_3 = SongModel(f"Song 3 Album B de {musician_name}")
song_4 = SongModel(f"Song 4 Album B de {musician_name}")

album_a.songs.extend([song_1, song_2])
album_b.songs.extend([song_3, song_4])

database_session.commit()

musician_to_delete = musician_repository.get_by_id(musician.id)

musician_repository.delete(musician_to_delete)

database_session.commit()

musicians = musician_repository.get()

for musician in musicians:
    print(musician.id)

print("The end")

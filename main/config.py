import os

basedir = os.path.abspath(os.path.dirname(__file__))
basedir_not_main = os.path.abspath(os.path.dirname(__file__))[:-5]

class base_config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'mcs9#dvqn(pl7y28kuz640_20b0t%30==3121!&beefel$rq^z')

    POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'localhost')
    POSTGRES_PORT = os.environ.get('POSTGRES_PORT', 5432)
    POSTGRES_USER = os.environ.get('POSTGRES_USER', 'igor')
    POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'vrqegtq4r23ewqs')
    POSTGRES_DB = os.environ.get('POSTGRES_DB', 'ishelkydb')

    SQLALCHEMY_DATABASE_URI = 'postgresql://%s:%s@%s:%s/%s' % (
        POSTGRES_USER,
        POSTGRES_PASSWORD,
        POSTGRES_HOST,
        POSTGRES_PORT,
        POSTGRES_DB
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

#    DEBUG=False
    """Default configuration options."""
    SITE_NAME = os.environ.get('APP_NAME', 'ishelky')


    # CKEDITOR_SERVE_LOCAL = True
    # CKEDITOR_HEIGHT = 400
    # CKEDITOR_FILE_UPLOADER = 'upload'
    # # CKEDITOR_ENABLE_CSRF = True  # if you want to enable CSRF protect, uncomment this line
    # UPLOADED_PATH = os.path.join(basedir_not_main, 'uploads')
    # print(UPLOADED_PATH)
    #
    # THUMBNAIL_MEDIA_ROOT =basedir_not_main+'/uploads'
    # THUMBNAIL_MEDIA_URL = '/uploads/'
    # THUMBNAIL_MEDIA_THUMBNAIL_ROOT= basedir_not_main+'/uploads/media/THUMBNAIL'
    # THUMBNAIL_MEDIA_THUMBNAIL_URL= '/uploads/media/THUMBNAIL/'
    # THUMBNAIL_STORAGE_BACKEND= 'flask_thumbnails.storage_backends.FilesystemStorageBackend'
    # THUMBNAIL_DEFAUL_FORMAT='JPEG'
    #
    #
    #
    # MAIL_SERVER = os.environ.get('MAIL_SERVER', 'mail')
    # MAIL_PORT = os.environ.get('MAIL_PORT', 1025)
    #
    # PAGIN_PAGE = 3
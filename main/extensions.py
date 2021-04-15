from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_ckeditor import CKEditor
from flask_thumbnails import Thumbnail


# урезать количество запросов к странице
limiter = Limiter(key_func=get_remote_address)
# работа с логином и паролем
lm = LoginManager()
mail = Mail()
migrate = Migrate()
ck_editor=CKEditor()
thum=Thumbnail()

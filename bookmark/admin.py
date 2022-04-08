# db에 접근할 때 관리자로 접속할 수 있도록 도와주는 파일
from django.contrib import admin

from bookmark.models import Bookmark

admin.site.register(Bookmark)  # import를 안했을 때는 오류가 난다.

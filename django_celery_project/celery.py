from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings

# 내가 생성한 셀러리 셋팅이 적용된 장고 setting 파일정보를 입력한다.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_project.settings')

# 셀러리 앱(일종의 백그라운드 비동기 프레임워크)을 생성한다. 앱의 이름을 지정한다.(임의의 이름이라도 상관 없을듯)
app = Celery('django_celery_project')

# 셀러리에서 utc 타임존 사용여부 설정인듯
app.conf.enable_utc = False

# 타임존을 한국시간으로 설정, settings.py의 CELERY_TIMEZONE와 중복되는 셋팅인듯 보인다. 없어도 될듯???
app.conf.update(timezone='Asia/Seoul')

# 접두어 CELERY로 시작하는 setting 정보들을 읽어와서(settings.py에서) 셋팅한다는 것 같다.
app.config_from_object(settings, namespace='CELERY')

# Celary는 비동기 테스크를 동작시크는 일종의 프레임 워크(테스트 요청->브로커->워커(비동기로 테스트실행)->result backend(결과)
# beat는 Celary에 확장 모듈같은 느낌으로 비동기 테스크를 스케쥴링으로 동작 시킨다.

# Celery Beat Settings
app.conf.beat_schedule = {

}

app.autodiscover_tasks()  # 등록된 장고 앱 설정에서 task를  불러온다. 테스크 데코레이션이 붙은 것들을 스케닝 하는듯


# 프로젝트에 등록된 앱에서 shared_task 데코레이션을 스캐닝 하는듯 하다.


# 디버깅용 공통 테스크?
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

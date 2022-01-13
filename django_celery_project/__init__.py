from .celery import app as celery_app
# 설정한 셀러리앱을 인스턴스화 한다.
__all__ = ('celery_app',)  # __all__은 공개살 패키지를 지정한다.

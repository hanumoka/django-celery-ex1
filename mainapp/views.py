from django.http import HttpResponse
from django.shortcuts import render
from .tasks import test_func


# Create your views here.
def test(request):
    '''http 요청을 받으면 테스트 태스크를 비동기로 실행 시킨다?'''
    # 태스크 실행, delay라는 메소드는 실행 메소드
    test_func.delay()
    return HttpResponse("Done")

from celery import shared_task


@shared_task(bind=True)
def test_func(self):
    '''테스트 테스크'''
    # operation
    for i in range(10):
        print(i)
    return "Done"

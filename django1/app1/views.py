from django.shortcuts import render
from app1.models import Worker


def index_page(request):

    new_worker = Worker(name='Иван', second_name='Закорюкин', salary=70000)
    new_worker.save()

    all_workers = Worker.objects.all()  # чтение всех записей
    print(all_workers)

    workers_filtered = Worker.objects.filter(salary=100000)  # чтение записей по фильтру
    print(workers_filtered)

    for i in all_workers:
        print(f'Фамилия: {i.second_name}, Имя: {i.name}, Зарплата: {i.salary}, ID: {i.id}')

    return render(request, 'index.html')

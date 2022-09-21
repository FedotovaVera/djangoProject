
    """
#вытащить из таблицы
def main(request): #вытащить из таблицы
    context = {'fromdb': Maine.objects.all()[0].position}
    return render(request, 'addtask.html', context=context)


    #занести в таблицу
    ex = Maine()
    ex.user = '100pir'
    ex.position = 'something'
    ex.birth_date = '15-06-1991'
    ex.save()
    return render(request, 'addtask.html')
"""
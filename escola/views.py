from django.http import JsonResponse

# só criaremos a API

def estudantes(request):
    if request.method == 'GET':
        estudante = {
            'id':'1',
            'nome':'Joao'
        }
        return JsonResponse(estudante)
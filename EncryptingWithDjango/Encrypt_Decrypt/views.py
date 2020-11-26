from django.shortcuts import render
from django.http import HttpResponse
import onetimepad
import random
# Create your views here.
# encrypt and decrypt text
def encrypted(request):
    params={}
    if 'Generate' in request.POST:
        generate = onetimepad.encrypt(request.POST['encrypt'],'random')
        # convert(generate)
        params['key'] = generate
    elif 'Convert' in request.POST:
        convert = onetimepad.decrypt(request.POST['decrypt'],'random')
        params['new'] = convert
    return render(request,'Encrypting_Decrypting.html',params)
from django.shortcuts import render
from django.http import HttpResponse
# 실질 코드 작성
# Create your views here.
# request는 인수로 항상 작성
# view에 작성하고 url에 추가
def calculator(request):
    # return  HttpResponse('start') 직접값을 응답
    num1=request.GET.get('num1')
    num2=request.GET.get('num2')
    operators=request.GET.get('operators')
    #calculate
    result=0
    if operators=='+':
        result=int(num1)+int(num2)
    elif  operators=='-':
        result=int(num1)-int(num2)
    elif  operators=='*':
        result=int(num1)*int(num2)
    elif  operators=='/':
        result=int(num1)/int(num2)
    #response
    return render(request,'calculator.html',{'result':result}) #templates 를 경유해서 응답 (html을 응답할때 사용)

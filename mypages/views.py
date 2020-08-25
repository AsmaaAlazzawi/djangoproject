from django.shortcuts import render

def home(requset):
    return render(requset, 'mypages/index.html', {'title': 'الصفحة الوئيسية'})

def about(requset):
    return render(requset, 'mypages/about.html', {'title': ' حول'})

def readings(requset):
    return render(requset, 'mypages/readings.html', {'title': ' قراءات ضغط الدم'})

def symptoms(requset):
    return render(requset, 'mypages/symptoms.html', {'title': 'الأعراض والأسباب'})

def influences(requset):
    return render(requset, 'mypages/influences.html', {'title': 'التأثيرات'})

def methods(requset):
    return render(requset, 'mypages/methods.html', {'title': 'طرق الوقاية'}) 

def system(requset):
    return render(requset, 'mypages/system.html', {'title': 'النظام الصحي'})

def tips(requset):
    return render(requset, 'mypages/tips.html', {'title': 'نصائح'})          
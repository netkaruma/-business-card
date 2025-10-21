from django.shortcuts import render
from django.http import JsonResponse

from comments.models import Comments, Like

# Create your views here.


def get_profile(request):
    errors = request.session.get('form_errors',None)

    if errors:
        del request.session['form_errors']

    if request.user.is_authenticated:
        liked_comments = Like.objects.filter(user = request.user).values_list('comment_id', flat=True)
        color = request.user.color_theme
    else:
        liked_comments = []
        color = "rgba(0, 191, 255, 1)"
    context = {
        "comments" : Comments.objects.all().order_by("-id"),
        "liked_comments" : liked_comments,
        "errors": errors,
        "color":color
    }
    
        
    return render(request, "visit.html", context=context)




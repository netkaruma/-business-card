from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from comments.models import Comments, Like
from django.contrib.auth.models import User





def comment_register(request):
    if request.method == "POST" and request.user.is_authenticated:
        comment_text = request.POST.get("comment")
        Comments.objects.create(user=request.user, value=comment_text, likes=0)   
        return redirect('main:main')

    return redirect('main:main')

def delete_comment(request):
    if request.method == "POST" and request.user.is_authenticated:
        Comments.objects.get(id = request.POST.get("comment-id")).delete()
        return redirect('main:main')
    return redirect('main:main')


def update_like(request):
    if request.method == 'POST' and request.user.is_authenticated:
        # Получаем действие (1 - добавление лайка, 0 - удаление лайка)
        try:
            like_action = int(request.POST.get('likeAction'))
        except ValueError:
            return JsonResponse({'success': False, 'message': 'Invalid action'}, status=400)
        comment = Comments.objects.get(id = request.POST.get('comment'))
        # user_likes = User.objects.get()

        Like_exist = Like.objects.filter(user = request.user, comment = comment).exists()
        # Логика добавления или удаления лайка
        if like_action == 1:
            if not Like_exist:
                comment.likes += 1 
                Like.objects.create(user = request.user, comment = comment)
            
            # Логика для добавления лайка (например, увеличиваем количество лайков)
                print("Лайк добавлен")
            else: 
                return redirect("main:main")
            
        elif like_action == 0:

            if Like_exist:
                comment.likes -= 1
                Like.objects.get(user = request.user, comment = comment).delete()
            # Логика для удаления лайка (например, уменьшаем количество лайков)
                print("Лайк удален")
            # Также можно уменьшить количество лайков в базе данных
            else:
                return redirect("main:main")
        else:
            return JsonResponse({'success': False, 'message': 'Invalid action'}, status=400)
        comment.save()
        # Возвращаем успешный ответ
        return JsonResponse({'success': True})
    
    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=400)
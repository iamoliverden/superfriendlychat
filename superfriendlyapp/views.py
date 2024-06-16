from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import ChatMessageCreateForm
from .models import Group

# Create your views here.

@login_required
def chat_view(request):
    chat_group = get_object_or_404(Group, group_name='pizza_lovers')
    chat_messages = chat_group.chat_messages.all()[:120]
    form = ChatMessageCreateForm()
    if request.htmx:
        form = ChatMessageCreateForm(request.POST)
        if form.is_valid:
            message = form.save(commit=False)
            message.author = request.user
            message.group = chat_group
            message.save()
            context = {
                'message': message,
                'user': request.user
            }
            return render(request,'chat_message_p.html', context)

    return render(request, 'chat.html', {'chat_messages':chat_messages,
                  'form': form})
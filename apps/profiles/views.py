from django.shortcuts import render

# Create your views here.
from apps.post.models import Post
from apps.profiles.forms import ProfileModelForm
from apps.profiles.models import Profile, FriendRequest


def edit_my_profile_view(request):
    obj = Profile.objects.get(user=request.user)
    form = ProfileModelForm(request.POST or None, request.FILES or None, instance=obj)
    confirm = False
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            confirm = True
    context = {'obj': obj, 'form': form, 'confirm': confirm}
    return render(request, 'profiles/myprofile.html', context)


#######################################################################################
#
#
# def my_profile(request):
#     p = request.user.profile
#     you = p.user
#     sent_friend_requests = FriendRequest.objects.filter(from_user=you)
#     rec_friend_requests = FriendRequest.objects.filter(to_user=you)
#     user_posts = Post.objects.filter(author=you)
#     friends = p.following.all()
#
#     # is this user our friend
#     button_status = 'none'
#     if p not in request.user.profile.following.all():
#         button_status = 'not_friend'
#
#         # if we have sent him a friend request
#         if len(FriendRequest.objects.filter(
#                 from_user=request.user).filter(to_user=you)) == 1:
#             button_status = 'friend_request_sent'
#
#         if len(FriendRequest.objects.filter(
#                 from_user=p.user).filter(to_user=request.user)) == 1:
#             button_status = 'friend_request_received'
#
#     context = {
#         'u': you,
#         'button_status': button_status,
#         'friends_list': friends,
#         'sent_friend_requests': sent_friend_requests,
#         'rec_friend_requests': rec_friend_requests,
#         'post_count': user_posts.count
#     }
#
#     return render(request, "profiles/profile.html", context)


####################################################################################3

def profile_view(request, first_name):
    p = Profile.objects.filter(first_name=first_name).first()
    u = p.user
    sent_friend_requests = FriendRequest.objects.filter(from_user=p.user)
    rec_friend_requests = FriendRequest.objects.filter(to_user=p.user)
    user_posts = Post.objects.filter(author=p.pk)

    friends = p.following.all()

    # is this user our friend
    button_status = 'none'
    if p not in request.user.profile.following.all():
        button_status = 'not_friend'

        # if we have sent him a friend request
        if len(FriendRequest.objects.filter(
                from_user=request.user).filter(to_user=p.user)) == 1:
            button_status = 'friend_request_sent'

        # if we have recieved a friend request
        if len(FriendRequest.objects.filter(
                from_user=p.user).filter(to_user=request.user)) == 1:
            button_status = 'friend_request_received'

    context = {
        'u': u,
        'button_status': button_status,
        'friends_list': friends,
        'sent_friend_requests': sent_friend_requests,
        'rec_friend_requests': rec_friend_requests,
        'user_posts': user_posts,
        'post_count': user_posts.count
    }

    return render(request, "profiles/profile.html", context)

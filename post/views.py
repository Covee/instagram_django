from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from .models import Post, Comment


def post_list(request):
	posts = Post.objects.all()
	context = {
		'posts': posts,
	}
	return render(request, 'post/post_list.html', context)


def comment_create(request, post_pk):
	if request.method == 'POST':          # it only works when POST requested
		post = get_object_or_404(Post, pk=post_pk)          # load POST instance or pop up a '404 Response'
		comment_form = CommentForm(request.POST)          # request.POST를 이용한 Bounded Form 생성
		if comment_form.is_valid():          # form 데이터 유효성 검사
			Comment.objects.create(          # valid 하면 comment객체 생성 및 DB에 저장
				post=post,
				author=request.user,
				content = comment_form.cleaned_data['content']
			)
			# comment 생성 후, 'post'네임스페이스를 가진 url의 'post_list'이름에 해당하는 뷰로 이동

		# if not content:          # 'content'가 없거나 내용이 없을 경우
		# 	return HttpResponse('댓글 내용을 입력하세요.', status=400)          # BadRequest(400) 응답을 전송

		return redirect('post:post_list')          # 'post'네임스페이스를 가진 url의 'post_list'이름에 해당하는 뷰로 이동


from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

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
		content = request.POST.get('content')          # take a value of 'content' from the request.POST

		if not content:          # 'content'가 없거나 내용이 없을 경우
			return HttpResponse('댓글 내용을 입력하세요.', status=400)          # BadRequest(400) 응답을 전송

		Comment.objects.create(          # 내용이 전달 된 경우, Comment객체 생성 및 DB에 저장
			post = post,
			author = request.user,     # 작성자는 현재 요청하는 사용자로 지정
			content = content
		)

		return redirect('post:post_list')          # 'post'네임스페이스를 가진 url의 'post_list'이름에 해당하는 뷰로 이동

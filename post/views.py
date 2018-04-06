from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm, PostForm
from .models import Post, Comment
from django.contrib import messages


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
			comment = comment_form.save(commit=False)  # 통과시 ModelForm의 save()호출로 인스턴스 생성, DB에 저장하지 않고 인스턴스 생성만을 위해 commit=False옵션
			comment.post = post          # 필수요소 author와 post속성 지정
			comment.author = request.user
			comment.save()          # DB에 저장
			messages.success(request, '댓글이 등록되었습니다')   # 성공 메시지를 다음 request 결과로 전달하도록 지정
		else:         # 유효성 검사 실패시,
			error_msg = '댓글 등록에 실패했습니다\n{}'.format(     # error목록을 순회하며 에러메시지 작성, messages의 error레벨로 추가
				'\n'.join(
					[f'-{error}'
					for key, value in comment_form.errors.items()
					for error in value]))
			messages.error(request, error_msg)

			# Comment.objects.create(          # valid 하면 comment객체 생성 및 DB에 저장
			# 	post=post,
			# 	author=request.user,
			# 	content = comment_form.cleaned_data['content']
			# )
			# comment 생성 후, 'post'네임스페이스를 가진 url의 'post_list'이름에 해당하는 뷰로 이동

		# if not content:          # 'content'가 없거나 내용이 없을 경우
		# 	return HttpResponse('댓글 내용을 입력하세요.', status=400)          # BadRequest(400) 응답을 전송

		return redirect('post:post_list')    # comment_form의 valid 여부와 관계없이 post'네임스페이스를 가진 url의 'post_list'이름에 해당하는 뷰로 이동

def post_detail(request, post_pk):
	post = get_object_or_404(Post, pk=post_pk)
	comment_form = CommentForm()
	context = {
		'post': post,
		'comment_form': comment_form,
	}
	return render(request, 'post/post_detail.html', context)

def post_create(request):
	if request.method == 'POST':
		post_form = PostForm(request.POST, request.FILES)
		if post_form.is_valid():
			post = post_form.save(commit=False)
			post.author = request.user
			post.save()

			messages.success(request, '사진이 등록되었습니다.')
			return redirect('post:post_list')
	else:
		post_form = PostForm()

	context = {
		'post_form': post_form,
	}
	return render(request, 'post/post_create.html', context)
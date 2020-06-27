from django.shortcuts import render, redirect

from catalog.models import Category
from .forms import ContactForm
from .models import Contact
from django.utils import timezone

def index(request):
	data = {
		'categorias': Category.objects.all()
	}
	return render(request, 'index.html', data)

def contact(request):
	form_class = Contact

	if request.method == 'POST':
		form = ContactForm(request.POST)
		f = form.save(commit=False)
		f.send = timezone.now()
		f.save()
		return redirect('tela-inicial')
	else:
		form = ContactForm()

	data ={
		'form': form
	}
	return render(request, 'contact.html', data)

# View da Class-Based view
from django.views.generic import CreateView
from accounts.models import User
from accounts.forms import UserAdminCreationForm

class RegisterView(CreateView):
	# pega o template
	form_class = UserAdminCreationForm
	# renderiza o template
	template_name = 'cadastrar-se.html'
	# passa o objeto
	model = User

	# caso der certo o cadastro encaminhar para a url com o seguinte nome
	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.user = self.request.user
		self.object.save()
		return redirect('tela-inicial')
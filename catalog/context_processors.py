from .models import Category

def categories(erquest):
	return {
		'categorias': Category.objects.all()
	}
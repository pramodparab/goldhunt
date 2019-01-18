from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):

	class goldtype:
		"""docstring for goldtype"""
		def __init__(self, name , value ,material, location ):
			self.name = name
			self.value = value
			self.material = material
			self.location = location

	goldtype = [ 

				goldtype('Puregold' , '1000', 'gold', 'MUM'),
				goldtype('Softgold', '400', 'impure gold', 'Pu'),
				goldtype('slvgold', '0', 'svgold impure', 'Anf')
	]			 

			



	return render( request,'index.html' , {'goldtype':goldtype})

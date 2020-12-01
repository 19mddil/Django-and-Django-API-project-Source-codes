from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token

from users.models import Paitent, Doctor

class PaitentCustomRegistrationSerializer(RegisterSerializer):
	paitent = serializers.PrimaryKeyRelatedField(read_only=True,) #by default it will do allow_null = False
	name = serializers.CharField(required=True)
	email = serializers.EmailField(required=True)
	age = serializers.IntegerField(required=True)
	sex = serializers.CharField(required=True)
	case = serializers.CharField(style={'base_template': 'textarea.html'})
	cell_number_one = serializers.CharField(required=True)

	def get_cleaned_data(self):
		data = super(PaitentCustomRegistrationSerializer, self).get_cleaned_data()
		get_data = {
			'name' : self.validated_data.get('name', ''),
			'email' : self.validated_data.get('email', ''),
			'age': self.validated_data.get('age', 0),
			'sex':self.validated_data.get('sex',''),
			'case':self.validated_data.get('case',''),
			'cell_number_one':self.validated_data.get('cell_number_one',''),
		}
		data.update(get_data)
		return data

	def save(self, request):
		user = super(PaitentCustomRegistrationSerializer, self).save(request)
		user.is_paitent = True
		user.save()
		paitent = Paitent(
			paitent=user, 
			name=self.cleaned_data.get('name'),
			email=self.cleaned_data.get('email'),
			age=self.cleaned_data.get('age'),
			sex=self.cleaned_data.get('sex'),
			case=self.cleaned_data.get('case'),
			cell_number_one=self.cell_number_one.get('cell_number_one'),
		),

		paitent.save()
		return paitent


class DoctorCustomRegistrationSerializer(RegisterSerializer):
	Doctor = serializers.PrimaryKeyRelatedField(read_only=True,) #by default it will do allow_null = False
	email = serializers.EmailField(required=True)

	def get_cleaned_data(self):
		data = super(DoctorCustomRegistrationSerializer, self).get_cleaned_data()
		get_data = {
		    'email' : self.validated_data.get('email', ''),
		}
		data.update(get_data)
		return data

	def save(self, request):
		user = super(DoctorCustomRegistrationSerializer, self).save(request)
		user.is_doctor = True
		user.save()
		doctor = Buyer(doctor=user,email=self.cleaned_data.get('email'))
		doctor.save()
		return doctor

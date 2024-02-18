from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def C4_5(obj): #obj[0]: CAT I, obj[1]: CAT II, obj[2]: CAT III, obj[3]: class
	# {"feature": "class", "instances": 487, "metric_value": 1.9421, "depth": 1}
	if obj[3]<=1:
		# {"feature": "CAT II", "instances": 386, "metric_value": 1.4205, "depth": 2}
		if obj[1]<=70.47707029931173:
			# {"feature": "CAT I", "instances": 358, "metric_value": 1.1203, "depth": 3}
			if obj[0]<=76.84863190924473:
				# {"feature": "CAT III", "instances": 356, "metric_value": 1.0877, "depth": 4}
				if obj[2]<=77.82777000676187:
					return '6'
				elif obj[2]>77.82777000676187:
					return '7'
				else: return '7'
			elif obj[0]>76.84863190924473:
				return '8'
			else: return '8'
		elif obj[1]>70.47707029931173:
			# {"feature": "CAT III", "instances": 28, "metric_value": 1.2871, "depth": 3}
			if obj[2]<=87:
				# {"feature": "CAT I", "instances": 24, "metric_value": 1.0409, "depth": 4}
				if obj[0]<=89:
					return '8'
				elif obj[0]>89:
					return '9'
				else: return '9'
			elif obj[2]>87:
				return '9'
			else: return '9'
		else: return '8'
	elif obj[3]>1:
		# {"feature": "CAT III", "instances": 101, "metric_value": 0.5539, "depth": 2}
		if obj[2]>86:
			# {"feature": "CAT II", "instances": 89, "metric_value": 0.3121, "depth": 3}
			if obj[1]>87:
				# {"feature": "CAT I", "instances": 77, "metric_value": 0.1, "depth": 4}
				if obj[0]>84:
					return '10'
				elif obj[0]<=84:
					return '10'
				else: return '10'
			elif obj[1]<=87:
				# {"feature": "CAT I", "instances": 12, "metric_value": 0.9183, "depth": 4}
				if obj[0]>86:
					return '10'
				elif obj[0]<=86:
					return '9'
				else: return '9'
			else: return '10'
		elif obj[2]<=86:
			# {"feature": "CAT II", "instances": 12, "metric_value": 0.9183, "depth": 3}
			if obj[1]<=90:
				return '9'
			elif obj[1]>90:
				# {"feature": "CAT I", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[0]>90:
					return '10'
				elif obj[0]<=90:
					return '9'
				else: return '9'
			else: return '10'
		else: return '9'
	else: return '10'
	

def Regression(obj): #obj[0]: CAT I, obj[1]: CAT II, obj[2]: CAT III, obj[3]: class, obj[4]: round
	# {"feature": "round", "instances": 487, "metric_value": 1.0201, "depth": 1}
	if obj[4]<=8:
		# {"feature": "class", "instances": 380, "metric_value": 0.1741, "depth": 2}
		if obj[3]<=0:
			# {"feature": "CAT III", "instances": 347, "metric_value": 0.0721, "depth": 3}
			if obj[2]>58.77233429394813:
				# {"feature": "CAT I", "instances": 209, "metric_value": 0.0216, "depth": 4}
				if obj[0]>55.39234449760765:
					# {"feature": "CAT II", "instances": 132, "metric_value": 0.0248, "depth": 5}
					if obj[1]<=63:
						return 6.3
					elif obj[1]>63:
						return 6.5
					else: return 6.47295081967213
				elif obj[0]<=55.39234449760765:
					# {"feature": "CAT II", "instances": 77, "metric_value": 0.0123, "depth": 5}
					if obj[1]>47.54545454545455:
						return 6.2
					elif obj[1]<=47.54545454545455:
						return 6.0
					else: return 6.0990625
				else: return 6.1202597402597405
			elif obj[2]<=58.77233429394813:
				# {"feature": "CAT II", "instances": 138, "metric_value": 0.1047, "depth": 4}
				if obj[1]>56.731884057971016:
					# {"feature": "CAT I", "instances": 82, "metric_value": 0.0055, "depth": 5}
					if obj[0]>40.93830675229795:
						return 6.2
					elif obj[0]<=40.93830675229795:
						return 6.0
					else: return 6.12
				elif obj[1]<=56.731884057971016:
					# {"feature": "CAT I", "instances": 56, "metric_value": 0.0165, "depth": 5}
					if obj[0]<=60.23429428834949:
						return 5.1
					elif obj[0]>60.23429428834949:
						return 5.9
					else: return 5.703749999999999
				else: return 5.438750000000001
			else: return 5.794565217391305
		elif obj[3]>0:
			# {"feature": "CAT III", "instances": 33, "metric_value": 0.0946, "depth": 3}
			if obj[2]>73:
				# {"feature": "CAT II", "instances": 17, "metric_value": 0.0661, "depth": 4}
				if obj[1]>71:
					# {"feature": "CAT I", "instances": 13, "metric_value": 0.05, "depth": 5}
					if obj[0]<=87:
						return 7.89
					elif obj[0]>87:
						return 8.45
					else: return 8.45
				elif obj[1]<=71:
					return 7.5725
				else: return 7.5725
			elif obj[2]<=73:
				# {"feature": "CAT II", "instances": 16, "metric_value": 0.1328, "depth": 4}
				if obj[1]<=75:
					# {"feature": "CAT I", "instances": 12, "metric_value": 0.0411, "depth": 5}
					if obj[0]<=75:
						return 7.0
					elif obj[0]>75:
						return 7.54
					else: return 7.54
				elif obj[1]>75:
					return 7.805
				else: return 7.805
			else: return 7.333125000000001
		else: return 7.6042424242424245
	elif obj[4]>8:
		# {"feature": "class", "instances": 107, "metric_value": 0.0805, "depth": 2}
		if obj[3]>1:
			# {"feature": "CAT III", "instances": 101, "metric_value": 0.0481, "depth": 3}
			if obj[2]>91:
				# {"feature": "CAT II", "instances": 70, "metric_value": 0.0212, "depth": 4}
				if obj[1]>85:
					# {"feature": "CAT I", "instances": 66, "metric_value": 0.0054, "depth": 5}
					if obj[0]>80:
						return 10.0
					elif obj[0]<=80:
						return 9.54
					else: return 9.772499999999999
				elif obj[1]<=85:
					return 9.61
				else: return 9.61
			elif obj[2]<=91:
				# {"feature": "CAT I", "instances": 31, "metric_value": 0.1085, "depth": 4}
				if obj[0]>86:
					# {"feature": "CAT II", "instances": 24, "metric_value": 0.0443, "depth": 5}
					if obj[1]>85:
						return 10.0
					elif obj[1]<=85:
						return 9.2
					else: return 9.47
				elif obj[0]<=86:
					# {"feature": "CAT II", "instances": 7, "metric_value": 0.0427, "depth": 5}
					if obj[1]<=88:
						return 9.2
					elif obj[1]>88:
						return 9.0
					else: return 9.0
				else: return 9.182857142857143
			else: return 9.640967741935484
		elif obj[3]<=1:
			# {"feature": "CAT II", "instances": 6, "metric_value": 0.0217, "depth": 3}
			if obj[1]>85:
				return 8.92
			elif obj[1]<=85:
				return 8.833333333333334
			else: return 8.833333333333334
		else: return 8.876666666666667
	else: return 9.764822429906543

@api_view(['GET'])
def get_prediction(request, cat1, cat2, cat3, bayers):
	
	if(cat1!=None and cat2!=None and cat3!=None and bayers!=None):
		sets = [cat1, cat2, cat3, bayers]
		sets.append(int(C4_5(sets)))
		sets.append(Regression(sets))
		return Response(sets[-1],status=status.HTTP_200_OK)
	else:
		return Response("Check the parameters",status=status.HTTP_400_BAD_REQUEST)
	
    


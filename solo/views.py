from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import postQuery
import pyjarowinkler
import main
# import ast

# Create your views here.

def test(request):
	if request.method == "POST" and not request.FILES:
		# flag = 'Non Forex'
		# tmp = 0.0
		form = postQuery(request.POST)
		if form.is_valid():
			# print form['query'].value()
			company = form['query'].value()
			score, features, urls = processCompanyName(form['query'].value())
			if(features[5] == 0):
				features[5] = "NA"
			# tmp = ast.literal_eval(score)
			# if(tmp >= 0.85):
				# flag = 'Forex'
			li = [["IEC Number", features[5]], ["Country Count", features[0]], ["City Count", features[1]], ["Import Count", features[2]], ["Export Count", features[3]], ["Keywords Count", features[4]]]
            #Order of feature list is countrycount, citycount, importcount,exportcount,keywordCount,isIEC
			return render(request, "result.html", {'score' : score, 'li' : li, 'company' : company, 'urls' : urls})
		else:
			pass
		return HttpResponse("Query Submitted, score:" + str(score))
	elif request.method == 'POST' and request.FILES['myfile']:
		myfile = request.FILES['myfile']
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
		uploaded_file_url = fs.url(filename)
		score_list,feature_list = processCompanyFile(uploaded_file_url)
		return HttpResponse("File Uploaded" + str(score_list))
	else:
		form = postQuery()
		return render(request, "index.html", {'form' : form})

def processCompanyName(company_name):
	obj = main.Logic()
	isiec = isIEC(company_name)
	score,features, urls = obj.process(company_name, isiec, settings.BASE_DIR)
	return score,features,urls


def processCompanyFile(filePath):
	filePath = settings.BASE_DIR + filePath
	file = open(filePath, "r+")
	score_list = []
	feature_list = []
	for line in file:
		company = line[:len(line) - 1]
		#search.objects.create(query = company, score = 0, date = timezone.now())
		score,features = processCompanyName(company)
		score_list.append(score)
		feature_list.append(features)
	return score_list,feature_list

def isIEC(company):
    #filename = settings.BASE_DIR + '/solo/iec.csv'
	filename =  './solo/iec.csv'
	f = open(filename, 'r')
	line = f.readline()
	flag = False
	while (line):
		company_name = line.split('\t')[1]
		try:
			company_name = str(company_name)
			company = str(company)
			dis = pyjarowinkler.get_jaro_distance(str(company), str(company_name), winkler = True, scaling = 0.1)
		except Exception as e:
			dis = 0.7
		if(dis >= 0.85):
			flag = True
			break
		line = f.readline()
	return flag

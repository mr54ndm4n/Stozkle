from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, render_to_response
from .models import Member, Equipment
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def store(request):
	store = Member.objects.get(nick_name = 'Store')
	equipslist = store.equipment_set.all()
	# equipslist = []
	# equips = Equipment.objects.all()
	# for equip in equips:
	# 	if str(equip.member) == 'Store':
	# 		equipslist += equip
	return render(request, 'equiplist.html', {'equips': equipslist})

@login_required(login_url='/login/')
def store_detail(request, equip_id):
	# equips = Equipment.objects.get(id=equip_id)
	equip = get_object_or_404(Equipment, id=equip_id)
	context = RequestContext(request)
	member = Member.objects.get(user = request.user)
	#context.update({'equip': equip})
	if request.method == 'POST':
		amount = request.POST['amount']
		# print(amount)
		if amount == '':
			error = 'Please enter int value'
			link = '/store/'+str(equip.id)
			return render(request, 'error.html', {'error': error, 'link':link})

		elif int(amount) > equip.amount:
			error = 'You can\'t borrow more than equipment amout in store'
			link = '/store/' + str(equip.id)
			return render(request, 'error.html', {'error': error, 'link':link})
		elif int(amount) < 0:
			error = 'You Borrow in negative number'
			link = '/store/' + str(equip.id)
			return render(request, 'error.html', {'error': error, 'link':link})
		else:
			#Can Borrow
			equip.amount -= int(amount)
			equip.save()
			myObject = Member.objects.get(nick_name = member.nick_name)
			scp = 'alert("You\'re Borrowed");'
			try:
				eq = myObject.equipment_set.get(name = equip.name)
				eq.amount += int(amount)
				eq.save()
			except:
				myObject.equipment_set.create(name=equip.name, member=member, size=equip.size, amount = int(amount), detail=equip.detail, address=equip.address)
			return render_to_response('equip.html', {'equip': equip}, context)
	else:
		return render_to_response('equip.html', {'equip': equip}, context)
# equips.amount += 1
	# equips.save()
# q = Member.objects.get(nick_name='Store')
# q = equipment_set.get(name='xxx') and use try/catch

@login_required(login_url='/login/')
def profile(request):
	count = 0
	context = RequestContext(request)
	user = request.user
	member = Member.objects.get(user = user)
	store = Member.objects.get(nick_name = 'Store')
	myObject = Member.objects.get(nick_name = member.nick_name)
	equips = myObject.equipment_set.all()
	#if request.method == 'POST':
	if request.POST:
		for equip in equips:
			if(equip.name) in request.POST:
				returnItem = store.equipment_set.get(name = equip.name)
				amt = request.POST['amount'+equip.name]
				if amt == '':
					error = 'Please enter value'
					link = '/store/profile'
					return render(request, 'error.html', {'error': error, 'link':link})
				amount = int(amt)
				if amount < 0:
					error = 'Please enter positive value'
					link = '/store/profile'
					return render(request, 'error.html', {'error': error, 'link':link})
				elif amount > equip.amount:
					error = 'You can\' return equipment more than you have'
					link = '/store/profile'
					return render(request, 'error.html', {'error': error, 'link':link})
				if equip.amount > 0:
					returnItem.amount += amount
					equip.amount -= amount 
					equip.save()
					returnItem.save()
	equiplist = []
	for equip in equips:
		if equip.amount != 0:
			count += 1
			equiplist.append(equip)
	return render_to_response('profile.html', {'user': user, 'member': member, 'equips': equiplist, 'count':count}, context)
# render(request, 'myStock/base.html', {'store': store})
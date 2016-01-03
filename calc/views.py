from django.shortcuts import render
from django.http import HttpResponse
from .models import School

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def calculator(request):
	context = {}
	return render(request, 'calc/calculator.html', context)

def participants(request):
    schools = School.objects.all()
    return HttpResponse(schools)

def compute(request):
	school = request.POST['school']
	state = request.POST['state']
	emissions = request.POST['emissions']
	c_lighting = c_lighting_emissions(request)
	nc_lighting = nc_lighting_emissions(request)
	heating = heating_emissions(request)
	ac = ac_emissions(request)
	wh = wh_emissions(request)
	car = car_emission(request)
	carpool = carpool_emission(request)
	bus = bus_emission(request)
	walk = walk_emission(request)
	bike = bike_emission(request)

	s = School.objects.create(name=school, state=state, emissions=emissions)
	response = school + " has " + str(c_lighting) + " classroom lighting emissions, " + str(nc_lighting) + " non-classroom lighting emissions, " + str(heating) + " heating emissions, " + str(ac) + " air conditioning emissions, " + str(wh) + " water heating emissions, " + str(car) + " car emissions, " + str(carpool) + " carpool emissions, " + str(bus) + " bus emissions, " + str(walk) + " walking emissions, " + str(bike) + " biking emissions."
	return HttpResponse(response)

def c_lighting_emissions(request):
	return 1628.60 * float(request.POST['classrooms']) * float(request.POST['clb_units']) * float(request.POST['clb_watts']) * float(request.POST['hours']) * 180 * 0.4536 / 1000 / 1000

def nc_lighting_emissions(request):
	return 1628.60 * float(request.POST['nclb_units']) * float(request.POST['nclb_watts']) * float(request.POST['hours']) * 180 * 0.4536 / 1000 / 1000

def heating_emissions(request):
	heating_type = request.POST['heating_type']
	emissions = 0
	if heating_type == 'Electric':
		emissions = 1628.60 * float(request.POST['heating_days']) * float(request.POST['heating_units']) * float(request.POST['heating_watts']) * float(request.POST['hours']) * 0.4536 / 1000 / 1000
	elif heating_type == 'Gas':
		emissions = 581.4442 * float(request.POST['heating_days']) * float(request.POST['heating_units']) * float(request.POST['heating_watts']) * float(request.POST['hours']) * 0.4536 / 1000 / 1000
	elif heating_type == 'Diesel':
		emissions = 589.7431 * float(request.POST['heating_days']) * float(request.POST['heating_units']) * float(request.POST['heating_watts']) * float(request.POST['hours']) * 0.4536 / 1000 / 1000
	elif heating_type == 'Propane':
		emissions = 474.3694 * float(request.POST['heating_days']) * float(request.POST['heating_units']) * float(request.POST['heating_watts']) * float(request.POST['hours']) * 0.4536 / 1000 / 1000
	return emissions

def ac_emissions(request):
	return 1628.60 * float(request.POST['ac_days']) * float(request.POST['ac_units']) * float(request.POST['heating_units']) * float(request.POST['ac_watts']) * float(request.POST['hours']) * 0.4536 / 1000 / 1000

def wh_emissions(request):
	emissions_type = request.POST['wh_type']
	emissions = 0
	if emissions_type == 'Electric':	
		emissions = 1628.60 * float(request.POST['avg_wh_watts']) * float(request.POST['wh_units']) * float(request.POST['hours']) * 180 * 0.4536 / 1000 / 1000
	else: 
		emissions = 581.4442 * float(request.POST['avg_wh_watts']) * float(request.POST['wh_units']) * float(request.POST['hours']) * 180 * 0.4536 / 1000 / 1000
	return emissions

def car_emission(request):
	return float(request.POST['students']) * float(request.POST['p_drive']) * float(request.POST['avg_distance']) * 2 * 2 * 8.81 * 180 / 22 / 100

def carpool_emission(request):
	return float(request.POST['students']) * float(request.POST['p_carpool']) * float(request.POST['avg_distance']) / float(request.POST['avg_carpool_students']) * 2 * 2 * 8.81 * 180 / 22 / 100

def bus_emission(request):
	return float(request.POST['students']) * float(request.POST['p_bus']) * float(request.POST['avg_bus_dist']) / float(request.POST['bus_students']) * 2 * 2 * 10.15 * 180 / 8 / 100

def walk_emission(request):
	return float(request.POST['students']) * float(request.POST['p_walk']) * 1.71 * 2 * 0.0195 * 180 / 100

def bike_emission(request):
	return float(request.POST['students']) * float(request.POST['p_bike']) * 1.6 * 2 * 0.0085 * 180 / 100

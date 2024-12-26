from django.shortcuts import render, redirect, HttpResponse
from .models import Leave, Driver
from django.contrib import messages
from .forms import ExcelFileForm
import pandas as pd
from django.db.models import Q
from .utils import sms_sender

def index(request):
    if request.method == 'POST':
        nation_code = request.POST['NationCode']
        phone_number = request.POST['phone_number']
        end_date = request.POST['end']
        start_date = request.POST['start']
        state = request.POST['state']
        city = request.POST['city']
        year, month, day = map(int, start_date.split('/'))
        start_date = f"{year}-{month}-{day}"
        # start_day = day
        year, month, day = map(int, end_date.split('/'))
        end_date = f"{year}-{month}-{day}"
        # end_day = day
        # len_leave = end_day - start_day
        # if len_leave > 9:
        driver = Driver.objects.filter(Q(nation_code=nation_code) &
                                       Q(mobile_number=phone_number)).first()
        if driver:
            Leave.objects.create(nation_code=nation_code, mobile_number=phone_number, end_date=end_date,
                                 start_date=start_date, state_travel_destination=state,
                                 city_travel_destination=city, driver=driver)
            print('done')
            result = sms_sender(driver.mobile_number)
            if not result:
                return render(request, 'accept.html', context={'random_code':result})
            else:
                messages.success(request,
                                 'در ارسال کد تایید مشکلی پیش امده لطفا شماره تماس خود را بررسی کنید')


        messages.success(request, 'فرد با این مشخصات یافت نشد')
        return redirect('leaves')
        # else:
        #     messages.success(request, 'مدت زمان مرخصی بیشتر از ۹ روز ممکن نیست')
        #     return redirect('leaves')
    return render(request, 'req-form.html')


# def get_all_states_city(request):
#     response = requests.get('https://amib.ir/weblog/wp-content/uploads/amib/iran-provinces-cities/')
#     soup = BeautifulSoup(response.content, 'html.parser')
#     soup_1 = soup.find_all('tr')
#     state = []
#     city = []
#     for item in soup_1:
#         state.append(item.contents[0].text)
#         city.append((item.contents[0].text, item.contents[1].text))
#     state = list(set(state))
#     state.sort()
#     with open('state.txt', 'w') as file:
#         for item in state:
#             file.write(item + '\n')
#     with open('city.txt', 'w') as file:
#         for item in city:
#             for i in item:
#                 file.write(i + '-')
#             file.write('\n')
#     return HttpResponse('<h1>done</h1>')
#
#
# def set_state_and_city(request):
#     states = State.objects.all()
#     if states:
#         State.objects.all().delete()
#     with open('state.txt', 'r') as file:
#         state = file.read()
#     state = state.split('\n')
#     for item in state:
#         if len(item) > 1:
#             State.objects.create(name=item)
#     with open('city.txt', 'r') as file:
#         city = file.read()
#     city = city.split('\n')
#     for item in city:
#         item_1 = item.split('-')
#         item_1.remove(item_1[-1])
#         city[city.index(item)] = item_1
#     cities = City.objects.all()
#     if cities:
#         City.objects.all().delete()
#     for item in city:
#
#         try:
#             City.objects.create(name=item[1], state=State.objects.get(name=item[0]))
#         except IndexError:
#             pass
#     return HttpResponse('<h1>done 2</h1>')
#

def get_excel(request):
    if request.method == 'POST':
        form = ExcelFileForm(request.POST, request.FILES)
        if form.is_valid():
            excel = form.cleaned_data['file']
            if excel.name == 'مسافربرشخصی.xlsx':
                data = pd.read_excel(excel)
                data = data.drop_duplicates()
                data = data.fillna('')

                for i, row in data.iterrows():
                    Driver.objects.create(
                        nation_code=row['کد ملی'],
                        name=row['نام'],
                        family=row['نام خانوادگی'],
                        father_name=row['نام پدر'],
                        mobile_number=str(row['تلفن همراه']).split('.')[0],
                        car=row['سیستم'],
                        city_code=row['ایران'],
                        three_len_code=row['سه رقم'],
                        alphabet=row['Unnamed: 9'],
                        two_len_code=row['دو رقم']
                    )
            elif excel.name == 'اکسل تاکسی.xlsx':
                data = pd.read_excel(excel)
                print(data)
    form = ExcelFileForm()
    return render(request=request, template_name='excel_test.html', context={'form': form})


def verify_request(request):
    pass
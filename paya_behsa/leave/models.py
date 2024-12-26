from django.db import models
from django.core.validators import MinLengthValidator
from django_jalali.db import models as jalali_models
import jdatetime


class LeaveRestriction(models.Model):
    day_per_year = models.IntegerField(verbose_name='تعداد روز های مجاز سالانه', default=60)

    class Meta:
        verbose_name = "تعداد روز های مجاز مرخصی سالانه"
        verbose_name_plural = "مرخصی در سال"

    def save(self, *args, **kwargs):
        if self.id:
            LeaveRestriction.objects.all().delete()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.day_per_year)


class State(models.Model):
    name = models.CharField(max_length=255, verbose_name='اسم استان')

    class Meta:
        verbose_name = "استان مد نظر"
        verbose_name_plural = "استان ها"

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=255, verbose_name='شهر استان')
    state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name='اسم استان مربوط')

    class Meta:
        verbose_name = "شهر مد نظر"
        verbose_name_plural = "شهر ها"

    def __str__(self):
        return f'{self.name} - {self.state}'


class Driver(models.Model):
    nation_code = models.CharField(max_length=10, validators=[MinLengthValidator(10)], verbose_name='کد ملی')
    name = models.CharField(max_length=255, verbose_name='نام')
    family = models.CharField(max_length=255, verbose_name='نام خانوادگی')
    father_name = models.CharField(max_length=255, verbose_name='نام پدر')
    mobile_number = models.CharField(max_length=15, validators=[MinLengthValidator(10)], verbose_name='تلفن همراه')
    car = models.CharField(max_length=255, verbose_name='سیستم')
    city_code = models.CharField(max_length=2, validators=[MinLengthValidator(2)], verbose_name='ایران')
    three_len_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)], verbose_name='سه رقم')
    alphabet = models.CharField(max_length=1, validators=[MinLengthValidator(1)], verbose_name='حرف')
    two_len_code = models.CharField(max_length=2, validators=[MinLengthValidator(2)], verbose_name='دو رقم')

    leave_restriction = models.IntegerField(default=0,verbose_name='مرخصی های باقی مانده')

    class Meta:
        verbose_name = "راننده مد نظر"
        verbose_name_plural = "راننده ها"

    def save(self, *args, **kwargs):
        if self.leave_restriction == 0:
            self.leave_restriction = LeaveRestriction.objects.first().day_per_year
        super().save(*args, **kwargs)

    def __str__(self):
        return (f'|{self.name}- {self.family} --- |{self.city_code}|{self.two_len_code}{self.alphabet}'
                f'{self.three_len_code}')


class Leave(models.Model):
    nation_code = models.CharField(max_length=10, validators=[MinLengthValidator(10)], verbose_name='کد ملی')
    mobile_number = models.CharField(max_length=14, validators=[MinLengthValidator(10)], verbose_name='شماره تماس')
    start_date = jalali_models.jDateField(default=jdatetime.date.today, verbose_name='شروع مرخصی')
    end_date = jalali_models.jDateField(default=jdatetime.date.today, verbose_name='پایان مرخصی')
    state_origin_trip = models.CharField(max_length=250, default='مازندران', verbose_name='استان مبدا سفر راننده')
    city_origin_trip = models.CharField(max_length=250, default='آمل', verbose_name='شهر مبدا سفر راننده')
    state_travel_destination = models.CharField(max_length=250, verbose_name='استان مقصد سفر راننده', default='')
    city_travel_destination = models.CharField(max_length=250, verbose_name='شهر مقصد سفر راننده', default='')
    status = models.BooleanField(default=False, verbose_name='تایید فرم مرخصی راننده')

    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, default='')

    class Meta:
        verbose_name = "فرم مرخصی"
        verbose_name_plural = "فرم مرخصی ها"

    def __str__(self):
        return f'{self.driver.nation_code} {self.start_date} {self.end_date}'

import uuid

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.utils.crypto import get_random_string
from django_jalali.db import models as jmodels

from datetime import date

from django.core.validators import RegexValidator

from multiselectfield import MultiSelectField


def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.mp4', '.mpeg', '.mpg', '.ts', '.mkv']
    if not ext.lower() in valid_extensions:
        raise ValidationError('فایل ویدیی فقط باید انتخاب شود')


def validate_file_pdf(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError('فایل pdf فقط باید انتخاب شود')


from django.forms import ModelForm, PasswordInput


class PersonInfo(models.Model):
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربرها'
        # ordering = ['due_back']


    def __str__(self):
        return '{0} {1} '.format(self.FirstName, self.LastName)

    SEX = (
        ('m', 'مرد'),
        ('f', 'خانم'),
    )
    BLooDT = (
        ('a+', 'a+'),
        ('a-', 'a-'),
        ('b+', 'b+'),
        ('b-', 'b-'),
        ('ab+', 'ab+'),
        ('ab-', 'ab-'),
        ('o+', 'o+'),
        ('o-', 'o-'),
    )
    VAZYATEtAHOL = (
        ('s', 'مجرد'),
        ('m', 'متاهل')
    )
    NESBAT = (
        ('k', 'خودم'),
        ('h', 'همسرم'),
        ('f', 'فرزندم'),
        ('t', 'تحت تکلفم'),
    )
    TAHSILAT = (
        ('m', 'محصل'),
        ('d', 'دیپلم و زیر دیپلم'),
        ('l', 'لیسانس'),
        ('f', 'فوق لیسانس'),
        ('d', 'دکترا'),
    )

    Token2 = get_random_string(length=64)

    Username = models.CharField(unique=True, max_length=50, verbose_name='نام کاربری')
    Password = models.CharField(max_length=50, verbose_name='رمز ورود')

    ApiToken = models.CharField(unique=True, default=Token2, max_length=64, auto_created=True)
    FirstName = models.CharField(max_length=50, null=False, verbose_name='نام')
    LastName = models.CharField(max_length=50, null=False, verbose_name='نام خانوادگی')
    FatherName = models.CharField(max_length=50, null=False, verbose_name='نام پدر')
    Sex = models.CharField(max_length=1,
                           choices=list(SEX),
                           default='m',
                           verbose_name='جنسیت')
    # DateOfBart = models.DateField(verbose_name='تاریخ تولد')
    objects = jmodels.jManager()

    DateOfBart =jmodels.jDateField(verbose_name='تاریخ تولد',default='1370-1-1')
    bloodType = models.CharField(max_length=3,
                                 choices=list(BLooDT),
                                 default='a',
                                 verbose_name='گروه خونی')
    NationalCode = models.IntegerField(null=False, verbose_name='کد ملی')
    ShenasnameCode = models.IntegerField(null=False, verbose_name='شماره شناسنامه')
    MohaleSedor = models.IntegerField(null=False, verbose_name='محل صدور')
    VazyateTahol = models.CharField(max_length=1,
                                    choices=list(VAZYATEtAHOL),
                                    default='s',
                                    verbose_name='وضعیت تاهل ')
    Tahsilat = models.CharField(max_length=1,
                                choices=list(TAHSILAT),
                                default='m',
                                verbose_name='تحصیلات',
                                help_text='تحصیلات شما'
                                )
    Address = models.TextField(max_length=300, verbose_name='آدرس کامل')

    phone_regex = RegexValidator(regex=r'^\+?0?\d{8,11}$', message="شماره وارد شده صحیح نمیباشد")
    phoneNumber = models.CharField(validators=[phone_regex], max_length=11, blank=True,
                                   verbose_name='شماره همراه')  # validators should be a list

    # phoneNumber = PhoneNumberField(blank=False, verbose_name='شماره همراه',region='IR')
    WorkNumber = models.CharField(blank=True, max_length=11, verbose_name='شماره محل کار', validators=[phone_regex])
    HomeNumber = models.CharField(blank=True, max_length=11, verbose_name='شماره منزل', validators=[phone_regex])

    SabegheVarzeshi = models.CharField(max_length=50, null=False, verbose_name='سابقه ورزشی')
    Height = models.IntegerField(null=False, verbose_name='قد')
    Weight = models.IntegerField(null=False, verbose_name='وزن')
    DaroyeKhas = models.TextField(max_length=200, null=False, verbose_name='مصرف دارو')
    SabegehBimari = models.TextField(max_length=200, null=True, verbose_name='سابقه بیماری')
    Paradox = models.TextField(max_length=200, null=True, verbose_name='ناهنجاری')

    #    job information

    MOJTAME = (
        ('s', 'سرچشمه'),
        ('b', 'شهربابک'),
        ('o', 'سوسنگرد'),

    )
    SEMAT = (
        ('m', 'مدیر'),
        ('o', 'معاون'),
        ('s', 'سرپرست'),
        ('k', 'کارشناس'),

    )
    Nesbat = models.CharField(max_length=1,
                              choices=list(NESBAT),
                              default='k',
                              verbose_name='نسبت',
                              help_text='نسبت شما به شخص کارمند'
                              )

    Mojtame = models.CharField(max_length=1,
                               choices=list(MOJTAME),
                               blank=True,
                               verbose_name='مجتمع',
                               help_text='محل کارا'
                               )
    Semat = models.CharField(max_length=1,
                             choices=list(SEMAT),
                             blank=True,
                             verbose_name='سمت',
                             help_text='سمت شغلی'
                             )
    PersonelNo = models.IntegerField(blank=True, verbose_name='شماره پرسنلی',
                                     help_text='شماره پرسنی خود و یا شخص کارمند')
    Omor = models.CharField(max_length=10, blank=True, verbose_name='امور')

    # Body result composition

    RESULT1 = (
        ('n', 'پایین'),
        ('l', 'نرمال'),
        ('u', 'بالا'),
        ('h', 'بسیار بالا'),
    )

    RESULT2 = (
        ('n', 'پایین'),
        ('l', 'نرمال'),
        ('u', 'بالا'),
    )

    RESULT3 = (
        ('l', 'نرمال'),
        ('u', 'بالا'),
    )

    Compo_date = models.DateField(verbose_name='تاریخ تست گرفتن')

    # body fat result
    BodyFat_w = models.CharField(max_length=1,
                                 choices=list(RESULT1),
                                 blank=True,
                                 verbose_name='میزان جاقی کل بدن',
                                 )

    BodyFat_t = models.CharField(max_length=1,
                                 choices=list(RESULT2),
                                 blank=True,
                                 verbose_name='میزان جاقی تنه',
                                 )

    BodyFat_a = models.CharField(max_length=1,
                                 choices=list(RESULT2),
                                 blank=True,
                                 verbose_name='میزان جاقی دست ها',
                                 )
    BodyFat_l = models.CharField(max_length=1,
                                 choices=list(RESULT2),
                                 blank=True,
                                 verbose_name='میزان جاقی پاها',
                                 )

    Bodyweight = models.IntegerField(null=True, verbose_name='وزن بدن با دستگاه')
    BMI = models.CharField(max_length=1,
                           choices=list(RESULT1),
                           blank=True,
                           verbose_name='شاخص توده بدنی',
                           )
    Bwater = models.CharField(max_length=1,
                              choices=list(RESULT2),
                              blank=True,
                              verbose_name='آب بدن',
                              )

    MuscleMass_w = models.CharField(max_length=1,
                                    choices=list(RESULT1),
                                    blank=True,
                                    verbose_name='میزان عضله کل بدن',
                                    )

    MuscleMass_t = models.CharField(max_length=1,
                                    choices=list(RESULT2),
                                    blank=True,
                                    verbose_name='میزان عضله تنه',
                                    )

    MuscleMass_a = models.CharField(max_length=1,
                                    choices=list(RESULT2),
                                    blank=True,
                                    verbose_name='میزان عضله دست ها',
                                    )
    MuscleMass_l = models.CharField(max_length=1,
                                    choices=list(RESULT2),
                                    blank=True,
                                    verbose_name='میزان عضله پاها',
                                    )
    Mage = models.IntegerField(null=True, verbose_name='سن متابولیک')
    LV = models.CharField(max_length=1,
                          choices=list(RESULT3),
                          blank=True,
                          verbose_name='چربی احشایی',
                          )
    Bone = models.IntegerField(null=True, verbose_name='استخوان')
    BMR = models.IntegerField(null=True, verbose_name='کالری پایه')
    MuscleQuality_w = models.CharField(max_length=1,
                                       choices=list(RESULT1),
                                       blank=True,
                                       verbose_name='کیفیت عضله کل بدن',
                                       )
    MuscleQuality_a = models.CharField(max_length=1,
                                       choices=list(RESULT2),
                                       blank=True,
                                       verbose_name='کیفیت عضله دست ها',
                                       )
    MuscleQuality_l = models.CharField(max_length=1,
                                       choices=list(RESULT2),
                                       blank=True,
                                       verbose_name='کیفیت عضله پاها',
                                       )


class ExerciseGroup(models.Model):
    class Meta:
        verbose_name = 'عضله'
        verbose_name_plural = 'عضله ها'
        # ordering = ['due_back']

    def __str__(self):
        return '{0}'.format(self.name)

    name = models.CharField(max_length=60, null=False, verbose_name='نام عضله')
    description = models.TextField(max_length=200, verbose_name='توضیحات عضله', null=True)


class Exercise(models.Model):
    class Meta:
        verbose_name = 'حرکت'
        verbose_name_plural = 'حرکت ها'
        # ordering = ['due_back']

    def __str__(self):
        return '{0} - {1} '.format(self.title, self.ExerciseGroups.name)

    title = models.CharField(max_length=60, null=False, verbose_name='عنوان حرکت')
    description = models.TextField(max_length=200, verbose_name='توضیحات حرکت', null=True)
    ExerciseGroups = models.ForeignKey('ExerciseGroup', on_delete=models.SET_NULL, null=True, verbose_name='عضله')
    video = models.FileField(validators=[validate_file_extension],
                             upload_to='media/videos/exercise/',
                             verbose_name='ویدو حرکت',
                             null=True)


class FoodPrograming(models.Model):
    pdf = models.FileField(validators=[validate_file_pdf],
                           upload_to='media/pdf/exercise/',
                           verbose_name='فایل برنامه غذایی',
                           null=True)

    # date = models.DateField(_("Date"), auto_now_add=True)
    FoodDate = models.DateField(default=date.today, verbose_name='تاریخ برنامه')
    PersonInfo = models.ForeignKey('PersonInfo', on_delete=models.SET_NULL, null=True, verbose_name='شخص وزش کار')

    class Meta:
        verbose_name = 'برنامه غذایی'
        verbose_name_plural = 'برنامه های غذایی'
        # ordering = ['due_back']

    def __str__(self):
        return '{0} - {1} '.format(self.PersonInfo, self.FoodDate)


class PersonExercise(models.Model):
    DATEWEEK = (
        (0, 'شنبه'),
        (1, 'یک شنبه'),
        (2, 'دو شنبه'),
        (3, 'سه شنبه'),
        (4, 'چهار شنبه'),
        (5, 'پنج شنبه'),
        (6, 'جمعه'),
    )

    MY_CHOICES2 = ((1, 'Item title 2.1'),
                   (2, 'Item title 2.2'),
                   (3, 'Item title 2.3'),
                   (4, 'Item title 2.4'),
                   (5, 'Item title 2.5'))

    Exercise = models.ForeignKey('Exercise', on_delete=models.CASCADE, null=True, verbose_name='حرکت ورزشی')
    PersonInfo = models.ForeignKey('PersonInfo', on_delete=models.CASCADE, null=True, verbose_name='شخص وزش کار')
    ZamanEsterahat = models.IntegerField(default=30, help_text='زمان استراحت', verbose_name='زمان استراحت')
    TedadSet = models.IntegerField(default=3, verbose_name='تعداد ست')
    TedadTekrar = models.IntegerField(default=7, verbose_name='تعداد تکرار')
    ShomareHarkat = models.IntegerField(default=1, verbose_name='شماره حرکت')
    # DateWeek = models.CharField(max_length=6,
    #                             choices=list(DATEWEEK),
    #                             blank=True,
    #                             verbose_name='روز هفته',
    #                             )

    DateWeek = MultiSelectField(choices=DATEWEEK,
                                default=(0, 3),
                                max_length=7,
                                max_choices=7,
                                verbose_name='روز های تکرار')

    class Meta:
        verbose_name = 'برنامه ورزشی فردی'
        verbose_name_plural = 'برنامه ورزشی فردی'
        # ordering = ['due_back']

    def __str__(self):
        return '{0} - {1} - '.format(self.PersonInfo, self.Exercise)

# Create your models here.
#
# class Genre(models.Model):
#     name = models.CharField(max_length=60, verbose_name='ژانر')
#     created = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.name
#     class Meta:
#         verbose_name = 'ژانر کتاب'
#         verbose_name_plural = 'ژانر کتاب ها'
#
#
#
# class Language(models.Model):
#     name = models.CharField(max_length=60, verbose_name='زبان')
#     created = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'زبان کتاب'
#         verbose_name_plural = 'زبان کتاب ها'
#
#
#
#
#
#
# class BookHome(models.Model):
#     name = models.CharField(max_length=60, verbose_name='کتابخانه')
#     created = models.DateTimeField(auto_now_add=True)
#
#
#
#
# class Book(models.Model):
#     title = models.CharField(max_length=60, verbose_name='عنوان کتاب')
#     Author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True,verbose_name='نویسنده')
#     Summary = models.TextField(max_length=500, verbose_name='توضیحات کتاب ')
#     Genre = models.ManyToManyField(Genre,verbose_name='ژانر کتاب')
#     bookHome = models.ForeignKey('bookHome', on_delete=models.SET_NULL, null=True)
#     bookparent = models.ForeignKey('book', on_delete=models.SET_NULL, null=True)
#
#     class Meta:
#         verbose_name = 'کتاب'
#         verbose_name_plural = 'کتاب ها'
#     def __str__(self):
#         return "{} - {} {}".format(self.title,self.Author.first_name , self.Author.last_name)
#
#
#
#
#
# class BookInstance(models.Model):
#     id = models.UUIDField(primary_key=True,
#                           default=uuid.uuid4,
#                           help_text='unique id for this book')
#     book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
#     borrower = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
#     imprint = models.CharField(max_length=200)
#     file = models.FileField(upload_to="uploads/image/",blank=True,null=True)
#     due_back = models.DateField(null=True, blank=True)
#     LON_STATUS = (
#         ('m', 'Maintenance'),
#         ('o', 'on Loan'),
#         ('a', 'Available'),
#         ('r', 'Reserve'),
#     )
#
#
#     status = models.CharField(max_length=4,
#                               choices=list(LON_STATUS),
#                               blank=True,
#
#
#                               help_text='Book availability')
#
#     class Meta:
#         verbose_name = 'جلد کتاب'
#         verbose_name_plural = 'جلد کتاب ها'
#         ordering = ['due_back']
#
#     def __str__(self):
#         return '{0} ({1})'.format(self.id, self.book.title)
#
#
# class Author(models.Model):
#     first_name = models.CharField(max_length=60, verbose_name='نام نویسنده')
#     last_name = models.CharField(max_length=60, verbose_name='فامیل نویسنده')
#     DateOfBart = models.DateTimeField(verbose_name='تاریخ تولد')
#     DateOfDeath = models.DateTimeField(verbose_name='تاریخ رفات')
#
#     # Books = models.ManyToManyField(Book)
#
#     class Meta:
#         ordering = ['first_name', 'last_name']
#         verbose_name = 'نویسنده'
#         verbose_name_plural = 'نویسنده ها'
#
#         return "{} {}".format(self.first_name, self.last_name)
#     def __str__(self):

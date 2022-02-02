from django.contrib import admin
#
# # Register your models here.

from .models import PersonInfo
from .models import ExerciseGroup
from .models import Exercise
from .models import PersonExercise
from .models import FoodPrograming

from django import forms

class ExerciseInstanceInline(admin.TabularInline):
    model = Exercise
    
class PersonExerciseInstanceInline(admin.TabularInline):
    model = PersonExercise
    
class FoodProgramingInstanceInline(admin.TabularInline):
    model = FoodPrograming

@admin.register(ExerciseGroup)
class ExerciseGroup(admin.ModelAdmin):
    list_filter = ('name', 'description')
    inlines = [ExerciseInstanceInline]


@admin.register(Exercise)
class Exercise(admin.ModelAdmin):
    list_filter = ('title', 'description')


# admin.site.register(PersonelNo)
@admin.register(PersonInfo)
class PersonInfo(admin.ModelAdmin):
    prepopulated_fields = {'Username':('phoneNumber',),
                           'Password':('NationalCode',),

                           }

    widgets = {
        'Password': forms.PasswordInput(),
    }
    inlines = [FoodProgramingInstanceInline,PersonExerciseInstanceInline]
 
    list_filter = ('DateOfBart', 'FirstName')
    fieldsets = (
        (None, {
            'fields': [
                ('FirstName',
                 'LastName',
                 'FatherName',
                 'Sex',
                 'DateOfBart',
                 )
            ]
        }),
        (None, {
            'fields': [
                (
                    'bloodType',
                    'NationalCode',
                    'ShenasnameCode',
                    'MohaleSedor',
                    'VazyateTahol',
                   
                )
            ]

        }),
        ('اطلاعات تماسی', {
            'fields': [
                (
                    'Address',
                    'phoneNumber',
                    'WorkNumber',
                    'HomeNumber',
                )
            ]

        }),
        ('اطلاعات ورود به برنامه همراه', {
            'fields': [
                (
                    'Username',
                    'Password',
                )
            ]

        }),
        ('اطلاعات بدنی', {
            'fields': [
                (
                    'DaroyeKhas',
                    'SabegheVarzeshi',
                    'Height',
                    'Weight',
                    'SabegehBimari',
                    'Paradox',
                )
            ]

        }),
        ('اطلاعات شغلی(در صورت کارمند نبودن فقط نسبت را مشخص کنید)', {
            'fields': [
                (
                    'Nesbat',
                    'PersonelNo',
                    'Mojtame',
                    'Semat',
                    'Omor',
                )
            ]

        }),
        ('خورجی دستگاه آنالیز بدن', {
            'fields': [
                (
                    'Compo_date',
                    'Bodyweight',
                    'Mage',
                    'Bone',
                    'BMR',
                ),
                (
                    'BMI',
                    'Bwater',
                    'LV',
                ),
                (
                    'BodyFat_w',
                    'BodyFat_t',
                    'BodyFat_a',
                    'BodyFat_l',
                ),
                (
                    'MuscleMass_w',
                    'MuscleMass_t',
                    'MuscleMass_a',
                    'MuscleMass_l',
                ),
                (
                    'MuscleQuality_w',
                    'MuscleQuality_a',
                    'MuscleQuality_l',
                ),

            ]
        }),
        
    )

# from .models import Author
# from .models import Language
# from .models import Genre
# from .models import Book
# from .models import BookInstance
# from .models import BookHome
#
# # admin.site.register(BookHome)
# admin.site.register(Language)
# admin.site.register(Genre)
#
#
# # admin.site.register(Book)
# admin.site.register(BookInstance)
# #
# class BookInstanceInline(admin.TabularInline):
#     model = BookInstance
#
#
# class BookHomeInline(admin.TabularInline):
#     model = Book
#
#
#
# @admin.register(Author)
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'DateOfBart', 'DateOfDeath')
#
#
#
#
# @admin.register(BookHome)
# class BookHomeAdmin(admin.ModelAdmin):
#     list_display = ('name','created')
#     inlines = [BookHomeInline]
#
#
#
# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     inlines = [BookInstanceInline]
#     list_display = ('title', 'Author', 'display_genre','bookHome','bookparent')
#     list_filter = ('Genre', 'title', 'Author')
#     fieldsets = (
#         (None, {
#             'fields': [
#                 ('title',
#                  'Summary',
#                  'bookHome',
#                  'bookparent')
#             ]
#         }),
#         ('اطلاعات کتاب', {
#             'fields': [
#                 ('Author',
#                  'Genre',
#                  )
#             ]
#
#         }
#
#          )
#     )
#
#
#
#     def display_genre(self, obj):
#         return ', '.join([genre.name for genre in obj.Genre.all()[:3]])
#

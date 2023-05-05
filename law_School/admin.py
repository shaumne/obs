from django.contrib import admin
from .models.contracts import Contracts
from .models.corporate_law import Corporate_Law
from .models.criminal_law_and_procedure import Criminal_Law_And_Procedure
from .models.environmental_law import Environmental_Law
from .models.family_law import Family_Law
from .models.intellectual_property import Intellectual_Property
from .models.international_law import International_Law
from .models.labor_law import Labor_Law
from .models.legal_profession import Legal_Profession
from .models.legislation_and_regulation import Legislation_And_Regulation
from .models.property import Property
from .models.taxation import Taxation
from .models.torts import Torts
from .models.civil_procedure import Civil_Procedure
from .models.constitutional_law import Constitutional_Law

# Register your models here.
admin.site.register([Contracts, 
                     Corporate_Law, 
                     Criminal_Law_And_Procedure, 
                     Environmental_Law, 
                     Family_Law, 
                     Intellectual_Property, 
                     International_Law, 
                     Labor_Law, 
                     Legal_Profession, 
                     Legislation_And_Regulation, 
                     Property, 
                     Taxation, 
                     Torts, 
                     Civil_Procedure, 
                     Constitutional_Law])
from django.contrib import admin
from .models.genetics_and_genomics import Genetics_And_Genomics
from .models.human_anatomy_and_development import Human_Anatomy_And_Development
from .models.human_physiology import Human_Physiology
from .models.immunology import Immunology
from .models.medical_biochemistry import Medical_Biochemistry
from .models.pharmacology_and_therapeutics import Pharmacology_And_Therapeutics
from .models.social_and_ethical_issues_in_medicine import Social_And_Ethical_Issues_In_Medicine
from .models.pathways_mechanisms_and_models_of_human_disease import Pathways_Mechanisms_And_Models_Of_Human_Disease

# Register your models here.
admin.site.register([
    Genetics_And_Genomics,
    Human_Anatomy_And_Development,
    Human_Physiology,
    Immunology,
    Pathways_Mechanisms_And_Models_Of_Human_Disease,
    Social_And_Ethical_Issues_In_Medicine,
    Pharmacology_And_Therapeutics,
    Medical_Biochemistry
])
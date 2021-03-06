# Generated by Django 3.2 on 2021-04-07 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ccsFormData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientNumber', models.CharField(blank=True, max_length=9)),
                ('title', models.CharField(blank=True, max_length=40)),
                ('firstName', models.CharField(blank=True, max_length=40)),
                ('lastName', models.CharField(blank=True, max_length=40)),
                ('firstNameNOTsame', models.CharField(blank=True, max_length=40)),
                ('lastNameNOTsame', models.CharField(blank=True, max_length=40)),
                ('nameOtherKnown', models.CharField(blank=True, max_length=40)),
                ('namePrefer', models.CharField(blank=True, max_length=40)),
                ('dob', models.DateField(null=True)),
                ('gender', models.CharField(blank=True, max_length=40)),
                ('irdNumber', models.CharField(blank=True, max_length=40)),
                ('flatHouseNum', models.CharField(blank=True, max_length=40)),
                ('streetName', models.CharField(blank=True, max_length=40)),
                ('suburb', models.CharField(blank=True, max_length=40)),
                ('townCity', models.CharField(blank=True, max_length=40)),
                ('mailingAddr', models.CharField(blank=True, max_length=40)),
                ('homePhone', models.CharField(blank=True, max_length=40)),
                ('mobPhone', models.CharField(blank=True, max_length=40)),
                ('otherPhone', models.CharField(blank=True, max_length=40)),
                ('getEmails', models.CharField(blank=True, max_length=40)),
                ('ethnicity', models.CharField(blank=True, max_length=40)),
                ('usuallyNZ', models.CharField(blank=True, max_length=40)),
                ('residenceStatus', models.CharField(blank=True, max_length=40)),
                ('dateGranted', models.DateField(null=True)),
                ('dateArrived', models.DateField(null=True)),
                ('countryOfBirth', models.CharField(blank=True, max_length=40)),
                ('ccAssistanceReason', models.CharField(blank=True, max_length=40)),
                ('isWorking', models.CharField(blank=True, max_length=40)),
                ('employerName', models.CharField(blank=True, max_length=40)),
                ('employerAddr', models.CharField(blank=True, max_length=40)),
                ('employerPhone', models.CharField(blank=True, max_length=40)),
                ('hoursPerWeek', models.CharField(blank=True, max_length=40)),
                ('hoursTravel', models.CharField(blank=True, max_length=40)),
                ('isWorkRelatedCourse', models.CharField(blank=True, max_length=40)),
                ('trainingOrgName', models.CharField(blank=True, max_length=40)),
                ('trainingOrgAddr', models.CharField(blank=True, max_length=40)),
                ('trainingOrgPhone', models.CharField(blank=True, max_length=40)),
                ('trainingOrgFaxEmail', models.CharField(blank=True, max_length=40)),
                ('employerFaxEmail', models.CharField(blank=True, max_length=40)),
                ('nameOfCourse', models.CharField(blank=True, max_length=40)),
                ('isNZQA', models.CharField(blank=True, max_length=40)),
                ('courseStartDate', models.DateField(null=True)),
                ('courseEndDate', models.DateField(null=True)),
                ('courseHoursPerWeek', models.CharField(blank=True, max_length=40)),
                ('otherStudyHoursPerWeek', models.CharField(blank=True, max_length=40)),
                ('hoursTravelCCtoCourse', models.CharField(blank=True, max_length=40)),
                ('isArrangedActivities', models.CharField(blank=True, max_length=40)),
                ('activityType', models.CharField(blank=True, max_length=40)),
                ('hoursActivity', models.CharField(blank=True, max_length=40)),
                ('hoursTravelCCtoActivity', models.CharField(blank=True, max_length=40)),
                ('applyForMedicalReasons', models.CharField(blank=True, max_length=40)),
                ('medicalDurationExpected', models.CharField(blank=True, max_length=40)),
                ('hoursPerWeekNeedCC', models.CharField(blank=True, max_length=40)),
                ('incomeWagesSalary', models.CharField(blank=True, max_length=40)),
                ('incomePPL', models.CharField(blank=True, max_length=40)),
                ('terminationPay', models.CharField(blank=True, max_length=40)),
                ('redundancyPay', models.CharField(blank=True, max_length=40)),
                ('acc', models.CharField(blank=True, max_length=40)),
                ('incomeInsurance', models.CharField(blank=True, max_length=40)),
                ('incomeBusiness', models.CharField(blank=True, max_length=40)),
                ('incomeSelfEmpContract', models.CharField(blank=True, max_length=40)),
                ('incomeInterest', models.CharField(blank=True, max_length=40)),
                ('incomeDividends', models.CharField(blank=True, max_length=40)),
                ('incomeRental', models.CharField(blank=True, max_length=40)),
                ('incomeFlatmates', models.CharField(blank=True, max_length=40)),
                ('incomeChildSup', models.CharField(blank=True, max_length=40)),
                ('incomeOtherForChild', models.CharField(blank=True, max_length=40)),
                ('incomeMaintenance', models.CharField(blank=True, max_length=40)),
                ('incomeFormerPartner', models.CharField(blank=True, max_length=40)),
                ('incomeStudentAllowance', models.CharField(blank=True, max_length=40)),
                ('incomeOverseasPension', models.CharField(blank=True, max_length=40)),
                ('incomeSuper', models.CharField(blank=True, max_length=40)),
                ('incomeEstate', models.CharField(blank=True, max_length=40)),
                ('incomeTrusts', models.CharField(blank=True, max_length=40)),
                ('incomeOther', models.CharField(blank=True, max_length=40)),
                ('jointPartnerWhere1', models.CharField(blank=True, max_length=40)),
                ('jointPartnerWith1', models.CharField(blank=True, max_length=40)),
                ('jointPartnerYou1', models.CharField(blank=True, max_length=40)),
                ('jointPartnerFreq1', models.CharField(blank=True, max_length=40)),
                ('jointPartnerWhere2', models.CharField(blank=True, max_length=40)),
                ('jointPartnerWith2', models.CharField(blank=True, max_length=40)),
                ('jointPartnerYou2', models.CharField(blank=True, max_length=40)),
                ('jointPartnerFreq2', models.CharField(blank=True, max_length=40)),
                ('jointPartnerWhere3', models.CharField(blank=True, max_length=40)),
                ('jointPartnerWith3', models.CharField(blank=True, max_length=40)),
                ('jointPartnerYou3', models.CharField(blank=True, max_length=40)),
                ('jointPartnerFreq3', models.CharField(blank=True, max_length=40)),
                ('jointPartnerWhere4', models.CharField(blank=True, max_length=40)),
                ('jointPartnerWith4', models.CharField(blank=True, max_length=40)),
                ('jointPartnerYou4', models.CharField(blank=True, max_length=40)),
                ('jointPartnerFreq4', models.CharField(blank=True, max_length=40)),
                ('jointPartnerWhere5', models.CharField(blank=True, max_length=40)),
                ('jointPartnerWith5', models.CharField(blank=True, max_length=40)),
                ('jointPartnerYou5', models.CharField(blank=True, max_length=40)),
                ('jointPartnerFreq5', models.CharField(blank=True, max_length=40)),
                ('other52weeksType1', models.CharField(blank=True, max_length=40)),
                ('other52weeksWhere1', models.CharField(blank=True, max_length=40)),
                ('other52weeksValue1', models.CharField(blank=True, max_length=40)),
                ('other52weeksType2', models.CharField(blank=True, max_length=40)),
                ('other52weeksWhere2', models.CharField(blank=True, max_length=40)),
                ('other52weeksValue2', models.CharField(blank=True, max_length=40)),
                ('other52weeksType3', models.CharField(blank=True, max_length=40)),
                ('other52weeksWhere3', models.CharField(blank=True, max_length=40)),
                ('other52weeksValue3', models.CharField(blank=True, max_length=40)),
                ('other52weeksType4', models.CharField(blank=True, max_length=40)),
                ('other52weeksWhere4', models.CharField(blank=True, max_length=40)),
                ('other52weeksValue4', models.CharField(blank=True, max_length=40)),
                ('other52weeksType5', models.CharField(blank=True, max_length=40)),
                ('other52weeksWhere5', models.CharField(blank=True, max_length=40)),
                ('other52weeksValue5', models.CharField(blank=True, max_length=40)),
                ('childFullName_1', models.CharField(blank=True, max_length=40)),
                ('childDOB_1', models.DateField(null=True)),
                ('childRelationToYou_1', models.CharField(blank=True, max_length=40)),
                ('childFullName_2', models.CharField(blank=True, max_length=40)),
                ('childDOB_2', models.DateField(null=True)),
                ('childRelationToYou_2', models.CharField(blank=True, max_length=40)),
                ('childFullName_3', models.CharField(blank=True, max_length=40)),
                ('childDOB_3', models.DateField(null=True)),
                ('childRelationToYou_3', models.CharField(blank=True, max_length=40)),
                ('childFullName_4', models.CharField(blank=True, max_length=40)),
                ('childDOB_4', models.DateField(null=True)),
                ('childRelationToYou_4', models.CharField(blank=True, max_length=40)),
                ('childFullName_5', models.CharField(blank=True, max_length=40)),
                ('childDOB_5', models.DateField(null=True)),
                ('childRelationToYou_5', models.CharField(blank=True, max_length=40)),
                ('Child_ECE_ChildName_1', models.CharField(blank=True, max_length=40)),
                ('Child_ECE_Provider_1', models.CharField(blank=True, max_length=40)),
                ('Child_ECE_WeekTotal_1', models.CharField(blank=True, max_length=40)),
                ('Child_ECE_StartDate_1', models.DateField(null=True)),
                ('Child_ECE_ChildName_2', models.CharField(blank=True, max_length=40)),
                ('Child_ECE_Provider_2', models.CharField(blank=True, max_length=40)),
                ('Child_ECE_WeekTotal_2', models.CharField(blank=True, max_length=40)),
                ('Child_ECE_StartDate_2', models.DateField(null=True)),
                ('Child_ECE_ChildName_3', models.CharField(blank=True, max_length=40)),
                ('Child_ECE_Provider_3', models.CharField(blank=True, max_length=40)),
                ('Child_ECE_WeekTotal_3', models.CharField(blank=True, max_length=40)),
                ('Child_ECE_StartDate_3', models.DateField(null=True)),
                ('Child_ECE_ChildName_4', models.CharField(blank=True, max_length=40)),
                ('Child_ECE_Provider_4', models.CharField(blank=True, max_length=40)),
                ('Child_ECE_WeekTotal_4', models.CharField(blank=True, max_length=40)),
                ('Child_ECE_StartDate_4', models.DateField(null=True)),
                ('whichChildCCS_1', models.CharField(blank=True, max_length=40)),
                ('whichChildCCS_2', models.CharField(blank=True, max_length=40)),
                ('whichChildCCS_3', models.CharField(blank=True, max_length=40)),
                ('whichChildCCS_4', models.CharField(blank=True, max_length=40)),
                ('whichChildOSCAR_1', models.CharField(blank=True, max_length=40)),
                ('whichChildOSCAR_2', models.CharField(blank=True, max_length=40)),
                ('whichChildOSCAR_3', models.CharField(blank=True, max_length=40)),
                ('whichChildOSCAR_4', models.CharField(blank=True, max_length=40)),
                ('understandRelationship', models.CharField(blank=True, max_length=40)),
                ('hasPartner', models.CharField(blank=True, max_length=40)),
                ('partnerFullName', models.CharField(blank=True, max_length=40)),
                ('partnerDOB', models.DateField(null=True)),
                ('relationshipStatus', models.CharField(blank=True, max_length=40)),
                ('p_clientNumber', models.CharField(blank=True, max_length=9)),
                ('p_title', models.CharField(blank=True, max_length=40)),
                ('p_firstName', models.CharField(blank=True, max_length=40)),
                ('p_lastName', models.CharField(blank=True, max_length=40)),
                ('p_firstNameNOTsame', models.CharField(blank=True, max_length=40)),
                ('p_lastNameNOTsame', models.CharField(blank=True, max_length=40)),
                ('p_nameOtherKnown', models.CharField(blank=True, max_length=40)),
                ('p_namePrefer', models.CharField(blank=True, max_length=40)),
                ('p_dob', models.DateField(null=True)),
                ('p_gender', models.CharField(blank=True, max_length=40)),
                ('p_irdNumber', models.CharField(blank=True, max_length=40)),
                ('p_flatHouseNum', models.CharField(blank=True, max_length=40)),
                ('p_streetName', models.CharField(blank=True, max_length=40)),
                ('p_suburb', models.CharField(blank=True, max_length=40)),
                ('p_townCity', models.CharField(blank=True, max_length=40)),
                ('p_mailingAddr', models.CharField(blank=True, max_length=40)),
                ('p_homePhone', models.CharField(blank=True, max_length=40)),
                ('p_mobPhone', models.CharField(blank=True, max_length=40)),
                ('p_otherPhone', models.CharField(blank=True, max_length=40)),
                ('p_getEmails', models.CharField(blank=True, max_length=40)),
                ('p_ethnicity', models.CharField(blank=True, max_length=40)),
                ('p_usuallyNZ', models.CharField(blank=True, max_length=40)),
                ('p_residenceStatus', models.CharField(blank=True, max_length=40)),
                ('p_dateGranted', models.DateField(null=True)),
                ('p_dateArrived', models.DateField(null=True)),
                ('p_countryOfBirth', models.CharField(blank=True, max_length=40)),
                ('p_ccAssistanceReason', models.CharField(blank=True, max_length=40)),
                ('p_isWorking', models.CharField(blank=True, max_length=40)),
                ('p_employerName', models.CharField(blank=True, max_length=40)),
                ('p_employerAddr', models.CharField(blank=True, max_length=40)),
                ('p_employerPhone', models.CharField(blank=True, max_length=40)),
                ('p_hoursPerWeek', models.CharField(blank=True, max_length=40)),
                ('p_hoursTravel', models.CharField(blank=True, max_length=40)),
                ('p_isWorkRelatedCourse', models.CharField(blank=True, max_length=40)),
                ('p_trainingOrgName', models.CharField(blank=True, max_length=40)),
                ('p_trainingOrgAddr', models.CharField(blank=True, max_length=40)),
                ('p_trainingOrgPhone', models.CharField(blank=True, max_length=40)),
                ('p_trainingOrgFaxEmail', models.CharField(blank=True, max_length=40)),
                ('p_employerFaxEmail', models.CharField(blank=True, max_length=40)),
                ('p_nameOfCourse', models.CharField(blank=True, max_length=40)),
                ('p_isNZQA', models.CharField(blank=True, max_length=40)),
                ('p_courseStartDate', models.DateField(null=True)),
                ('p_courseEndDate', models.DateField(null=True)),
                ('p_courseHoursPerWeek', models.CharField(blank=True, max_length=40)),
                ('p_otherStudyHoursPerWeek', models.CharField(blank=True, max_length=40)),
                ('p_hoursTravelCCtoCourse', models.CharField(blank=True, max_length=40)),
                ('p_isArrangedActivities', models.CharField(blank=True, max_length=40)),
                ('p_activityType', models.CharField(blank=True, max_length=40)),
                ('p_hoursActivity', models.CharField(blank=True, max_length=40)),
                ('p_hoursTravelCCtoActivity', models.CharField(blank=True, max_length=40)),
                ('p_applyForMedicalReasons', models.CharField(blank=True, max_length=40)),
                ('p_medicalDurationExpected', models.CharField(blank=True, max_length=40)),
                ('p_hoursPerWeekNeedCC', models.CharField(blank=True, max_length=40)),
                ('p_incomeWagesSalary', models.CharField(blank=True, max_length=40)),
                ('p_incomePPL', models.CharField(blank=True, max_length=40)),
                ('p_terminationPay', models.CharField(blank=True, max_length=40)),
                ('p_redundancyPay', models.CharField(blank=True, max_length=40)),
                ('p_acc', models.CharField(blank=True, max_length=40)),
                ('p_incomeInsurance', models.CharField(blank=True, max_length=40)),
                ('p_incomeBusiness', models.CharField(blank=True, max_length=40)),
                ('p_incomeSelfEmpContract', models.CharField(blank=True, max_length=40)),
                ('p_incomeInterest', models.CharField(blank=True, max_length=40)),
                ('p_incomeDividends', models.CharField(blank=True, max_length=40)),
                ('p_incomeRental', models.CharField(blank=True, max_length=40)),
                ('p_incomeFlatmates', models.CharField(blank=True, max_length=40)),
                ('p_incomeChildSup', models.CharField(blank=True, max_length=40)),
                ('p_incomeOtherForChild', models.CharField(blank=True, max_length=40)),
                ('p_incomeMaintenance', models.CharField(blank=True, max_length=40)),
                ('p_incomeFormerPartner', models.CharField(blank=True, max_length=40)),
                ('p_incomeStudentAllowance', models.CharField(blank=True, max_length=40)),
                ('p_incomeOverseasPension', models.CharField(blank=True, max_length=40)),
                ('p_incomeSuper', models.CharField(blank=True, max_length=40)),
                ('p_incomeEstate', models.CharField(blank=True, max_length=40)),
                ('p_incomeTrusts', models.CharField(blank=True, max_length=40)),
                ('p_incomeOther', models.CharField(blank=True, max_length=40)),
                ('p_jointPartnerWhere1', models.CharField(blank=True, max_length=40)),
                ('p_jointPartnerWith1', models.CharField(blank=True, max_length=40)),
                ('p_jointPartnerYou1', models.CharField(blank=True, max_length=40)),
                ('p_jointPartnerFreq1', models.CharField(blank=True, max_length=40)),
                ('p_jointPartnerWhere2', models.CharField(blank=True, max_length=40)),
                ('p_jointPartnerWith2', models.CharField(blank=True, max_length=40)),
                ('p_jointPartnerYou2', models.CharField(blank=True, max_length=40)),
                ('p_jointPartnerFreq2', models.CharField(blank=True, max_length=40)),
                ('p_jointPartnerWhere3', models.CharField(blank=True, max_length=40)),
                ('p_jointPartnerWith3', models.CharField(blank=True, max_length=40)),
                ('p_jointPartnerYou3', models.CharField(blank=True, max_length=40)),
                ('p_jointPartnerFreq3', models.CharField(blank=True, max_length=40)),
                ('p_jointPartnerWhere4', models.CharField(blank=True, max_length=40)),
                ('p_jointPartnerWith4', models.CharField(blank=True, max_length=40)),
                ('p_jointPartnerYou4', models.CharField(blank=True, max_length=40)),
                ('p_jointPartnerFreq4', models.CharField(blank=True, max_length=40)),
                ('p_jointPartnerWhere5', models.CharField(blank=True, max_length=40)),
                ('p_jointPartnerWith5', models.CharField(blank=True, max_length=40)),
                ('p_jointPartnerYou5', models.CharField(blank=True, max_length=40)),
                ('p_jointPartnerFreq5', models.CharField(blank=True, max_length=40)),
                ('p_other52weeksType1', models.CharField(blank=True, max_length=40)),
                ('p_other52weeksWhere1', models.CharField(blank=True, max_length=40)),
                ('p_other52weeksValue1', models.CharField(blank=True, max_length=40)),
                ('p_other52weeksType2', models.CharField(blank=True, max_length=40)),
                ('p_other52weeksWhere2', models.CharField(blank=True, max_length=40)),
                ('p_other52weeksValue2', models.CharField(blank=True, max_length=40)),
                ('p_other52weeksType3', models.CharField(blank=True, max_length=40)),
                ('p_other52weeksWhere3', models.CharField(blank=True, max_length=40)),
                ('p_other52weeksValue3', models.CharField(blank=True, max_length=40)),
                ('p_other52weeksType4', models.CharField(blank=True, max_length=40)),
                ('p_other52weeksWhere4', models.CharField(blank=True, max_length=40)),
                ('p_other52weeksValue4', models.CharField(blank=True, max_length=40)),
                ('p_other52weeksType5', models.CharField(blank=True, max_length=40)),
                ('p_other52weeksWhere5', models.CharField(blank=True, max_length=40)),
                ('p_other52weeksValue5', models.CharField(blank=True, max_length=40)),
            ],
        ),
    ]

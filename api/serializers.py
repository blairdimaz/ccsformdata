from rest_framework import serializers
from .models import ccsFormData

class ccsSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = ccsFormData
        fields = ['id',
                  'clientNumber',
                  'firstName','lastName',
                  'firstNameNOTsame', 'lastNameNOTsame',
                  'nameOtherKnown' ,
                  'dob',
                  'gender',
                  'irdNumber',
                  'flatHouseNum',
                  'streetName',
                  'suburb',
                  'townCity',
                  'mailingAddr',
                  'homePhone',
                  'mobPhone',
                  'otherPhone',
                  'getEmails',
                  'ethnicity',
                  'usuallyNZ',
                  'residenceStatus',
                  'dateGranted',
                  'dateArrived',
                  'countryOfBirth',
                  'ccAssistanceReason',
                  'isWorking',
                  'employerName',
                  'employerAddr',
                  'employerPhone',
                  'employerFaxEmail',
                  'hoursPerWeek',
                  'hoursTravel',
                  'isWorkRelatedCourse',
                  'trainingOrgName',
                  'trainingOrgAddr',
                  'trainingOrgPhone',
                  'trainingOrgFaxEmail',
                  'employerFaxEmail',
                  'nameOfCourse',
                  'isNZQA',
                  'courseStartDate',
                  'courseEndDate',
                  'courseHoursPerWeek',
                  'otherStudyHoursPerWeek',
                  'hoursTravelCCtoCourse',
                  'isArrangedActivities',
                  'activityType',
                  'hoursActivity',
                  'hoursTravelCCtoActivity',
                  'applyForMedicalReasons',
                  'medicalDurationExpected',
                  'hoursPerWeekNeedCC',
                  'incomeWagesSalary',
                  'incomePPL',
                  'terminationPay',
                  'redundancyPay',
                  'acc',
                  'incomeInsurance',
                  'incomeBusiness',
                  'incomeSelfEmpContract',
                  'incomeInterest',
                  'incomeDividends',
                  'incomeRental',
                  'incomeFlatmates',
                  'incomeChildSup',
                  'incomeOtherForChild',
                  'incomeMaintenance',
                  'incomeFormerPartner',
                  'incomeStudentAllowance',
                  'incomeOverseasPension',
                  'incomeSuper',
                  'incomeEstate',
                  'incomeTrusts',
                  'incomeOther',
                  'jointPartnerWhere1',
                  'jointPartnerWith1',
                  'jointPartnerYou1',
                  'jointPartnerFreq1',
                  'jointPartnerWhere2',
                  'jointPartnerWith2',
                  'jointPartnerYou2',
                  'jointPartnerFreq2',
                  'jointPartnerWhere3',
                  'jointPartnerWith3',
                  'jointPartnerYou3',
                  'jointPartnerFreq3',
                  'jointPartnerWhere4',
                  'jointPartnerWith4',
                  'jointPartnerYou4',
                  'jointPartnerFreq4',
                  'jointPartnerWhere5',
                  'jointPartnerWith5',
                  'jointPartnerYou5',
                  'jointPartnerFreq5',
                  'other52weeksType1',
                  'other52weeksWhere1',
                  'other52weeksValue1',
                  'other52weeksType2',
                  'other52weeksWhere2',
                  'other52weeksValue2',
                  'other52weeksType3',
                  'other52weeksWhere3',
                  'other52weeksValue3',
                  'other52weeksType4',
                  'other52weeksWhere4',
                  'other52weeksValue4',
                  'other52weeksType5',
                  'other52weeksWhere5',
                  'other52weeksValue5',
                  'childFullName_1',
                  'childDOB_1',
                  'childRelationToYou_1',
                  'childFullName_2',
                  'childDOB_2',
                  'childRelationToYou_2',
                  'childFullName_3',
                  'childDOB_3',
                  'childRelationToYou_3',
                  'childFullName_4',
                  'childDOB_4',
                  'childRelationToYou_4',
                  'childFullName_5',
                  'childDOB_5',
                  'childRelationToYou_5',
                  'Child_ECE_ChildName_1',
                  'Child_ECE_Provider_1',
                  'Child_ECE_WeekTotal_1',
                  'Child_ECE_StartDate_1',

                  'Child_ECE_ChildName_2',
                  'Child_ECE_Provider_2',
                  'Child_ECE_WeekTotal_2',
                  'Child_ECE_StartDate_2',

                  'Child_ECE_ChildName_3',
                  'Child_ECE_Provider_3',
                  'Child_ECE_WeekTotal_3',
                  'Child_ECE_StartDate_3',

                  'Child_ECE_ChildName_4',
                  'Child_ECE_Provider_4',
                  'Child_ECE_WeekTotal_4',
                  'Child_ECE_StartDate_4',

                  'whichChildCCS_1',
                  'whichChildCCS_2',
                  'whichChildCCS_3',
                  'whichChildCCS_4',

                  'whichChildOSCAR_1',
                  'whichChildOSCAR_2',
                  'whichChildOSCAR_3',
                  'whichChildOSCAR_4',

                  'understandRelationship',
                  'hasPartner',
                  'partnerFullName',
                  'partnerDOB',
                  'relationshipStatus',
                  'p_clientNumber',
                  'p_firstName', 'p_lastName',
                  'p_firstNameNOTsame', 'p_lastNameNOTsame',
                  'p_nameOtherKnown',
                  'p_dob',
                  'p_gender',
                  'p_irdNumber',
                  'p_flatHouseNum',
                  'p_streetName',
                  'p_suburb',
                  'p_townCity',
                  'p_mailingAddr',
                  'p_homePhone',
                  'p_mobPhone',
                  'p_otherPhone',
                  'p_getEmails',
                  'p_ethnicity',
                  'p_usuallyNZ',
                  'p_residenceStatus',
                  'p_dateGranted',
                  'p_dateArrived',
                  'p_countryOfBirth',
                  'p_ccAssistanceReason',
                  'p_isWorking',
                  'p_employerName',
                  'p_employerAddr',
                  'p_employerPhone',
                  'p_employerFaxEmail',
                  'p_hoursPerWeek',
                  'p_hoursTravel',
                  'p_isWorkRelatedCourse',
                  'p_trainingOrgName',
                  'p_trainingOrgAddr',
                  'p_trainingOrgPhone',
                  'p_trainingOrgFaxEmail',
                  'p_employerFaxEmail',
                  'p_nameOfCourse',
                  'p_isNZQA',
                  'p_courseStartDate',
                  'p_courseEndDate',
                  'p_courseHoursPerWeek',
                  'p_otherStudyHoursPerWeek',
                  'p_hoursTravelCCtoCourse',
                  'p_isArrangedActivities',
                  'p_activityType',
                  'p_hoursActivity',
                  'p_hoursTravelCCtoActivity',
                  'p_applyForMedicalReasons',
                  'p_medicalDurationExpected',
                  'p_hoursPerWeekNeedCC',
                  'p_incomeWagesSalary',
                  'p_incomePPL',
                  'p_terminationPay',
                  'p_redundancyPay',
                  'p_acc',
                  'p_incomeInsurance',
                  'p_incomeBusiness',
                  'p_incomeSelfEmpContract',
                  'p_incomeInterest',
                  'p_incomeDividends',
                  'p_incomeRental',
                  'p_incomeFlatmates',
                  'p_incomeChildSup',
                  'p_incomeOtherForChild',
                  'p_incomeMaintenance',
                  'p_incomeFormerPartner',
                  'p_incomeStudentAllowance',
                  'p_incomeOverseasPension',
                  'p_incomeSuper',
                  'p_incomeEstate',
                  'p_incomeTrusts',
                  'p_incomeOther',
                  'p_jointPartnerWhere1',
                  'p_jointPartnerWith1',
                  'p_jointPartnerYou1',
                  'p_jointPartnerFreq1',
                  'p_jointPartnerWhere2',
                  'p_jointPartnerWith2',
                  'p_jointPartnerYou2',
                  'p_jointPartnerFreq2',
                  'p_jointPartnerWhere3',
                  'p_jointPartnerWith3',
                  'p_jointPartnerYou3',
                  'p_jointPartnerFreq3',
                  'p_jointPartnerWhere4',
                  'p_jointPartnerWith4',
                  'p_jointPartnerYou4',
                  'p_jointPartnerFreq4',
                  'p_jointPartnerWhere5',
                  'p_jointPartnerWith5',
                  'p_jointPartnerYou5',
                  'p_jointPartnerFreq5',
                  'p_other52weeksType1',
                  'p_other52weeksWhere1',
                  'p_other52weeksValue1',
                  'p_other52weeksType2',
                  'p_other52weeksWhere2',
                  'p_other52weeksValue2',
                  'p_other52weeksType3',
                  'p_other52weeksWhere3',
                  'p_other52weeksValue3',
                  'p_other52weeksType4',
                  'p_other52weeksWhere4',
                  'p_other52weeksValue4',
                  'p_other52weeksType5',
                  'p_other52weeksWhere5',
                  'p_other52weeksValue5',
                  ]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),

    # GETs
    path('advised/', views.getAdvised, name='advised'),
    path('advised/<int:pk>/', views.getOneAdvised, name='oneAdvised'),
    path('locality/', views.getLocalities, name='getLocalities'),
    path('group/', views.getGroups, name='getGroups'),
    path('visit-status/', views.getVisitSatuses, name='getVisitStatuses'),
    path('agreement/', views.getAgreements, name='getAgreements'),
    path('contacted-referrer/', views.getContactedReferrers, name='getContactedReferrers'),
    path('address/', views.getAddresses, name='getAddresses'),
    path('logo/', views.getLogos, name='getLogos'),
    path('visit/', views.getVisits, name='getVisits'),
    path('useraccount/', views.getUserAccount, name='getUserAccount'),
    path('vehicles/', views.getVehicles, name='getVehicles'),
    path('requeststatus/', views.getRequestStatus, name='getRequestStatus'),
    path('contactedreferreremail/', views.getContactedReferrerEmail, name='getContactedReferrerEmail'),
    path('contactedreferrerphone/', views.getContactedReferrerPhone, name='getContactedReferrerPhone'),
    path('mayoremail/', views.getMayorEmail, name='getMayorEmail'),
    path('mayorphone/', views.getMayorPhone, name='getMayorPhone'),
    path('ministry-department/', views.getMinistryDepartments, name='getMinistryDepartments'),
    path('faq/', views.getFaqs, name='getFaqs'),
    path('coordinator/', views.getCoordinators, name='getCoordinators'),
    path('coordinator/<int:pk>/', views.getOneCoordinator, name='getOneCoordinator'),
    path('advisor/', views.getAdvisors, name='getAdvisors'),
    path('advisor/<int:pk>/', views.getOneAdvisor, name='getOneAdvisor'),
    path('cityDepartment/', views.getCityDepartments, name='getCityDepartment'),
    path('userstatuses/', views.getUserStatuses, name='getUserStatuses'),
    path('mayors/', views.getMayors, name='getMayors'),
    path('vehiclebrand/', views.getVehicleBrands, name='getVehicleBrand'),
    path('vehiclemodel/', views.getVehicleModels, name='getVehicleModels'),
    path('politicparty/', views.getPoliticParties, name='getPoliticParties'),
    path('vehicleplate/', views.getVehiclePlates, name='getVehiclePlates'),
    path('role/', views.getRoles, name='getRoles'),
    path('requeststatus/', views.getRequestStatuses, name='getRequestStatuses'),
    path('request/', views.getRequests, name='getRequests'),
    path('groups/<int:id_group>/advisors', views.getGroupAdvisors, name='getGroupAdvisors'),
    path('groups/<int:id_group>/coordinators', views.getGroupCoordinators, name='getGroupCoordinators'),
    path('advisor-users/', views.getAdvisorUsers, name='getAdvisorUsers'),
    path('coordinator-users/', views.getCoordinatorUsers, name='getCoordinatorUsers'),
    path('group/<int:id_group>/coordinator/users/', views.getGroupCoordinatorUsers, name='getGroupCoordinatorUsers'),
    path('group/<int:id_group>/advisor/users/', views.getGroupAdvisorUsers, name='getGroupAdvisorUsers'),



    # POSTs
    path('visit/add/', views.postVisit, name='postVisit'),
    path('group/add/', views.postGroup, name='postGroup'),
    path('request/add/', views.postRequest, name='postRequest'),
    path('coordinator/add/', views.postCoordinator, name='postCoordinator'),
    path('advisor/add/', views.postAdvisor, name='postAdvisor'),
    path('advised/add/', views.postAdvised, name='postAdvised'),
]

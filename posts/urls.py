from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf.urls import url


urlpatterns = [
    path('', views.home, name='home'),
    #Custom admin panel urls
    path('webadmin/', views.webadmin, name='webadmin'),
    path('addpost/', views.add_post, name='addpost'),
    path('addcat/', views.add_cat, name='addcat'),
    path('webadmin/addleftcat/', views.add_leftcat, name='addleftcat'),
    path('webadmin/addmiddlecat/', views.add_middlecat, name='addmiddlecat'),
    path('webadmin/addrightcat/', views.add_rightcat, name='addrightcat'),
    path('addvideo/', views.add_videos, name='addvideo'),
    path('add_course/', views.add_course, name='addcourse'),
    path('allposts/', views.allposts, name='allposts'),
    path('allcat/', views.allcat, name='allcat'),
    path('allusers/', views.allusers, name='allusers'),
    path('allcourse/', views.allcourse, name='allcourses'),
    path('allorders/', views.allorders, name='allorders'),
    path('appprove_cert/<int:id>', views.approve_certificates, name='appprove_cert'),
    path('allvideos/', views.allvideos, name='allvideos'),
    # path('orderdetail/<int:id>', views.order_details, name='orderdetail'),
    path('webadmin/editpost/<int:id>', views.edit_post, name='editpost'),
    path('webadmin/deletepost/<int:id>', views.delete_post, name='deletepost'),
    path('webadmin/editcat/<int:id>', views.edit_cat, name='editcat'),
    path('webadmin/editvideo/<int:id>', views.edit_videos, name='editvideo'),
    path('webadmin/deletecat/<int:id>', views.delete_cat, name='deletecat'),
    path('webadmin/deletevideo/<int:id>', views.delete_video, name='deletevideo'),
    path('webadmin/editcourse/<int:id>', views.edit_course, name='editcourse'),
    path('webadmin/deletecourse/<int:id>', views.delete_course, name='deletecourse'),
    path('webadmin/add_faq/', views.add_faq, name='add_faq'),
    path('webadmin/edit_faq/<int:id>', views.edit_faq, name='edit_faq'),
    path('webadmin/delete_faq/<int:id>', views.delete_faq, name='delete_faq'),
    path('webadmin/allfaq/', views.allfaq, name='allfaq'),
    path('webadmin/add_time/', views.add_time, name='add_time'),
    path('webadmin/edit_time/<int:id>', views.edit_time, name='edit_time'),
    path('webadmin/delete_time/<int:id>', views.delete_time, name='delete_time'),
    path('webadmin/alltime/', views.alltime, name='alltime'),
    path('webadmin/add_features/', views.add_features, name='add_features'),
    path('webadmin/edit_features/<int:id>', views.edit_features, name='edit_features'),
    path('webadmin/delete_features/<int:id>', views.delete_features, name='delete_features'),
    path('webadmin/allfeatures/', views.allfeatures, name='allfeatures'),
    path('webadmin/add_curriculam/', views.add_curriculam, name='add_curriculam'),
    path('webadmin/edit_curriculam/<int:id>', views.edit_curriculam, name='edit_curriculam'),
    path('webadmin/delete_curriculam/<int:id>', views.delete_curriculam, name='delete_curriculam'),
    path('webadmin/allcurriculam/', views.allcurriculam, name='allcurriculam'),
    path('webadmin/add_subcatg/', views.add_subcatg, name='add_subcatg'),
    path('webadmin/edit_subcatg/<int:id>', views.edit_subcatg, name='edit_subcatg'),
    path('webadmin/delete_subcatg/<int:id>', views.delete_subcatg, name='delete_subcatg'),
    path('webadmin/allsubcatg/', views.allsubcatg, name='allsubcatg'),
    path('webadmin/add_blogs/', views.add_blogs, name='add_blogs'),
    path('webadmin/edit_blogs/<int:id>', views.edit_blogs, name='edit_blogs'),
    path('webadmin/delete_blogs/<int:id>', views.delete_blogs, name='delete_blogs'),
    path('webadmin/allblogs/', views.allblogs, name='allblog'),
    path('webadmin/add_blank/', views.add_blank, name='add_blank'),
    path('webadmin/edit_blank/<int:id>', views.edit_blank, name='edit_blank'),
    path('webadmin/delete_blank/<int:id>', views.delete_blank, name='delete_blank'),
    path('webadmin/allblank/', views.allblank, name='allblank'),
    path('webadmin/add_tc/', views.add_tc, name='add_tc'),
    path('webadmin/edit_tc/<int:id>', views.edit_tc, name='edit_tc'),
    path('webadmin/delete_tc/<int:id>', views.delete_tc, name='delete_tc'),
    path('webadmin/alltc/', views.alltc, name='alltc'),
    path('webadmin/admin_reviews/', views.admin_reviews, name='admin_reviews'),
    path('webadmin/delete_admin_review/<int:id>', views.delete_admin_review, name='delete_admin_review'),
    path('webadmin/edit_admin_review/<int:id>', views.edit_admin_review, name='edit_admin_review'),
    path('webadmin/alladmin_review/', views.alladmin_review, name='alladmin_review'),
    path('webadmin/add_ribbon/', views.add_ribbon, name='add_ribbon'),
    path('webadmin/delete_ribbon/<int:id>', views.delete_ribbon, name='delete_ribbon'),
    path('webadmin/edit_ribbon/<int:id>', views.edit_ribbon, name='edit_ribbon'),
    path('webadmin/allribbon/', views.allribbon, name='allribbon'),


    #User panel urls
    path('userlogin/', views.login, name='userlogin'),
    path('usersignup/', views.signup, name='usersignup'),
    path('userlogout/', views.logout, name='logout'),
    path('userdashboard/', views.userdashboard, name='userhome'),
    path('userprofile/', views.userprofile, name='profile'),
    path('userdetail/<int:id>', views.userdetails, name='userdetails'),
    path('edituserprofile/', views.edit_profile, name='editprofile'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('certificate/<str:category_slug>/<str:slug>/', views.usercertificate, name='certificate'),

    #Public urls
    # path('career/', views.career, name='career'),
    path('add/<str:slug>', views.add_to_cart, name='add'),
    path('add_promo/<code>', views.add_promo, name='add_promo'),
    path('cart/', views.cart_view, name='cart'),
    path('removecart/<int:id>', views.remove_from_cart, name='removecart'),
    path('search/', views.search, name='search'),
    # path('category/<str:slug>/', views.post_by_category, name='catpost'),
    path('filter/<str:catslug>', views.post_by_category, name='catpost'),
    # path('subcat/<str:slug>/', views.subcat_by_category, name='subcat'),
    path('subcat/<str:subcatslug>', views.subcat_by_category, name='subcat'),
    # path('posts/category/<str:slug>/', views.allpost_by_category, name='allcatpost'),
    path('<str:postslug>', views.allpost_by_category, name='allcatpost'),
    path('<str:category_slug>/<str:slug>', views.post_details, name='details'),
    path('videos/', views.videos, name='videos'),
    path('users/yourcoursesvideo/<str:slug>/', views.paid_video, name='paid_video'),
    path('blogs/', views.blogs, name='blogs'),
    # path('blogs/<str:slug>', views.blog_catposts, name='blog_catposts'),            
    path('<str:blogcatslug>', views.blog_catposts, name='blog_catposts'),            
    # path('blog/<str:slug>', views.blogdetails, name='blogdetails'),            
    path('<str:detslug>', views.blogdetails, name='blogdetails'),            
    path('courses/', views.courses, name='courses'),            
    path('<str:slug>', views.blank_page, name='blank_page'), 
    path('checkout/', views.checkout, name='checkout'), 
    path('add-promocode/', views.add_coupon, name='add_coupon'), 
    path('verify_payment/', views.verify_payment, name='verify_payment'), 
    path('allcourses/', views.totalposts, name='all-courses'), 

    # url(r'^getSubcategory/$', views.get_subcategory)           


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

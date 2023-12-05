from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from hub.models import *
import json


class signup_view(APIView):
    
    def post(self, request, format=None):
        
        data = json.loads(request.body.decode('utf-8'))
        username = data["username"]
        password = data["password"]
        email = data["email"]
        gender = data["gender"]
        age = data["age"]
        department = data["department"]
        
        userObject = User.objects.create(username=username, password=password, email=email)
        user.objects.create(user=userObject, gender=gender, age=age, department=department)
        
        return Response({'status':'SignIn Success'})
    
# -----------------------------------------------------------------------------------------------------------------------

class login_view(APIView):
    
    def post(self, request, format=None):
        
        data = json.loads(request.body.decode('utf-8'))
        username = data["username"]
        password = data["password"]
        try:
            userObject = User.objects.get(username=username)
        except Exception as e:
            return Response({'Status':'User Not Found'})
        if userObject.password == password:
            staff = "false"
            staffClub = ''
            userClubs = []
            if userObject.is_staff:
                staff = "true"
                staffObject = user.objects.get(user = userObject)
                staffClub = staffObject.club.all()[0]
                staffClub = staffClub.clubName
            else:
                userObj = user.objects.get(user = userObject)
                clubObj = userObj.club.all()
                for i in clubObj: 
                    userClubs.append(i.clubName)
            
            data = {
                'userid': userObject.id,
                'username': userObject.username,
                'status':'success',
                'staff':staff,
                'staffClub':staffClub,
                'userClubs':userClubs
            }
            
            return Response(data)
        
        return Response({'Status':'Login Failed'})
    
# -----------------------------------------------------------------------------------------------------------------------
    
class event_view(APIView):
    
    def get(self, request, format=None):
        
        eventObject = event.objects.all()
        eventList = {}
        for events in eventObject: 
            eventList[events.eventName] = {
                "EventClub":events.eventClub.clubName,
                "EvenDate":events.eventDate, 
                "EventTime":events.eventTime
                }
            
        return Response(eventList)
    
    # _______________________________________________________
    
    def post(self, request, format=None):
        
        data = request.data
        eventclub = data["eventclub"]
        
        try:
            clubObject = club.objects.get(clubName=eventclub)
        except club.DoesNotExist:
            return Response({'Status':'Club Not Found'})
        eventname = data["eventname"]
        date = data["date"]
        time = data["time"]
                             
        event.objects.create(
            eventClub=clubObject,
            eventName=eventname,
            eventDate=date,
            eventTime=time
            )
        
        return Response({'status':'Event added'})
    
    # _______________________________________________________
    
    def delete(self, request, format = None):
        
        data = request.data
        eventname = data["eventName"]
        
        try:
            eventObject = event.objects.get(eventName=eventname)
        except event.DoesNotExist:
            return Response({'Status':'Event Not Found'})
        
        eventObject.delete()
                             
        return Response({'status':'Event Deleted'})
    
    # _______________________________________________________
    
    def patch(self, request, format = None):
        
        data = request.data
        eventName = data["eventName"]
        eventUpdatedName = data.get("eventUpdatedName")
        eventUpdateDate = data.get("eventUpdateDate")
        eventUpdateTime = data.get("eventUpdateTime")
        
        try:
            eventObject = event.objects.get(eventName=eventName)
        except event.DoesNotExist:
            return Response({'Status':'Event Not Found'})
        
        if eventUpdatedName:
            eventObject.eventName = eventUpdatedName
        if eventUpdateDate:
            eventObject.eventDate = eventUpdateDate
        if eventUpdateTime:
            eventObject.eventTime = eventUpdateTime
            
        eventObject.save()
        
        return Response({'status':'Event Updated'})
    
# -----------------------------------------------------------------------------------------------------------------------

class club_view(APIView):
    
    def get(self, request, format=None):
        
        clubObject = club.objects.all()
        clubList = {}
        for clubs in clubObject: 
            clubList[clubs.clubName] = {
                "ClubAdvisor":clubs.clubAdvisor,
                }
            
        return Response(clubList)
    
    # _______________________________________________________
    
    def post(self, request, format=None):
        
        data = request.data
        clubName = data["clubName"]
        clubAdvisor = data["clubAdvisor"]
        
        club.objects.create(
            clubName = clubName,
            clubAdvisor = clubAdvisor
        )
        
        return Response({'Status':'Club Added'})
    
    # _______________________________________________________
    
    def delete(self, request, format=None):
        
        data = request.data
        clubName = data["clubName"]
        
        try:
            clubObject = club.objects.get(clubName=clubName)
        except club.DoesNotExist:
            return Response({'Status':'Club Not Found'})
        
        clubObject.delete()
                             
        return Response({'status':'Club Deleted'})
    
    # _______________________________________________________
    
    def patch(self, request, format=None):
        
        data = request.data
        clubName = data["clubName"]
        clubUpdatedName = data.get("clubUpdatedName")
        clubUpdateAdvisor = data.get("clubUpdateAdvisor")
        
        try:
            clubObject = club.objects.get(clubName=clubName)
        except club.DoesNotExist:
            return Response({'Status':'Club Not Found'})
        
        if clubUpdatedName:
            clubObject.clubName = clubUpdatedName
            clubObject.save()
        if clubUpdateAdvisor:
            clubObject.clubAdvisor = clubUpdateAdvisor
            
        clubObject.save()
        
        return Response({'status':'Club Updated'})
    
# -----------------------------------------------------------------------------------------------------------------------

class feed_view(APIView):
    
    def get(self, request, format=None):
        
        feedObject = feedback.objects.all()
        feedList = []
        
        for feeds in feedObject: 
            feedList.append({
                "eventName":feeds.event.eventName,
                "Feedback":feeds.feedback,
                "User":feeds.user.user.username
                })
            
        return Response(feedList)
    
    # _______________________________________________________
    
    def post(self, request, format=None):
        
        data = request.data
        userName = data["userName"]
        eventName = data["eventName"]
        
        try:
            djangoUserObject = User.objects.get(username=userName)
            userObject = user.objects.get(user=djangoUserObject)
            eventObject = event.objects.get(eventName=eventName)
        except User.DoesNotExist or event.DoesNotExist:
            return Response({'Status':'User/Event not found'})
        feed = data["feed"]
        
        feedback.objects.create(
            user = userObject,
            event = eventObject,
            feedback = feed
        )
        
        return Response({'Status':'Feedback Added'})
    
# -----------------------------------------------------------------------------------------------------------------------

class user_view(APIView):
    
    def post(self, request):
        data = request.data
        clubname = data['clubName']
        username = data['username']
        clubObject = club.objects.get(clubName=clubname)
        userModel = User.objects.get(username=username)
        userObject = user.objects.get(user=userModel)
        userObject.club.add(clubObject)
        userObject.save()
        return Response({'status':'success'})
    
class club_user_view(APIView):
    
    def post(self, request):
        
        data = request.data
        
        staffClub = data["staffClub"]
    
        userList = []
        UserObjects = User.objects.all()
        for Users in UserObjects:
            try:
                userObject = user.objects.get(user=Users)
                for clubObj in userObject.club.filter(clubName=staffClub):
                    userList.append({
                        "username":Users.username,
                        "email":Users.email,
                        "department":userObject.department,
                        "club":clubObj.clubName,
                    })
            except Exception as e:
                print(e)
        return Response({"data":userList})
    
    def delete(self,request):
        
        data = request.data
        username = data["username"]
        clubname = data["clubname"]
        djangoObject = User.objects.get(username=username)
        userObject = user.objects.get(user=djangoObject)
        clubObject = userObject.club.get(clubName=clubname)
        clubObject.delete()
        clubObject.save()
        return Response({"status":"Deleted"})
        
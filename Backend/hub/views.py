from rest_framework.views import APIView
from rest_framework.response import Response
from hub.models import *


class SIGNUP(APIView):
    
    def post(self, request):
        
        data = request.data
        username = data["username"]
        password = data["password"]
        email = data["email"]
        gender = data["gender"]
        age = data["age"]
        department = data["department"]
        HubUser.objects.create(username=username, password=password, email=email, gender=gender, age=age, department=department)
        return Response({'status':'Signup Success'})
    

class LOGIN(APIView):
    
    def post(self, request):
        
        data = request.data
        username = data["username"]
        password = data["password"]
        user_exists = HubUser.objects.filter(username=username).exists()
        if user_exists:
            if HubUser.objects.get(username=username).password == password:
                user = HubUser.objects.get(username=username)
                staff, staffClub, userClubs = "false", '', []
                if user.is_staff:
                    staff = "true"
                    staffClub = user.club.all()[0].name
                else:
                    clubs = user.club.all()
                    [userClubs.append(clubObj.name) for clubObj in clubs]
                data = {
                    'userid': user.id,
                    'username': user.username,
                    'status':'success',
                    'staff':staff,
                    'staffClub':staffClub,
                    'userClubs':userClubs
                }
                return Response(data)
            return Response({'status':'Incorrect Password'})
        return Response({'status':'User not Found'})

    
class EVENT(APIView):
    
    def get(self, request):
        
        eventObject = event.objects.all()
        eventList = {}
        for events in eventObject: 
            eventList[events.name] = {
                "EventClub":events.club.name,
                "EvenDate":events.date, 
                "EventTime":events.time
                }
        return Response(eventList)
    
    def post(self, request):
        
        data = request.data
        eventclub = data["eventclub"]
        eventname = data["eventname"]
        date = data["date"]
        time = data["time"]
        clubObject = club.objects.get(name=eventclub)
        
        event.objects.create(
            club=clubObject,
            name=eventname,
            date=date,
            time=time
            )
        
        return Response({'status':'Event added'})
    
    def delete(self, request, format = None):
        
        data = request.data
        eventname = data["eventname"]
        eventObject = event.objects.get(name=eventname)
        eventObject.delete()                  
        return Response({'status':'Event Deleted'})
    
    def patch(self, request, format = None):
        
        data = request.data
        eventName = data["eventname"]
        eventUpdatedName, eventUpdateDate, eventUpdateTime = data.get("eventupdatedname"), data.get("eventupdatedate"), data.get("eventupdatetime")
        eventObject = event.objects.get(name=eventName)
        if eventUpdatedName:
            eventObject.name = eventUpdatedName
        if eventUpdateDate:
            eventObject.date = eventUpdateDate
        if eventUpdateTime:
            eventObject.time = eventUpdateTime
        eventObject.save()
        return Response({'status':'Event Updated'})
    

class CLUB(APIView):
    
    def get(self, request):
    
        clubObject = club.objects.all()
        clubList = {}
        for clubs in clubObject:
            clubList[clubs.name] = {
                "ClubAdvisor":clubs.advisor.user.get_username(),
                }
            
        return Response(clubList)
    

class FEEDBACK(APIView):
    
    def get(self, request):
        
        feedObject = feedback.objects.all()
        feedList = []
        for feeds in feedObject: 
            feedList.append({
                "eventName":feeds.event.name,
                "Feedback":feeds.feedback,
                "User":feeds.user.username
                })
        return Response(feedList)
    
    def post(self, request):
        
        data = request.data
        userName = data["username"]
        eventName = data["eventname"]
        feed = data["feedback"]
        user = HubUser.objects.get(username=userName)
        eventObject = event.objects.get(name=eventName)
        feedback.objects.create(
            user = user,
            event = eventObject,
            feedback = feed
        )
        return Response({'Status':'Feedback Added'})

class JOIN_CLUB(APIView):
    
    def post(self, request):
        data = request.data
        username = data['username']
        clubname = data['clubName']
        user = HubUser.objects.get(username=username)
        clubObject = club.objects.get(name=clubname)
        user.club.add(clubObject)
        return Response({'status':'success'})
    
class CLUB_USER(APIView):
    
    def post(self, request):
        
        data = request.data
        staffClub = data["staffclub"]
        userList = []
        users = HubUser.objects.all()
        for user in users:
            userClubs = [i.name for i in user.club.all()]
            if staffClub in userClubs and (not user.is_staff):
                userList.append({
                    "username":user.username,
                    "email":user.email,
                    "department":user.department,
                    "club":staffClub,
                })
        return Response({"data":userList})
    
    def delete(self,request):
        
        data = request.data
        username = data["username"]
        clubname = data["clubname"]
        user = HubUser.objects.get(username=username)
        clubObject = user.club.get(name=clubname)
        clubObject.delete()
        clubObject.save()
        return Response({"status":"Deleted"})
        
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from account.models import Profile
from kidney.models import *
import pickle
@api_view(['GET', 'POST'])
def kidney_data(request):
    filename = 'Prediction_status_of_Chronic_kidney_disease.sav'
    scaler=pickle.load(open('scalar_kidney.sav', 'rb'))   
    loaded_model =pickle.load(open(filename, 'rb'))
    if request.method=="POST":
        serializer = person_dataSerializer(data=request.data)
        if serializer.is_valid():
                form1=serializer.save()
                ls=[]
                ls.append(float(form1.age))
                ls.append(form1.al)
                ls.append(float(form1.su))
                ls.append(form1.bgr)
                ls.append(form1.bu)
                ls.append(float(form1.sc))
                ls.append(float(form1.hemo))
                ls.append(form1.pcv)
                ls.append(form1.wc)
                if form1.htn == 'yes':ls.append(1)
                else: ls.append(0)
                print("jjjj",ls)
                ans=loaded_model.predict(scaler.transform([ls]))
                ans1=loaded_model.predict_proba(scaler.transform([ls]))
                form1.result=int(ans[0])
                form1.result2=str(ans1[0][0]);
                form1.save()
                request.user.profile.get().kidney.add(form1)
                print("llllll",form1)

                # print(ans,ans1)     
                return Response({
                    "result":ans,
                    "result2":ans1,
                })
       
    else :
        user1=request.user
        profile=Profile.objects.get(user=user1)
        try:
            person_Data= profile.kidney

        except:
            return Response("You do not have it know")

        serializer = person_dataSerializer(person_Data,many=True)
        return Response(serializer.data)
        # return Response("ss")


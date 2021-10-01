from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from account.models import Profile
import pickle 
import warnings
warnings.filterwarnings("ignore")
from .models import *
@api_view(['GET', 'POST'])
def heart_data(request):
    filename = 'heart-disease-prediction.sav'
    scaler=pickle.load(open('scalar.sav', 'rb'))
    loaded_model =pickle.load(open(filename, 'rb'))
    print(loaded_model)
    if request.method=="POST":
        serializer =Heart_dataSerializer(data=request.data)
        if serializer.is_valid():
                form1=serializer.save()
                ls=[]
                ls.append(float(form1.age))
                ls.append(float(form1.cp))
                ls.append(float(form1.trestbps))
                ls.append(float(form1.chol))
                ls.append(float(form1.thalach))
                ls.append(float(form1.exang))
                ls.append(float(form1.oldpeak))
                ls.append(float(form1.ca))
                ans=loaded_model.predict(scaler.transform([ls]))
                ans1=loaded_model.predict_proba(scaler.transform([ls]))
                form1.result=int(ans[0])
                form1.result2=int(ans1[0][0])
                form1.save()
                request.user.profile.get().heart.add(form1)      
                return Response({
                    "result":ans,
                    "result2":ans1
                })
       
    else :
        user1=request.user
        profile=Profile.objects.get(user=user1)
        try:
            person_Data=profile.heart

        except:
            return Response("You do not have it know")

        serializer = Heart_dataSerializer(person_Data,many=True)
        return Response(serializer.data)
        # return Response("ss")


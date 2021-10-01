from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from account.models import Profile
import pickle 
import warnings
warnings.filterwarnings("ignore")
from .models import *
@api_view(['GET', 'POST'])
def Diabetes_data(request):
    filename = 'Diabetes-disease-prediction.sav'
    scaler=pickle.load(open('Diabetes.sav', 'rb'))
    loaded_model =pickle.load(open(filename, 'rb'))
    print(loaded_model)
    print(scaler)
    if request.method=="POST":
        serializer =Diabets_dataSerializer(data=request.data)
        if serializer.is_valid():
                form1=serializer.save()
                ls=[]
                ls.append(form1.Pregnancies)
                ls.append(form1.Glucose)
                ls.append(form1.SkinThickness)
                ls.append(form1.Insulin)
                ls.append(int(form1.age))
                print(ls)
                ans=loaded_model.predict(scaler.transform([ls]))
                ans1=loaded_model.predict_proba(scaler.transform([ls]))
                form1.result=int(ans[0])
                form1.result2=int(ans1[0][0])
                form1.save()
                request.user.profile.get().diabetes.add(form1)      
                return Response({
                    "result":ans,
                    "result2":ans1
                })
       
    else :
        user1=request.user
        profile=Profile.objects.get(user=user1)
        try:
            person_Data=profile.diabetes

        except:
            return Response("You do not have it know")

        serializer = Diabets_dataSerializer(person_Data,many=True)
        return Response(serializer.data)
        # return Response("ss")


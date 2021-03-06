import json

from flask import Flask, jsonify, request
from flask_restful import Api,Resource,reqparse
from Backend.utils_backend import  input_adapter,sedwik_main,twitter_collector_basic as tw_cl
from functools import wraps
from flask_cors import CORS
from Backend.summarization import hugging_faces
from Backend.utils_backend.emotion_tweet import EmotionTweet
app = Flask(__name__)
api=Api(app)
Input_Adapter = input_adapter.Adapter()
CORS(app, supports_credentials=True)


# example to the use of flask server & endpoints

# import pandas as pd
# import datetime



#
# df=pd.read_csv(r"C:\Users\meiri\Desktop\חומרים לימודיים\שנה ג\Downloads\relevant_tweets.tsv", sep='\t')
# df.to_csv('results_csv', index=False,float_format='%.16f')
# print(df.iloc[:,1].values)
class Router(Resource):
    def get(self):
        Tw_Cl=tw_cl.TwitterCollector()
        Tw_Cl.read_from_twitter()
        Input_Adapter.from_twitter_to_sedtwik()
        sedwik_main.mainFunc()

        return {"data":"this is endpoint_example"}
    def post(self):
        return {"data":"this is post endpoint_example"}

class events(Resource):
    def get(self, algorithm):
        path=r"C:\Users\user\Documents\GitHub\Twitter-Event-Detection\Backend\results\\2012-10-12_{}.json".format(algorithm)
        with open(path, 'r') as file:
            data =json.load(file)
            if  data[0]['summarized'] == "true":
                return jsonify(data)
            hg=hugging_faces.HuggingFaces()
            for i in range(len(data)):
                # summarize for event name
                dictionary=data[i]
                if algorithm == "sedwik":
                    summary=hg.summarize(dictionary["event"])
                elif algorithm == "twembeddings":
                    summary = hg.summarize(dictionary["dirty_text"])
                # calc tweet emotion
                if "tweets_emotion" not in dictionary:
                    dictionary["tweets_emotion"] = EmotionTweet().find_emotion(dictionary["dirty_text"])
                dictionary['event'] = summary
                data[i] = dictionary

        with open(path, 'w') as file:
            json.dump(data, file)
            # with open(path, 'w') as f:
        #     json.dump(jsonify(data), f)
        return jsonify(data)

class eventsByDate(Resource):
    def get(self, Date,algorithm):
        # date=request.args['Date'] # yyyy-mm-dd
        # print(request)
        prefix= r"C:\Users\user\Documents\GitHub\Twitter-Event-Detection\Backend\results\\"
        with open(prefix+"{}_{}.json".format(Date,algorithm)) as date_file:
            data = json.load(date_file)
            return jsonify(data)



class sedtwik(Resource):
    def get(self):
        return {"data": "without router"}

api.add_resource(Router,"/excute_sedtwik")

api.add_resource(events,"/events/summary/<algorithm>")
api.add_resource(eventsByDate,"/events/<algorithm>/<Date>")

api.add_resource(sedtwik,"/")

if __name__ == '__main__':
    app.run(debug=True)


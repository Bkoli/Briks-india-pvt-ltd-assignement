from flask import Flask, render_template, make_response
from flask_restful import Resource, Api
import http.client

app = Flask(__name__)
api = Api(app)

class file_reader(Resource):

    def get(self,filename=None, start_point=None, end_point=None):
        """
        accepte file name and read file depends on line numbers
        App route : http://127.0.0.1:8000/filename/startpoint/endpoint
        http://127.0.0.1:8000/file4/1/4

        :return: File Data
        """
        data = []
        try:
            if filename is None:
                filename ="file1"

            with open(filename+".txt","r", encoding="utf8" , errors='ignore') as fp:
                for i, line in enumerate(fp.readlines()):
                    data.append(line)
            if start_point and end_point:
                data =data[start_point:end_point]
            elif start_point and not end_point:
                data =data[start_point:len(data)] 
            headers = {'Content-Type': 'text/html'}
            return make_response(render_template("index.html", title= filename,list2=data), 200, headers)
        # except Exception as error:

        except Exception as error:
            print("Error while fetching file data", error)
            response = make_response(render_template("Error_page.html", title= "Exception",error=error),
                                      http.HTTPStatus.BAD_REQUEST)
        return response


api.add_resource(file_reader,'/', '/<filename>', '/<filename>/<int:start_point>','/<filename>/<int:start_point>/<int:end_point>', endpoint='user')


if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port=8000)

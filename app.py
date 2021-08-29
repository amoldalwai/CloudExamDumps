from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from examlist import examlist
import csv

filename = "aws_asc_sa_all.csv"

fileList=['aws_asc_sa_all.csv','aws_asc_cp_all.csv','aws_asc_dev_all.csv']

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

result={}
 
@app.route('/<string:quiz>')
def quiz_page(quiz):
    examlist_id=""
    qcount=0
    quizval=quiz
    quiz =quiz.strip()+".csv"
    if quiz not in fileList:
       error_result={"Status":"ErrorPAge"}
       return render_template('error.html')

    with open(quiz, 'r', encoding='unicode_escape') as csvfile:
      csvreader = csv.reader(csvfile)
      first_row = next(csvreader)
      for row in csvreader:
         qcount+=1
         result[row[0]] = {}
         result[row[0]]['id'] = row[0]
         result[row[0]]['question'] = row[1]
         result[row[0]]['options'] = {}
         result[row[0]]['options']['A']=row[2]
         result[row[0]]['options']['B']=row[3]
         result[row[0]]['options']['C']=row[4]
         result[row[0]]['options']['D']=row[5]
         result[row[0]]['answer'] = str(row[6]).strip()
    # return jsonify(result['34']['options']['A'])
    #return jsonify(result)
      for key, value in examlist.items():
         for key1, value1 in value.items():
             if quizval== value1:
                 examlist_id= key 
                 break
      
    return render_template('template.html', my_string="Wheeeee!", qcount=qcount, examlist=examlist, exam_selected_id=examlist_id, result=result)

@app.route('/')
def homepage():
  result={
   "Status":"200OK"
  }
  return render_template('navbar.html',examlist=examlist)

@app.route('/examlist')
def exam_list():
  result={
   "Status":"200OK"
  }
  return jsonify(examlist)

# @app.route('/aws_asc_sa/<int :n>')
# def loopdict():
#   len
   
 
#   return ""

if __name__=="__main__":
 app.run(debug=True)
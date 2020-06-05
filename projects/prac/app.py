from flask import Flask, render_template
app = Flask(__name__)
# 플라스크 사용하겠다

@app.route('/')
def home():
   return render_template('index.html')



if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)
   # 플라스크 파일을 돌려주는애야 app.run
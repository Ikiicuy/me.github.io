import pandas as pd
from flask import Flask,render_template,request
app=Flask(__name__)
app.config["SECRET_KEY"]="hai"

file="excel.xlsx"
try:
  df=pd.read_excel(file)
except FileNotFoundError:
  df = pd.DataFrame(columns=["pesan"])
  df.to_excel(file, index=False)
@app.route("/beranda",methods=["GET","POST"])
def beranda():
	if request.method=="POST":
	  
	  pesan = request.form["pesan"]
    if pesan != "":
      
      df = df.append({"pesan": pesan}, ignore_index=True)
      df.to_excel(file, index=False)
      print("data berhasil masuk")
      break
	return render_template("bst2.html")


        
        
        
 if __name__=="__main__":
 	app.run(debug=True)
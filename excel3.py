import pandas as pd
from flask import Flask,render_template,request,url_for
app=Flask(__name__)
app.config["SECRET_KEY"]="hai"

file="excel.xlsx"

@app.route("/beranda",methods=["GET","POST"])
def beranda():
  if request.method=="POST":
    df=pd.read_excel(file)
    pesan = request.form["pesan"]
    if pesan != "":
      df = df.append({"pesan": pesan}, ignore_index=True)
      df.to_excel(file, index=False)
      print("data berhasil masuk")
      
  return render_template("bst2.html")

if __name__=="__main__":
 	app.run(debug=True)

from flask import Flask, render_template,request

app=Flask(__name__)

data = {
    "0": {"name":"Huracan", "price":"180,000","date":"2018","country":"Usa","engine":"4.9", "src":"https://www.auto-data.net/images/f63/Lamborghini-Huracan-Sterrato.jpg"},  #data moncembi
     "1": {"name":"aventator", "price":"160,000","engine":"4.6","date":"2017", "country":"Geo", "src":"https://imgcdnblog.carmudi.com.ph/carmudi-ph/wp-content/uploads/2018/11/18021232/526140-min.jpg"},
     "2": {"name":"Huracan", "price":"230,000","engine":"6.5", "date":"2024", "country":"japan","src":"https://www.lamborghini.com/sites/it-en/files/DAM/lamborghini/facelift_2019/models_gw/2023/03_29_revuelto/gate_models_s_03_m.jpg" }, 
     "3": {"name":"Conpect", "price":"260,000", "engine":"3.8","date":"2025","country":"Usa", "src":"https://www.topgear.com/sites/default/files/images/gallery-migration/2014-05/9FECF49A-F108-4E96-8D4A-271A03FCC2EC.jpg" }, 
     "4": {"name":"Murcielago", "price":"150,000", "engine":"5.5","date":"2015","country":"Corea", "src":"https://wearecurated.b-cdn.net/wp-content/uploads/Lamborghini-Murcielago-LP640-Arancio-on-Orange-Black-8.jpg" }, 
     "5": {"name":"Murcielago", "price":"160,000","engine":"4.3", "date":"2026","country":"deuchland", "src":"https://www.carbodydesign.com/media/2006/02/Lamborghini-Murcielago-LP640-1-lg-720x540.jpg" }, 
     "6": {"name":"Gallardo", "price":"200,000","engine":"4.5", "date":"2020","country":"france", "src":"https://www.hdcarwallpapers.com/walls/lamborghini_galardo_superleggera-wide.jpg" }, 
      "7": {"name":"Huracan", "price":"320,000","engine":"4.5", "date":"2023","country":"france", "src":"https://s3-prod-europe.autonews.com/s3fs-public/Lamborghini%20Huracan%20STO%20web.jpg" }, 
      "8": {"name":"Gallardo", "price":"200,000","engine":"4.5", "date":"2020","country":"USa", "src":"https://www.cars.com/i/large/in/v2/stock_photos/12081274-be33-46c5-be10-807ddcc54bd7/00e97afc-5c7b-4203-a1e0-0508c8262e7c.png" }, 
     "9": {"name":"Gallardo", "price":"300,000","engine":"6.5", "date":"2024","country":"Deuchland", "src":"https://res.cloudinary.com/driveau/image/private/q_auto/v1/ca-s3/2012/09/Lamborghini-Gallardo-LP570-4-Superleggera-Edizione-Tecnica-1-625x468.jpg" }, 
     }


@app.route("/", methods=['GET'])   # როუტერია რამდნიც გინდა იმდნი გააკეტე  გვერდებს ნიშნავს როგორც ანგულრზე
def hello_world():                  # / sleshi მთვარ გვერდს ნიშნავს 
    return render_template("index.html")

@app.route("/ebaut", methods=['GET'])   # ეს ებაუტ როუტის ფეიჯია, სადაც გადლინკვა მაქ ჰტმლში გაკეტბული 
def ebaut():
    return render_template("ebaut.html")




@app.route("/car",methods=['GET'])  
def car(): 
   
    
    return render_template("car.html", car=data)  #მეორე პარმტრად ჩააწოდე ცვლადი რომ ჰტმლ მხარეს დაინხოს და დავტრილო ლუპი
 




@app.route("/car/<int:carid>")   #int გავნსზრვრე პარმეტრი, book ის ყველა გვერდს თავის იდ რო ქოდნეს
def cargverdebi(carid):  #  ზემოთ შექმნლი პარმეტრი ჩავაწოდე ამ ფუნქციას
  
    
    
    element=data[str(carid)] # el გავხდა data დან წიგნის ის იდ რასაც შეიყვნს მომხრბლი, რასაც დაკლიკბს
    
    return render_template("car_detal.html", car=element)



if __name__ == "__main__":
    app.run(debug=True)
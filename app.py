from flask import Flask, jsonify, request

app = Flask(__name__)

#Criptomoneda Bitcoin, conversión a 10 Monedas.

@app.route("/BitcoinaUSD/<string:valorUSD>")
def get_datosUSD(valorUSD):
    valorUSD = float(valorUSD)
    conversion1 = valorUSD*43810.10
    return jsonify({ "Conversion a USD" : conversion1})

@app.route("/BitcoinaARS/<string:valorARS>")
def get_datosARS(valorARS):
    valorARS = float(valorARS)
    conversion2 = valorARS*4714839.00
    return jsonify({ "Conversion a ARS" : conversion2})

@app.route("/BitcoinaAUD/<string:valorAUD>")
def get_datosAUD(valorAUD):
    valorAUD = float(valorAUD)
    conversion3 = valorAUD*55848.74
    return jsonify({ "Conversion a AUD" : conversion3})

@app.route("/BitcoinaEUR/<string:valorEUR>")
def get_datosEUR(valorEUR):
    valorEUR = float(valorEUR)
    conversion4 = valorEUR*55848.74
    return jsonify({ "Conversion a EUR" : conversion4})

@app.route("/BitcoinaCAD/<string:valorCAD>")
def get_datosCAD(valorCAD):
    valorCAD = float(valorCAD)
    conversion5 = valorCAD*56445.00
    return jsonify({ "Conversion a CAD" : conversion5})

@app.route("/BitcoinaJPY/<string:valorJPY>")
def get_datosJPY(valorJPY):
    valorJPY = float(valorJPY)
    conversion6 = valorJPY*5070744.00
    return jsonify({ "Conversion a JPY" : conversion6})

@app.route("/BitcoinaMXN/<string:valorMXN>")
def get_datosMXN(valorMXN):
    valorMXN = float(valorMXN)
    conversion7 = valorMXN*917431.19
    return jsonify({ "Conversion a MXN" : conversion7})

@app.route("/BitcoinaGBP/<string:valorGBP>")
def get_datosGBP(valorGBP):
    valorGBP = float(valorGBP)
    conversion8 = valorGBP*33035.27
    return jsonify({ "Conversion a GBP" : conversion8})

@app.route("/BitcoinaBRL/<string:valorBRL>")
def get_datosBRL(valorBRL):
    valorBRL = float(valorBRL)
    conversion9 = valorBRL*225598.58
    return jsonify({ "Conversion a BRL" : conversion9})

#Criptomoneda Ethereum, conversión a 10 Monedas.

@app.route("/EthereumaUSD/<string:valorEUSD>")
def get_datosEUSD(valorEUSD):
    valorEUSD = float(valorEUSD)
    conversion11 = valorEUSD*2990.08
    return jsonify({ "Conversion a USD" : conversion11})

@app.route("/EthereumaARS/<string:valorEARS>")
def get_datosEARS(valorEARS):
    valorEARS = float(valorEARS)
    conversion12 = valorEARS*321578.00
    return jsonify({ "Conversion a ARS" : conversion12})

@app.route("/EthereumaAUD/<string:valorEAUD>")
def get_datosEAUD(valorEAUD):
    valorEAUD = float(valorEAUD)
    conversion13 = valorEAUD*4121.15
    return jsonify({ "Conversion a AUD" : conversion13})

@app.route("/EthereumaEUR/<string:valorEEUR>")
def get_datosEEUR(valorEEUR):
    valorEEUR = float(valorEEUR)
    conversion14 = valorEEUR*2703.05
    return jsonify({ "Conversion a EUR" : conversion14})

@app.route("/EthereumaCAD/<string:valorECAD>")
def get_datosECAD(valorECAD):
    valorECAD = float(valorECAD)
    conversion15 = valorECAD*3810.64
    return jsonify({ "Conversion a CAD" : conversion15})

@app.route("/EthereumaJPY/<string:valorEJPY>")
def get_datosEJPY(valorEJPY):
    valorEJPY = float(valorEJPY)
    conversion16 = valorEJPY*344483.00
    return jsonify({ "Conversion a JPY" : conversion16})

@app.route("/EthereumaMXN/<string:valorEMXN>")
def get_datosEMXN(valorEMXN):
    valorEMXN = float(valorEMXN)
    conversion17 = valorEMXN*61996.28
    return jsonify({ "Conversion a MXN" : conversion17})

@app.route("/EthereumaGBP/<string:valorEGBP>")
def get_datosEGBP(valorEGBP):
    valorEGBP = float(valorEGBP)
    conversion18 = valorEGBP*2250.90
    return jsonify({ "Conversion a GBP" : conversion18})

@app.route("/EthereumaBRL/<string:valorEBRL>")
def get_datosEBRL(valorEBRL):
    valorEBRL = float(valorEBRL)
    conversion19 = valorEBRL*15358.21
    return jsonify({ "Conversion a BRL" : conversion19})

#Criptomoneda Tether, conversión a 10 Monedas.

@app.route("/TetheraUSD/<string:valorTUSD>")
def get_datosTUSD(valorTUSD):
    valorTUSD = float(valorTUSD)
    conversion21 = valorTUSD*1.00
    return jsonify({ "Conversion a USD" : conversion21})

@app.route("/TetheraARS/<string:valorTARS>")
def get_datosTARS(valorTARS):
    valorTARS = float(valorTARS)
    conversion22 = valorTARS*108.00
    return jsonify({ "Conversion a ARS" : conversion22})

@app.route("/TetheraAUD/<string:valorTAUD>")
def get_datosTAUD(valorTAUD):
    valorTAUD = float(valorTAUD)
    conversion23 = valorTAUD*108.00
    return jsonify({ "Conversion a AUD" : conversion23})

@app.route("/TetheraEUR/<string:valorTEUR>")
def get_datosTEUR(valorTEUR):
    valorTEUR = float(valorTEUR)
    conversion24 = valorTEUR*2641.00
    return jsonify({ "Conversion a EUR" : conversion24})

@app.route("/TetheraCAD/<string:valorTCAD>")
def get_datosTCAD(valorTCAD):
    valorTCAD = float(valorTCAD)
    conversion25 = valorTCAD*3725.00
    return jsonify({ "Conversion a CAD" : conversion25})

@app.route("/TetheraJPY/<string:valorTJPY>")
def get_datosTJPY(valorTJPY):
    valorTJPY = float(valorTJPY)
    conversion26 = valorTJPY*338589.00
    return jsonify({ "Conversion a JPY" : conversion26})

@app.route("/TetheraMXN/<string:valorTMXN>")
def get_datosTMXN(valorTMXN):
    valorTMXN = float(valorTMXN)
    conversion27 = valorTMXN*60901.34
    return jsonify({ "Conversion a MXN" : conversion27})

@app.route("/TetheraGBP/<string:valorTGBP>")
def get_datosTGBP(valorTGBP):
    valorTGBP = float(valorTGBP)
    conversion28 = valorTGBP*2208.00
    return jsonify({ "Conversion a GBP" : conversion28})

@app.route("/TetheraBRL/<string:valorTBRL>")
def get_datosTBRL(valorTBRL):
    valorTBRL = float(valorTBRL)
    conversion29 = valorTBRL*15063.40
    return jsonify({ "Conversion a BRL" : conversion29})

#Criptomoneda BNB, conversión a 10 Monedas.

@app.route("/BNBaUSD/<string:valorBUSD>")
def get_datosBUSD(valorBUSD):
    valorBUSD = float(valorBUSD)
    conversion31 = valorBUSD*406.21
    return jsonify({ "Conversion a USD" : conversion31})

@app.route("/BNBaARS/<string:valorBARS>")
def get_datosBARS(valorBARS):
    valorBARS = float(valorBARS)
    conversion32 = valorBARS*43853.21
    return jsonify({ "Conversion a ARS" : conversion32})

@app.route("/BNBaAUD/<string:valorBAUD>")
def get_datosBAUD(valorBAUD):
    valorBAUD = float(valorBAUD)
    conversion33 = valorBAUD*557.58
    return jsonify({ "Conversion a AUD" : conversion33})

@app.route("/BNBaEUR/<string:valorBEUR>")
def get_datosBEUR(valorBEUR):
    valorBEUR = float(valorBEUR)
    conversion34 = valorBEUR*366.60
    return jsonify({ "Conversion a EUR" : conversion34})

@app.route("/BNBaCAD/<string:valorBCAD>")
def get_datosBCAD(valorBCAD):
    valorBCAD = float(valorBCAD)
    conversion35 = valorBCAD*518.12
    return jsonify({ "Conversion a CAD" : conversion35})

@app.route("/BNBaJPY/<string:valorBJPY>")
def get_datosBJPY(valorBJPY):
    valorBJPY = float(valorBJPY)
    conversion36 = valorBJPY*46992.18
    return jsonify({ "Conversion a JPY" : conversion36})

@app.route("/BNBaMXN/<string:valorBMXN>")
def get_datosBMXN(valorBMXN):
    valorBMXN = float(valorBMXN)
    conversion37 = valorBMXN*8424.60
    return jsonify({ "Conversion a MXN" : conversion37})

@app.route("/BNBaGBP/<string:valorBGBP>")
def get_datosBGBP(valorBGBP):
    valorBGBP = float(valorBGBP)
    conversion38 = valorBGBP*305.20
    return jsonify({ "Conversion a GBP" : conversion38})

@app.route("/BNBaBRL/<string:valorBBRL>")
def get_datosBBRL(valorBBRL):
    valorBBRL = float(valorBBRL)
    conversion39 = valorBBRL*2095.33
    return jsonify({ "Conversion a BRL" : conversion39})

#Criptomoneda XRP, conversión a 10 Monedas.

@app.route("/XRPaUSD/<string:valorXUSD>")
def get_datosXUSD(valorXUSD):
    valorXUSD = float(valorXUSD)
    conversion41 = valorXUSD*0.766160
    return jsonify({ "Conversion a USD" : conversion41})

@app.route("/XRPaARS/<string:valorXARS>")
def get_datosXARS(valorXARS):
    valorXARS = float(valorXARS)
    conversion42 = valorXARS*82.73
    return jsonify({ "Conversion a ARS" : conversion42})

@app.route("/XRPaAUD/<string:valorXAUD>")
def get_datosXAUD(valorXAUD):
    valorXAUD = float(valorXAUD)
    conversion43 = valorXAUD*1.06
    return jsonify({ "Conversion a AUD" : conversion43})

@app.route("/XRPaEUR/<string:valorXEUR>")
def get_datosXEUR(valorXEUR):
    valorXEUR = float(valorXEUR)
    conversion44 = valorXEUR*0.694500
    return jsonify({ "Conversion a EUR" : conversion44})

@app.route("/XRPaCAD/<string:valorXCAD>")
def get_datosXCAD(valorXCAD):
    valorXCAD = float(valorXCAD)
    conversion45 = valorXCAD*0.970000
    return jsonify({ "Conversion a CAD" : conversion45})

@app.route("/XRPaJPY/<string:valorXJPY>")
def get_datosXJPY(valorXJPY):
    valorXJPY = float(valorXJPY)
    conversion46 = valorXJPY*89.17
    return jsonify({ "Conversion a JPY" : conversion46})

@app.route("/XRPaMXN/<string:valorXMXN>")
def get_datosXMXN(valorXMXN):
    valorXMXN = float(valorXMXN)
    conversion47 = valorXMXN*15.98
    return jsonify({ "Conversion a MXN" : conversion47})

@app.route("/XRPaGBP/<string:valorXGBP>")
def get_datosXGBP(valorXGBP):
    valorXGBP = float(valorXGBP)
    conversion48 = valorXGBP*0.578000
    return jsonify({ "Conversion a GBP" : conversion48})

@app.route("/XRPaBRL/<string:valorXBRL>")
def get_datosXBRL(valorXBRL):
    valorXBRL = float(valorXBRL)
    conversion49 = valorXBRL*2095.33
    return jsonify({ "Conversion a BRL" : conversion49})

#Criptomoneda Cardano, conversión a 10 Monedas.

@app.route("/CardanoaUSD/<string:valorCUSD>")
def get_datosCUSD(valorCUSD):
    valorCUSD = float(valorCUSD)
    conversion51 = valorCUSD*0.950209
    return jsonify({ "Conversion a USD" : conversion51})

@app.route("/CardanoaARS/<string:valorCARS>")
def get_datosCARS(valorCARS):
    valorCARS = float(valorCARS)
    conversion52 = valorCARS*102.56
    return jsonify({ "Conversion a ARS" : conversion52})

@app.route("/CardanoaAUD/<string:valorCAUD>")
def get_datosCAUD(valorCAUD):
    valorCAUD = float(valorCAUD)
    conversion53 = valorCAUD*1.06
    return jsonify({ "Conversion a AUD" : conversion53})

@app.route("/CardanoaEUR/<string:valorCEUR>")
def get_datosCEUR(valorCEUR):
    valorCEUR = float(valorCEUR)
    conversion54 = valorCEUR*0.694500
    return jsonify({ "Conversion a EUR" : conversion54})

@app.route("/CardanoaCAD/<string:valorCCAD>")
def get_datosCCAD(valorCCAD):
    valorCCAD = float(valorCCAD)
    conversion55 = valorCCAD*0.970000
    return jsonify({ "Conversion a CAD" : conversion55})

@app.route("/CardanoaJPY/<string:valorCJPY>")
def get_datosCJPY(valorCJPY):
    valorCJPY = float(valorCJPY)
    conversion56 = valorCJPY*89.17
    return jsonify({ "Conversion a JPY" : conversion56})

@app.route("/CardanoaMXN/<string:valorCMXN>")
def get_datosCMXN(valorCMXN):
    valorCMXN = float(valorCMXN)
    conversion57 = valorCMXN*15.98
    return jsonify({ "Conversion a MXN" : conversion57})

@app.route("/CardanoaGBP/<string:valorCGBP>")
def get_datosCGBP(valorCGBP):
    valorCGBP = float(valorCGBP)
    conversion58 = valorCGBP*0.578000
    return jsonify({ "Conversion a GBP" : conversion58})

@app.route("/CardanoaBRL/<string:valorCBRL>")
def get_datosCBRL(valorCBRL):
    valorCBRL = float(valorCBRL)
    conversion59 = valorCBRL*2095.33
    return jsonify({ "Conversion a BRL" : conversion59})

#Criptomoneda Solana, conversión a 10 Monedas.

@app.route("/SolanaaUSD/<string:valorSUSD>")
def get_datosSUSD(valorSUSD):
    valorSUSD = float(valorSUSD)
    conversion61 = valorSUSD*98.95
    return jsonify({ "Conversion a USD" : conversion61})

@app.route("/SolanaaARS/<string:valorSARS>")
def get_datosSARS(valorSARS):
    valorSARS = float(valorSARS)
    conversion62 = valorSARS*10685.03
    return jsonify({ "Conversion a ARS" : conversion62})

@app.route("/SolanaaAUD/<string:valorSAUD>")
def get_datosSAUD(valorSAUD):
    valorSAUD = float(valorSAUD)
    conversion63 = valorSAUD*135.94 
    return jsonify({ "Conversion a AUD" : conversion63})

@app.route("/SolanaaEUR/<string:valorSEUR>")
def get_datosSEUR(valorSEUR):
    valorSEUR = float(valorSEUR)
    conversion64 = valorSEUR*89.36
    return jsonify({ "Conversion a EUR" : conversion64})

@app.route("/SolanaaCAD/<string:valorSCAD>")
def get_datosSCAD(valorSCAD):
    valorSCAD = float(valorSCAD)
    conversion65 = valorSCAD*125.65
    return jsonify({ "Conversion a CAD" : conversion65})

@app.route("/SolanaaJPY/<string:valorSJPY>")
def get_datosSJPY(valorSJPY):
    valorSJPY = float(valorSJPY)
    conversion66 = valorSJPY*11429.49
    return jsonify({ "Conversion a JPY" : conversion66})

@app.route("/SolanaaMXN/<string:valorSMXN>")
def get_datosSMXN(valorSMXN):
    valorSMXN = float(valorSMXN)
    conversion67 = valorSMXN*2041.32
    return jsonify({ "Conversion a MXN" : conversion67})

@app.route("/SolanaaGBP/<string:valorSGBP>")
def get_datosSGBP(valorSGBP):
    valorSGBP = float(valorSGBP)
    conversion68 = valorSGBP*73.90
    return jsonify({ "Conversion a GBP" : conversion68})

@app.route("/SolanaaBRL/<string:valorSBRL>")
def get_datosSBRL(valorSBRL):
    valorSBRL = float(valorSBRL)
    conversion69 = valorSBRL*506.49
    return jsonify({ "Conversion a BRL" : conversion69})

#Criptomoneda Avalanche, conversión a 10 Monedas.

@app.route("/AvalancheaUSD/<string:valorAUSD>")
def get_datosAUSD(valorAUSD):
    valorAUSD = float(valorAUSD)
    conversion71 = valorAUSD*0.950209
    return jsonify({ "Conversion a USD" : conversion71})

@app.route("/AvalancheaARS/<string:valorAARS>")
def get_datosAARS(valorAARS):
    valorAARS = float(valorAARS)
    conversion72 = valorAARS*102.56
    return jsonify({ "Conversion a ARS" : conversion72})

@app.route("/AvalancheaAUD/<string:valorAAUD>")
def get_datosAAUD(valorAAUD):
    valorAAUD = float(valorAAUD)
    conversion73 = valorAAUD*1.06
    return jsonify({ "Conversion a AUD" : conversion73})

@app.route("/AvalancheaEUR/<string:valorAEUR>")
def get_datosAEUR(valorAEUR):
    valorAEUR = float(valorAEUR)
    conversion74 = valorAEUR*0.694500
    return jsonify({ "Conversion a EUR" : conversion74})

@app.route("/AvalancheaCAD/<string:valorACAD>")
def get_datosACAD(valorACAD):
    valorACAD = float(valorACAD)
    conversion75 = valorACAD*0.970000
    return jsonify({ "Conversion a CAD" : conversion75})

@app.route("/AvalancheaJPY/<string:valorAJPY>")
def get_datosAJPY(valorAJPY):
    valorAJPY = float(valorAJPY)
    conversion76 = valorAJPY*89.17
    return jsonify({ "Conversion a JPY" : conversion76})

@app.route("/AvalancheaMXN/<string:valorAMXN>")
def get_datosAMXN(valorAMXN):
    valorAMXN = float(valorAMXN)
    conversion77 = valorAMXN*15.98
    return jsonify({ "Conversion a MXN" : conversion77})

@app.route("/AvalancheaGBP/<string:valorAGBP>")
def get_datosAGBP(valorAGBP):
    valorAGBP = float(valorAGBP)
    conversion78 = valorAGBP*0.578000
    return jsonify({ "Conversion a GBP" : conversion78})

@app.route("/AvalancheaBRL/<string:valorABRL>")
def get_datosABRL(valorABRL):
    valorABRL = float(valorABRL)
    conversion79 = valorABRL*2095.33
    return jsonify({ "Conversion a BRL" : conversion79})

#Criptomoneda Terra, conversión a 10 Monedas.

@app.route("/TerraaUSD/<string:valorTEUSD>")
def get_datosTEUSD(valorTEUSD):
    valorTEUSD = float(valorTEUSD)
    conversion81 = valorTEUSD*92.55
    return jsonify({ "Conversion a USD" : conversion81})

@app.route("/TerraaARS/<string:valorTEARS>")
def get_datosTEARS(valorTEARS):
    valorTEARS = float(valorTEARS)
    conversion82 = valorTEARS*3078.25
    return jsonify({ "Conversion a ARS" : conversion82})

@app.route("/TerraaAUD/<string:valorTEAUD>")
def get_datosTEAUD(valorTEAUD):
    valorTEAUD = float(valorTEAUD)
    conversion83 = valorTEAUD*128.27
    return jsonify({ "Conversion a AUD" : conversion83})

@app.route("/TerraaEUR/<string:valorTEEUR>")
def get_datosTEEUR(valorTEEUR):
    valorTEEUR = float(valorTEEUR)
    conversion84 = valorTEEUR*83.10
    return jsonify({ "Conversion a EUR" : conversion84})

@app.route("/TerraaCAD/<string:valorTECAD>")
def get_datosTECAD(valorTECAD):
    valorTECAD = float(valorTECAD)
    conversion85 = valorTECAD*117.73
    return jsonify({ "Conversion a CAD" : conversion85})

@app.route("/TerraaJPY/<string:valorTEJPY>")
def get_datosTEJPY(valorTEJPY):
    valorTEJPY = float(valorTEJPY)
    conversion86 = valorTEJPY*10750.24
    return jsonify({ "Conversion a JPY" : conversion86})

@app.route("/TerraaMXN/<string:valorTEMXN>")
def get_datosTEMXN(valorTEMXN):
    valorTEMXN = float(valorTEMXN)
    conversion87 = valorTEMXN*1924.82
    return jsonify({ "Conversion a MXN" : conversion87})

@app.route("/TerraaGBP/<string:valorTEGBP>")
def get_datosTEGBP(valorTEGBP):
    valorTEGBP = float(valorTEGBP)
    conversion88 = valorTEGBP*69.50
    return jsonify({ "Conversion a GBP" : conversion88})

@app.route("/TerraaBRL/<string:valorTEBRL>")
def get_datosTEBRL(valorTEBRL):
    valorTEBRL = float(valorTEBRL)
    conversion89 = valorTEBRL*477.83
    return jsonify({ "Conversion a BRL" : conversion89})

if __name__== '__main__':
    app.run(debug=True, port=5000)
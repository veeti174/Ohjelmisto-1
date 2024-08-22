#Harjoitustehtava t2.5
leiviska = float(input("Paljonko paino on leiviskoissa?"))
naula = float(input("Paljonko paino on nauloissa?"))
luoti = float(input("Paljonko paino on luodeissa?"))
#Now that we have the measurements in right format we transform them into the right format
#the kerroin we have to use for leivska to get them to kg is 20*32*13,3 which is 8512g/1000= which is 8,512kg what we can use as the
#the kerroin for naula is 32*13,3/1000 or 0.4256
#the kerroin for luoti is 13,3/1000 or 0.0133
leiviskakg = leiviska*8.512
naulakg = naula*0.4256
luotikg = luoti*0.0133
summa = leiviskakg + naulakg + luotikg
#now i can present the answer to the user
print("Ne painavat kilogrammoissa " +str(summa))
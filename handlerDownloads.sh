#!/bin/bash

curl appredeshdj.herokuapp.com/consultarNuevasDescargas > nuevasDescargas.txt

if [ -s nuevasDescargas.txt ]
then
	nuevasDescargas=$(cat nuevasDescargas.txt)
	numeroNuevasDescargas=${nuevasDescargas%% *}
	descargasActuales=${nuevasDescargas#* }
	for ((i=0; i<$numeroNuevasDescargas; i++))
	do
		descargaI=${descargasActuales%% *}
		transmission-remote -n transmission:transmission -a $descargaI
		descargasActuales=${descargasActuales#* }
	done
	rm -rf nuevasDescargas.txt 
fi

numeroTotalDescargas=$(curl appredeshdj.herokuapp.com/consultarNumeroDescargas)
infoTrans=$(transmission-remote -n transmission:transmission -l)
info=${infoTrans#*Name}
id_dt=$(curl appredeshdj.herokuapp.com/consultarIdFinalDescargas)

for ((i=numeroTotalDescargas; i>0; i--))
do
	info=${info%\%*}
	estadoDescargaI=${info##* }
	echo $estadoDescargaI; 
	curl "appredeshdj.herokuapp.com/actualizarEstadoDescarga/"$id_dt"/"$estadoDescargaI"%"
	id_dt=$((id_dt - 1)) 
done

 
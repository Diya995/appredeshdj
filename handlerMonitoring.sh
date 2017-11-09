#!/bin/bash

estadomaquina=$(curl 0.0.0.0:5000/os)

kernel=${estadomaquina:51:5}
release=${estadomaquina:269:17}
nodename=${estadomaquina:174:9}

kvs=${estadomaquina:84:42}
kernelv=${kvs// /_}

machine=${estadomaquina:146:6}
processor=${estadomaquina:243:6}

sop=${estadomaquina:212:3}
sos=${estadomaquina:216:5}
so=$sop"_"$sos

hardware=${estadomaquina:26:6}

usuario_logueado=$(curl 0.0.0.0:5000/who)
user_logged=${usuario_logueado:14:6}

us=$(curl 0.0.0.0:5000/cpu/us)
cpu_us=${us:15:1}

sy=$(curl 0.0.0.0:5000/cpu/sy)
cpu_sy=${sy:15:1}

id=$(curl 0.0.0.0:5000/cpu/id)
cpu_id=${id:15:2}

wa=$(curl 0.0.0.0:5000/cpu/wa)
cpu_wa=${wa:15:1}

st=$(curl 0.0.0.0:5000/cpu/st)
cpu_st=${st:15:1}

swpd=$(curl 0.0.0.0:5000/mem/swpd)
mem_swpd=${swpd:17:1}

free=$(curl 0.0.0.0:5000/mem/free)
mem_free=${free:17:6}

buff=$(curl 0.0.0.0:5000/mem/buff)
mem_buff=${buff:17:5}

cache=$(curl 0.0.0.0:5000/mem/cache)
mem_cache=${cache:18:6}

si=$(curl 0.0.0.0:5000/swap/si)
swap_si=${si:16:1}

swo=$(curl 0.0.0.0:5000/swap/so)
swap_so=${swo:16:1}

curl "appredeshdj.herokuapp.com/actualizarEstadoMaquina/"$kernel"/"$release"/"$nodename"/"$kernelv"/"$machine"/"$processor"/"$so"/"$hardware"/"$user_logged"/"$cpu_us"/"$cpu_sy"/"$cpu_id"/"$cpu_wa"/"$cpu_st"/"$mem_swpd"/"$mem_free"/"$mem_buff"/"$mem_cache"/"$swap_si"/"$swap_so


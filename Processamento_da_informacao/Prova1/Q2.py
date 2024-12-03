def entrada():
    global mystr, m3, tarifa10, tarifa11, tarifa21, tarifa31, tarifa50
    mystr = "Faixa	por Economia	Tarifa	Valor\n"
    m3 = int(input())
    tarifa10 = 21.30
    tarifa11 = 3.00
    tarifa21 = 8.00
    tarifa31 = 9.00
    tarifa50 = 10.60

def process():
    global mystr
    if m3 > 50:
        eco11 = 10
        eco21 = 10
        eco31 = 20
        eco50 = m3 - 50
        valor10 = tarifa10
        valor11 = tarifa11*eco11
        valor21 = tarifa21*eco21
        valor31 = tarifa31*eco31
        valor50 = tarifa50*eco50
        agua = valor10+valor11+valor21+valor31+valor50
        mystr += f"Ate 10 	Minimo   		{tarifa10:.2f}  	  {tarifa10:.2f}\n"
        mystr += f"11a20	   {eco11}      {tarifa11:.2f}      {valor11:.2f}\n"
        mystr += f"21a30	   {eco21}      {tarifa21:.2f}      {valor21:.2f}\n"
        mystr += f"31a50	   {eco31}      {tarifa31:.2f}      {valor31:.2f}\n"
        mystr += f" > 50      {eco50}       {tarifa50:.2f}      {valor50:.2f}\n"
        mystr += "\n"
        mystr += f"Consumo agua (m^3)         {m3}\n"
        mystr += f"Total agua (R$)          {agua:.2f}\n"
        mystr += f"Total agua + Esgoto (R$) {2*agua:.2f}\n"
        mystr += "\n"
        mystr += "Desperdicio ate aquecer a agua nas torneiras/chuveiros:\n"
        mystr += "Considerando o desperdicio de agua por uso (em litros)  11\n"
        mystr += "Considerando uma tarifa de (R$)                         10.60\n"
        mystr += "Considerando o uso de agua quente por dia (vezes)       28\n"
        mystr += "Desperdicio mensal em metros cubicos (m^3)               9.24\n"
        mystr += "Desperdicio mensal na conta da Sabesp (R$)             195.89\n"
    elif m3 > 31:
        eco11 = 10
        eco21 = 10
        eco31 = m3 - 30
        valor10 = tarifa10
        valor11 = tarifa11*eco11
        valor21 = tarifa21*eco21
        valor31 = tarifa31*eco31
        agua = valor10+valor11+valor21+valor31
        mystr += f"Ate 10 	Minimo   		{tarifa10:.2f}  	  {tarifa10:.2f}\n"
        mystr += f"11a20	   {eco11}             	  {tarifa11:.2f}      {valor11:.2f}\n"
        mystr += f"21a30	   {eco21}             	  {tarifa21:.2f}      {valor21:.2f}\n"
        mystr += f"31a50	   {eco31}             	    {tarifa31:.2f}      {valor31:.2f}\n"
        mystr += "\n"        
        mystr += f"Consumo agua (m^3)         {m3}\n"
        mystr += f"Total agua (R$)           {agua:.2f}\n"
        mystr += f"Total agua + Esgoto (R$) {2*agua:.2f}\n"
        mystr += "\n"
        mystr += "Desperdicio ate aquecer a agua nas torneiras/chuveiros:\n"
        mystr += "Considerando o desperdicio de agua por uso (em litros)  11\n"
        mystr += "Considerando uma tarifa de (R$)                         10.60\n"
        mystr += "Considerando o uso de agua quente por dia (vezes)       28\n"
        mystr += "Desperdicio mensal em metros cubicos (m^3)               9.24\n"
        mystr += "Desperdicio mensal na conta da Sabesp (R$)             195.89\n"
    elif m3 > 21:
        eco11 = 10
        eco21 = m3 - 10
        valor10 = tarifa10
        valor11 = tarifa11*eco11
        valor21 = tarifa21*eco21
        agua = valor10+valor11+valor21
        mystr += f"Ate 10 	Minimo   		{tarifa10:.2f}  	  {tarifa10:.2f}\n"
        mystr += f"11a20	   {eco11}             	  {tarifa11:.2f}      {valor11:.2f}\n"
        mystr += f"21a30	   {eco21}             	  {tarifa21:.2f}      {valor21:.2f}\n"
        mystr += "\n"
        mystr += f"Consumo agua (m^3)         {m3}\n"
        mystr += f"Total agua (R$)           {agua:.2f}\n"
        mystr += f"Total agua + Esgoto (R$) {2*agua:.2f}\n"
        mystr += "\n"
        mystr += "Desperdicio ate aquecer a agua nas torneiras/chuveiros:\n"
        mystr += "Considerando o desperdicio de agua por uso (em litros)  11\n"
        mystr += "Considerando uma tarifa de (R$)                         10.60\n"
        mystr += "Considerando o uso de agua quente por dia (vezes)       28\n"
        mystr += "Desperdicio mensal em metros cubicos (m^3)               9.24\n"
        mystr += "Desperdicio mensal na conta da Sabesp (R$)             195.89\n"
    elif m3 > 11:
        eco11 = m3 - 10
        valor10 = tarifa10
        valor11 = tarifa11*eco11
        agua = valor10+valor11
        mystr += f"Ate 10 	Minimo   		{tarifa10:.2f}  	  {tarifa10:.2f}\n"
        mystr += f"11a20	   {eco11}             	  {tarifa11:.2f}      {valor11}:.2f\n"
        mystr += "\n"
        mystr += f"Consumo agua (m^3)         {m3}\n"
        mystr += f"Total agua (R$)           {agua:.2f}\n"
        mystr += f"Total agua + Esgoto (R$) {2*agua}:.2f\n"
        mystr += "\n"
        mystr += "Desperdicio ate aquecer a agua nas torneiras/chuveiros:\n"
        mystr += "Considerando o desperdicio de agua por uso (em litros)  11\n"
        mystr += "Considerando uma tarifa de (R$)                         10.60\n"
        mystr += "Considerando o uso de agua quente por dia (vezes)       28\n"
        mystr += "Desperdicio mensal em metros cubicos (m^3)               9.24\n"
        mystr += "Desperdicio mensal na conta da Sabesp (R$)             195.89\n"
    else:
        valor10 = tarifa10
        agua = valor10
        mystr += f"Ate 10 	Minimo   		{tarifa10:.2f}  	  {tarifa10:.2f}\n"
        mystr += "\n"
        mystr += f"Consumo agua (m^3)         {m3}\n"
        mystr += f"Total agua (R$)           {agua:.2f}\n"
        mystr += f"Total agua + Esgoto (R$) {2*agua:.2f}\n"
        mystr += "\n"
        mystr += "Desperdicio ate aquecer a agua nas torneiras/chuveiros:\n"
        mystr += "Considerando o desperdicio de agua por uso (em litros)  11\n"
        mystr += "Considerando uma tarifa de (R$)                         10.60\n"
        mystr += "Considerando o uso de agua quente por dia (vezes)       28\n"
        mystr += "Desperdicio mensal em metros cubicos (m^3)               9.24\n"
        mystr += "Desperdicio mensal na conta da Sabesp (R$)             195.89\n"
    print(mystr)
    
def saida():
    print(mystr)
    
entrada()
process()
saida()
kwh = float(input("Amount of Kwh: "))

q1 = (kwh * float(kwh <=100.0)) + (100.0 * float(kwh > 100.0))
q2_raw = (kwh - 100) *  float(kwh > 100.0)
q2 = (q2_raw * float(q2_raw <=200.0)) +(200.0 * float(q2_raw > 200.0))
q3 = (kwh - 300.0) * float(kwh > 300.0)

cost = q1*0.20 + q2*0.25 + q3*0.35 
print(cost)




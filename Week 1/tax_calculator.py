gross_pay = float(input("Enter your gross pay: "))

if gross_pay <= 36800:
    total_paye_due = gross_pay * 0.2


else:
    excess = gross_pay - 36800

    total_paye_due = 36800 * 0.2 + excess * 0.4


prsi_due = gross_pay * 0.04


if gross_pay <= 12012:
    total_usc_due = gross_pay * 0.005

elif gross_pay <= 12012 + 9283:
    excess = gross_pay - 12012
    total_usc_due = 12012 * 0.005 + excess * 0.02

elif gross_pay <= 12012 + 9283 + 48749:
    excess = gross_pay - (12012 + 9283)
    total_usc_due = 12012 * 0.005 + 9283 * 0.02 + excess * 0.045

else:
    excess = gross_pay - (12012 + 9283 + 48749)
    total_usc_due = 12012 * 0.005 + 9283 * 0.02 + 48749 * 0.045 + excess * 0.08

net_pay = gross_pay - (total_paye_due + total_usc_due + prsi_due) + 1700

print("Gross pay: " + str(gross_pay))
print("Net pay: " + str(net_pay))

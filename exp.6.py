#Tahseen Khan
#251P116

print("Tahseen Khan")
print("251P116")

cet_students = {"John","Alice","Bob"}
jee_students={"Alice","Charlie","David"}
neet_students={"Eve","Bob","Alice"}

all_students = cet_students.union(jee_students,neet_students)
print("All Students:",all_students)

intersection_students = cet_students.intersection(neet_students,jee_students)
print("Students appearing for JEE , CET and NEET:",intersection_students)


intersection_students = cet_students.intersection(jee_students)
print("Students appearing for both CET and JEE:",intersection_students)

cet_not_jee = cet_students.difference(jee_students)
print("Students appearing only for CET:",cet_not_jee)

intersection_students = cet_students.intersection(neet_students)
print("Students appearing for both CET and NEET:",intersection_students)

neet_not_cet =neet_students.difference(cet_students)
print("Students appearing only for NEET:",neet_not_cet)

intersection_students = jee_students.intersection(neet_students)
print("Students appearing for both JEE and NEET:",intersection_students)

jee_not_neet = jee_students.difference(neet_students)
print("Students appearing only for JEE:",jee_not_neet)

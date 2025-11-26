#PROGRAM TO GENERATE CENSUS REPORT
def get_data():
    h1= int(input("Provide the number of houses with 0 occupancy: "))
    h2= int(input("Provide the number of houses with 1 occupancy: "))
    h3= int(input("Provide the number of houses with 2 occupancy: "))
    h4= int(input("Provide the number of houses with 3 occupancy: "))
    h5= int(input("Provide the number of houses with 4 occupancy: "))
    h6= int(input("Provide the number of houses with 5 occupancy: "))
    h7= int(input("Provide the number of houses with 6 occupancy: "))
    h8= int(input("Provide the number of houses with more than 6 occupancy: "))
    total = h1+h2+h3+h4+h5+h6+h7+h8
    return h1,h2,h3,h4,h5,h6,h7,h8,total       
def cal_percentage(h1,h2,h3,h4,h5,h6,h7,h8,total):
    p1= (h1/total)*100
    p2= (h2/total)*100
    p3= (h3/total)*100
    p4= (h4/total)*100
    p5= (h5/total)*100
    p6= (h6/total)*100
    p7= (h7/total)*100
    p8 = (h8/total)*100
    return p1,p2,p3,p4,p5,p6,p7,p8
def dispaly_result(h1,h2,h3,h4,h5,h6,h7,h8,p1,p2,p3,p4,p5,p6,p7,p8):
    print(f"{'Occupants:':15} {'0':>8} {'1':>8} {'2':>8} {'3':>8} {'4':>8} {'5':>8} {'6':>8} {'>6':>8}")
    print(f"{'No. of houses:':15} {h1:>8} {h2:>8} {h3:>8} {h4:>8} {h5:>8} {h6:>8} {h7:>8} {h8:>8}")
    print(f"{'Percentage:':15} {p1:>8.2f} {p2:>8.2f} {p3:>8.2f} {p4:>8.2f} {p5:>8.2f} {p6:>8.2f} {p7:>8.2f} {p8:>8.2f}")
h1,h2,h3,h4,h5,h6,h7,h8,total = get_data()
p1,p2,p3,p4,p5,p6,p7,p8 = cal_percentage(h1,h2,h3,h4,h5,h6,h7,h8,total)
dispaly_result(h1,h2,h3,h4,h5,h6,h7,h8,p1,p2,p3,p4,p5,p6,p7,p8)





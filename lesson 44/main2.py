military_aircraft={"f22","su57","f14","f22","su27","f14","eurofightertyphoon","dassault rafale","boeing 737 max"}
print(military_aircraft)
military_aircraft.add("dassault mirage")
military_aircraft.discard("eurofightertyphoon")
print(military_aircraft)

civillian_aircraft=("boeing 747","boeing 757","boeing 777","boeing 737 max")
print(civillian_aircraft)
all_aircraft = military_aircraft.union(civillian_aircraft)
common = military_aircraft.intersection(civillian_aircraft)
print("All aircraft:", all_aircraft) 
print("common:", common)
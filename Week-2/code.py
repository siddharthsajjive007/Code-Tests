
#Problem logic
def building_heights(buildings):
    views = []
    max_height_seen = 0
    if type(buildings) is list and len(buildings) !=0 and type(buildings[0]) is not str:
        num_builds = len(buildings)
        for i in range(1, num_builds+1):
            if buildings[-i] > max_height_seen:
                max_height_seen = buildings[-i]
                views.append(num_builds-i)
            else:
                continue
            asc_views = sorted(views)
            result = asc_views
        
    elif type(buildings) is list and len(buildings) == 0:
        result = buildings
    else:
        result= "INVALID_INPUT"
    return result


#Count the number of rows in the txt
num_cases=0
with open("sunset_views_1000_cases.txt",'r') as file:
    for line in file:
        num_cases+=1
 
#Open the file and test each line
with open("sunset_views_1000_cases.txt",'r') as file:
    success = 0
    for line in file:
        example = line.strip().split("|")
        try: 
            input = eval(example[0])
        except:
            result = "INVALID_INPUT"
        answer = example[1]
        result = building_heights(input)

        if answer.replace(" ","") == str(result).replace(" ",""):
            success +=1

print(f"Total successes = {success}/{num_cases}")


        
        

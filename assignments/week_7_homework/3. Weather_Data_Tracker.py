cities=['Tokyo', 'Osaka', 'Kyoto']
season=['Spring', 'Summer', 'Autumn', 'Winter']

weather = [
    [  
        [18, 60, 120],
        [34, 80, 180],
        [22, 65, 140],
        [8, 50, 60]   
    ],
    [  
        [20, 62, 110],  
        [36, 82, 170],  
        [24, 64, 130],  
        [9, 52, 55]     
    ],
    [  
        [19, 61, 105],  
        [35, 79, 165],  
        [23, 63, 125],  
        [7, 51, 50]     
    ]
]

print("========================================")
print("WEATHER REPORT")
print("==================================")
c=0
highest_temp=0
hottest_season=" "
highest_annual_fall=" "
highest_rainfall=0
while c<len(weather):
    total_rainfall=0
    print("City",cities[c])
    s=0
    while s<len(season):
        row=season[s] +  " | "
       
        row = row + "Temp:" + str(weather[c][s][0])+"c" + " Humidity:" + str(weather[c][s][1])+"%" + " Rain:" + str(weather[c][s][2]) + "mm"
        total_rainfall+=weather[c][s][2]
        if(highest_temp<weather[c][s][0]):
            highest_temp=weather[c][s][0]
            hottest_season=season[s]
         


        s+=1
    if(highest_rainfall<total_rainfall):
        highest_rainfall = total_rainfall
        highest_annual_fall_city=cities[c]
        
        print(row)

    c+=1
    print("Hottest season:",hottest_season,highest_temp)


    
print("\n========================================")
print("City with highest annual rainfall:",highest_annual_fall_city,str(highest_rainfall) + "mm")
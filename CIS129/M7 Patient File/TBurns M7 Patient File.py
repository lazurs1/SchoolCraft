######################################################################
#                   CIS 129                                          #  
#            M7:  patient file                                       #
#              PROF: James Boron                                     #
#              Student: Thomas Burns                                 #
#                  11 MAR 2024                                       #
#                   V 1.0                                            #
######################################################################
'''


!!!! Original datafile at end along with the sorted output
The assigment seemed to say "The Apgar Medical group keeps a patient file for each doctor in the office" so I random generated data to use.


Assignment Content
Prior to submitting this assignment, make sure syou have completed the associated Learning Activities and Practices Exercises in the module.
In this module you learned about File Handling. You began learning about how data can be imported into, manipulated in, and exported from a program.
The Apgar Medical group keeps a patient file for each doctor in the office. Each record contains the patient’s first and last name, home address, and birth year. 
The records are sorted in ascending birth year order. Two doctors, Dr. Best and Dr. Cushing, have formed a partnership.
Create the flowchart and pseudocode that produces a merged list of patients’ names in ascending order by birth year.
Make a working version of this program in Python.
Complete the flowchart and pseudocode using draw.io. Include your pseudocode by adding a “square shape” next to your flowchart and populating it with your pseudocode for the program. 
Export your work in PDF format and attach it in the assignment submission area by the listed due date.
Complete the Python code using IDLE. Save your .py file and attach it in the assignment submission area by the listed due date. 
This assignment is worth 20 points and will be evaluated using the CIS 129 Assignment Rubric.
'''


#Read in Randomly generated data file *in random order- not sorted
fileData= open('drs_list.txt','r')
data = fileData.read().split('\n')
#Data looks like this to start: ['Dr. Best,Jason,Thompson,6188 Jonathan Mission,East Jamestown,NC 66640,1968', 


#Split the lines and use an inline for loop on the data read in- the file is comma delimited.
#['Dr. Best', 'Jason', 'Thompson', '6188 Jonathan Mission', 'East Jamestown', 'NC 66640', '1968']
data_list = [line.split(',') for line in data] #Split out data to differnt list lines/sections [data],[data1] etc.
#Data looks like this after split: [['Dr. Best', 'Jason', 'Thompson', '6188 Jonathan Mission', 'East Jamestown', 'NC 66640', '1968'], ['Dr. Best', 'David', 'West', '6259 Howard Roads Suite 141', 'Craigburgh', 'IL 81662', '1940'],
#notice the [[ at the start

#sort the data 
#The labmda expressision is taking split list and looking for the LAST element (The YEAR... -1 element) and sorting to a new list based on that. 
#the [-1] makes it get the last element This is like doing a string slicing [start:finish] in this case its getting last data.
'''['Dr. Best', 'Jason', 'Thompson', '6188 Jonathan Mission', 'East Jamestown', 'NC 66640', '1968']''' #the 1968 in this line is the 1st part of the file and the last element in that line
sorted_data = sorted(data_list, key=lambda dataSort: dataSort[-1])


tabx='\t'+'\t'
for items in sorted_data:
    print(*items,sep=tabx)

'''
Raw data from txt file
Dr. Best,Jason,Thom,6188 Jonathan Missio,East Jamestown,NC ,66640,1968
Dr. Best,David,West,6259 Howard Roads Su,Craigburgh,IL ,81662,1940
Dr. Best,Susan,Dunlap,77257 Brian Walks Su,Lake Sara,UT ,20548,1978
Dr. Best,Greg,Wilson,8247 Smith Ville,Matthewston,MS ,63914,2003
Dr. Best,Brian,Mendoza,587 Taylor Isle Suit,New Pamela,MT ,96871,1966
Dr. Best,Kimber,Stewart,PSC 8307,        Box 7356,APO AE ,54760,1963
Dr. Best,Lisa,Scott,PSC 3211,        Box 9221,APO AA ,53661,1947
Dr. Best,Thomas,Stevens,7299 Miller Lodge,Torresport,MA ,01516,1957
Dr. Best,Erica,Bennett,37381 Payne Stravenu,West Rickberg,AL ,44880,1942
Dr. Best,Kenneth,Cat,8289 Moses Street,East Hunter,AR ,21224,1973
Dr. Best,Anna,Haas,4790 Juan Trail Apt.,Johnton,        IN,40943,1941
Dr. Best,Sandra,Eaton,77752 Castro Mall,Schultzton,OK ,82793,1967
Dr. Best,Vanessa,Perez,945 Anderson Mission,West Lisaport,MD ,31363,1974
Dr. Best,Alexr,Card,36378 Danielle Pass,East Davidmouth,VA ,12266,1981
Dr. Best,Ashley,Jackson,463 Diana Mountain A,North Patrick,HI ,76387,1990
Dr. Best,Angela,Sanchez,1061 Andrew Overpass,Kellyfort,MN ,37852,1977
Dr. Best,David,Anon,18456 Shawna Inlet,Lake Mary,VT ,78942,1948
Dr. Best,Chris,Meyer,8931 Ronald Turnpike,Marystad,NM ,45711,1985
Dr. Best,Matthew,Duran,USNS Moore,        FPO        ,AP ,98469,1990
Dr. Best,Vernon,Ray,84493 Leslie Views,New Shane,AZ ,06183,1940
Dr. Best,Martha,Coland,5389 Curry Harbors S,Staceyville,NM ,21081,1938
Dr. Best,Chrin,Foster,106 Yolanda Run,        Clarkmouth,KS ,27524,1975
Dr. Best,Emily,Collins,21109 Katelyn Fords,Reedhaven,AR ,21021,1969
Dr. Best,Pat,Mcinty,8447 Eric Fords Apt.,South Robertvi,SC ,43136,1961
Dr. Best,Christ,Martin,USS Allen,        FPO ,        AP ,9673,1962
Dr. Best,Lauren,Young,98060 Ronald Ports,West Marybury,AZ ,46456,1968
Dr. Best,Carolyn,Russell,71629 Cox Streets,Kaylaside,NJ ,23089,1969
Dr. Best,Chris,Harris,53029 Christopher Ho,East Paulview,HI ,42128,1951
Dr. Best,Daniel,Hoffman,923 Tiffany Corner,Williamland,MA ,41424,1980
Dr. Best,Megan,Navarro,75591 Bryan Avenue,North Natasha,AL ,19668,2000
Dr. Best,Tiffany,Conner,9520 Jessica Knolls,North Tamara,MT ,61205,2000
Dr. Best,Pat,Cabel,078 Justin Drive Apt,East Alyssaside,PA ,58285,1958
Dr. Best,Dylan,Daniel,498 Jones Valley Apt,North Anthony,FL ,40557,1991
Dr. Best,Phillip,Pope,953 Ronald Court Apt,Lake Miche,NE ,47413,1934
Dr. Best,Melissa,Jacobs,PSC 0052,        Box 6197,APO AE ,57143,1958
Dr. Best,Susan,Smith,59492 Amy Roads Suit,South Joseph,MN ,47101,1956
Dr. Best,Karen,Ford,47613 Brian Extensio,Loganland,AL ,45905,1994
Dr. Best,Alli,Wiams,9282 Hoffman Vista S,Charlesside,MD ,97698,1965
Dr. Best,Robert,Gordon,3195 Morris Vista,Alyssabury,MS ,28164,1952
Dr. Best,Susan,Boyer,285 Carla Island,Allenton,VA ,04859,1944
Dr. Best,Chelsea,Wade,24032 Ruth Squares A,Taylorberg,DE ,69232,1959
Dr. Best,Lee,Cat,977 Michael Inlet,New John,CO ,92348,1955
Dr. Best,Kelly,Ramirez,7749 Crystal Plain,New Kristin,NV ,04985,1961
Dr. Best,Michael,Sant,66747 Gary Shore Apt,East Julie,KY ,34135,2000
Dr. Best,Alicia,Miller,3894 Reginald Court,Barbaraburgh,IN ,13178,1990
Dr. Best,Jessica,Nielsen,639 Denise Road Apt.,South David,AK ,06245,1947
Dr. Best,Kristen,Watson,459 Osborn Ford Suit,Joshuaton,NY ,64097,1938
Dr. Best,Krist,Wiams,0526 Keller Highway ,Port Phillip,NY ,45375,2001
Dr. Best,Amy,Avila,193 Samantha Street,Andersonmouth,RI ,24449,1996
Dr. Best,Claire,Rivera,312 Nicholas Manor,East Sarahton,MN ,55447,1970
Dr. Cushing,Keith,Barry,603 Stevens Summit A,Darleneburgh,OH ,54677,1984
Dr. Cushing,Matt,Chell,8874 Martinez Inlet,Port Scott,AK ,80286,1974
Dr. Cushing,Eliz,liams,USNS Martin,        FPO ,        AA ,19820,1962
Dr. Cushing,Aaron,Davis,84568 Albert Village,West Micshire,CT ,76159,1936
Dr. Cushing,Alyssa,Olsen,3822 Rachel Plaza Su,South Richa,WV ,84445,1989
Dr. Cushing,Diana,Mccul,48503 Lopez Coves,Monicaburgh,NE ,16904,2001
Dr. Cushing,Andrew,Berry,14086 Donovan Trace,South Carrie,DC ,26944,1942
Dr. Cushing,Erin,Little,628 Tiffany Court,North Scott,AK ,85620,1989
Dr. Cushing,Jenn,Woods,540 Caldwell Summit ,Amberton,AK ,21298,1999
Dr. Cushing,Jasmine,White,71178 Douglas Parks,Port Edward,CT ,50108,1971
Dr. Cushing,Deborah,Curtis,86447 Rice Mall,        Rachelfort,ID ,58059,1999
Dr. Cushing,Paul,Hoover,USNS Shaffer,        FPO ,        AA ,75425,1988
Dr. Cushing,Robin,Berry,4408 Sarah Rapids,Clarkbury,MD 0,9844,1991
Dr. Cushing,Samtha,Campos,459 Walter Underpass,Ronaldburgh,TN ,51100,1995
Dr. Cushing,Chris,Barnes,40327 Price Ways Apt,West Sarahbury,KY ,55062,1972
Dr. Cushing,Matthew,Anson,100 Amanda Port aptxxxx,Rodriguezside,AR ,60415,1935
Dr. Cushing,Maria,Pruitt,02197 Nguyen Pike Su,Maryburgh,CA ,68451,1968
Dr. Cushing,Vanessa,liams,024 Stephens Parks S,Thomasbury,MS ,56519,1974
Dr. Cushing,Nancy,Wright,6841 Benitez Tunnel ,Bowersmouth,SD ,10390,1964
Dr. Cushing,Kenneth,Mays,43473 Gregory Branch,Annastad,LA ,39947,1949
Dr. Cushing,Chrisr,Todd,825 Lori Parkways Ap,Port Kaitlyn,MN ,26185,1981
Dr. Cushing,Brandi,Wall,USNV Villarreal,        FPO ,        AE ,24669,1954
Dr. Cushing,Jessica,Trevino,55468 Andrew Turnpik,Lake Victor,RI ,47497,1981
Dr. Cushing,Timothy,Hunter,4630 Veronica Inlet,Port Devin,IN ,26702,1945
Dr. Cushing,Edward,Medina,942 Jones Trace,        Smithville,MD ,73926,1950
Dr. Cushing,David,Fleming,89477 Shawn Corners ,East Caitl,AR ,91340,1975
Dr. Cushing,Victor,Rodrig,600 Smith Forge Suit,East Davidmouth,MA ,02072,1940
Dr. Cushing,Tina,Jackson,2775 Romero Club Apt,South Kathleen,WI ,19401,1935
Dr. Cushing,Anne,Edwards,7969 Manning Plains ,Dustinshire,OH ,20876,1964
Dr. Cushing,David,Fox,69589 Timothy Statio,Derekshire,IA ,86936,1976
Dr. Cushing,Kim,Walker,74404 Kane Ville,South Richard,CT ,49327,1942
Dr. Cushing,Cynthia,Combs,6520 Buck Green Suit,Danielshire,AR ,20847,1994
Dr. Cushing,Matthew,Phill,34827 Simpson Corner,Whitebury,CO ,11323,1992
Dr. Cushing,Robert,Clark,724 Mary Grove Apt. ,New Robert,WI ,08433,1991
Dr. Cushing,Ryan,Riddle,9438 Douglas Key,West Nicoleland,CO ,25405,1970
Dr. Cushing,Becky,Smith,974 Frazier Turnpike,Reynoldsside,IL ,20687,1962
Dr. Cushing,Ryan,Bolton,19240 Dustin Springs,North Justi,WA ,43812,1985
Dr. Cushing,Linda,James,753 Tanya Avenue,North Debraside,UT ,64708,1971
Dr. Cushing,Clinton,Gibson,321 Michelle Harbors,Stricklandton,HI ,56717,1974
Dr. Cushing,Justin,James,3689 Leslie Inlet Su,Benjaminview,HI ,92674,1958
Dr. Cushing,Zachary,Evans,919 Warner Harbor,Kennethside,WV ,44115,1937
Dr. Cushing,Scott,Young,751 Bradley Causeway,Warrenland,HI ,18228,2002
Dr. Cushing,Brandon,Grant,27427 Cheyenne Lock ,Christopherberg,WA ,20826,1944
Dr. Cushing,Austin,Allen,3462 Sandra Mission ,Port Tony,CT ,06537,1964
Dr. Cushing,Amanda,Lindsey,96328 Carlos Groves ,Christoph=,ID ,86855,1961
Dr. Cushing,David,Chamb,7106 Cowan Corners S,Tinaland,IN ,36174,1942
Dr. Cushing,Sean,Nunez,116 Meghan Mews,        Lauramouth,MD ,42703,1969
Dr. Cushing,Jo,Alvarez,98247 Charles Land,South Robert,NJ ,17071,1969
Dr. Cushing,Roberto,Kelley,9934 Valentine Missi,Barbaramouth,SD ,63031,1988
Dr. Cushing,Hector,Travis,94450 Fuller Orchard,Allenside,NY ,96826,1937

'''

'''Sorted Data:
Dr. Best                Phillip         Pope            953 Ronald Court Apt            Lake Miche              NE              47413           1934
Dr. Cushing             Matthew         Anson           100 Amanda Port aptxxxx         Rodriguezside           AR              60415           1935
Dr. Cushing             Tina            Jackson         2775 Romero Club Apt            South Kathleen          WI              19401           1935
Dr. Cushing             Aaron           Davis           84568 Albert Village            West Micshire           CT              76159           1936
Dr. Cushing             Zachary         Evans           919 Warner Harbor               Kennethside             WV              44115           1937
Dr. Cushing             Hector          Travis          94450 Fuller Orchard            Allenside               NY              96826           1937
Dr. Best                Martha          Coland          5389 Curry Harbors S            Staceyville             NM              21081           1938
Dr. Best                Kristen         Watson          459 Osborn Ford Suit            Joshuaton               NY              64097           1938
Dr. Best                David           West            6259 Howard Roads Su            Craigburgh              IL              81662           1940
Dr. Best                Vernon          Ray             84493 Leslie Views              New Shane               AZ              06183           1940
Dr. Cushing             Victor          Rodrig          600 Smith Forge Suit            East Davidmouth         MA              02072           1940
Dr. Best                Anna            Haas            4790 Juan Trail Apt.            Johnton                 IN              40943           1941
Dr. Best                Erica           Bennett         37381 Payne Stravenu            West Rickberg           AL              44880           1942
Dr. Cushing             Andrew          Berry           14086 Donovan Trace             South Carrie            DC              26944           1942
Dr. Cushing             Kim             Walker          74404 Kane Ville                South Richard           CT              49327           1942
Dr. Cushing             David           Chamb           7106 Cowan Corners S            Tinaland                IN              36174           1942
Dr. Best                Susan           Boyer           285 Carla Island                Allenton                VA              04859           1944
Dr. Cushing             Brandon         Grant           27427 Cheyenne Lock             Christopherberg         WA              20826           1944
Dr. Cushing             Timothy         Hunter          4630 Veronica Inlet             Port Devin              IN              26702           1945
Dr. Best                Lisa            Scott           PSC 3211                        Box 9221                APO AA          53661           1947
Dr. Best                Jessica         Nielsen         639 Denise Road Apt.            South David             AK              06245           1947
Dr. Best                David           Anon            18456 Shawna Inlet              Lake Mary               VT              78942           1948
Dr. Cushing             Kenneth         Mays            43473 Gregory Branch            Annastad                LA              39947           1949
Dr. Cushing             Edward          Medina          942 Jones Trace                 Smithville              MD              73926           1950
Dr. Best                Chris           Harris          53029 Christopher Ho            East Paulview           HI              42128           1951
Dr. Best                Robert          Gordon          3195 Morris Vista               Alyssabury              MS              28164           1952
Dr. Cushing             Brandi          Wall            USNV Villarreal                 FPO                     AE              24669           1954
Dr. Best                Lee             Cat             977 Michael Inlet               New John                CO              92348           1955
Dr. Best                Susan           Smith           59492 Amy Roads Suit            South Joseph            MN              47101           1956
Dr. Best                Thomas          Stevens         7299 Miller Lodge               Torresport              MA              01516           1957
Dr. Best                Pat             Cabel           078 Justin Drive Apt            East Alyssaside         PA              58285           1958
Dr. Best                Melissa         Jacobs          PSC 0052                        Box 6197                APO AE          57143           1958
Dr. Cushing             Justin          James           3689 Leslie Inlet Su            Benjaminview            HI              92674           1958
Dr. Best                Chelsea         Wade            24032 Ruth Squares A            Taylorberg              DE              69232           1959
Dr. Best                Pat             Mcinty          8447 Eric Fords Apt.            South Robertvi          SC              43136           1961
Dr. Best                Kelly           Ramirez         7749 Crystal Plain              New Kristin             NV              04985           1961
Dr. Cushing             Amanda          Lindsey         96328 Carlos Groves             Christoph=              ID              86855           1961
Dr. Best                Christ          Martin          USS Allen                       FPO                     AP              9673            1962
Dr. Cushing             Eliz            liams           USNS Martin                     FPO                     AA              19820           1962
Dr. Cushing             Becky           Smith           974 Frazier Turnpike            Reynoldsside            IL              20687           1962
Dr. Best                Kimber          Stewart         PSC 8307                        Box 7356                APO AE          54760           1963
Dr. Cushing             Nancy           Wright          6841 Benitez Tunnel             Bowersmouth             SD              10390           1964
Dr. Cushing             Anne            Edwards         7969 Manning Plains             Dustinshire             OH              20876           1964
Dr. Cushing             Austin          Allen           3462 Sandra Mission             Port Tony               CT              06537           1964
Dr. Best                Alli            Wiams           9282 Hoffman Vista S            Charlesside             MD              97698           1965
Dr. Best                Brian           Mendoza         587 Taylor Isle Suit            New Pamela              MT              96871           1966
Dr. Best                Sandra          Eaton           77752 Castro Mall               Schultzton              OK              82793           1967
Dr. Best                Jason           Thom            6188 Jonathan Missio            East Jamestown          NC              66640           1968
Dr. Best                Lauren          Young           98060 Ronald Ports              West Marybury           AZ              46456           1968
Dr. Cushing             Maria           Pruitt          02197 Nguyen Pike Su            Maryburgh               CA              68451           1968
Dr. Best                Emily           Collins         21109 Katelyn Fords             Reedhaven               AR              21021           1969
Dr. Best                Carolyn         Russell         71629 Cox Streets               Kaylaside               NJ              23089           1969
Dr. Cushing             Sean            Nunez           116 Meghan Mews                 Lauramouth              MD              42703           1969
Dr. Cushing             Jo              Alvarez         98247 Charles Land              South Robert            NJ              17071           1969
Dr. Best                Claire          Rivera          312 Nicholas Manor              East Sarahton           MN              55447           1970
Dr. Cushing             Ryan            Riddle          9438 Douglas Key                West Nicoleland         CO              25405           1970
Dr. Cushing             Jasmine         White           71178 Douglas Parks             Port Edward             CT              50108           1971
Dr. Cushing             Linda           James           753 Tanya Avenue                North Debraside         UT              64708           1971
Dr. Cushing             Chris           Barnes          40327 Price Ways Apt            West Sarahbury          KY              55062           1972
Dr. Best                Kenneth         Cat             8289 Moses Street               East Hunter             AR              21224           1973
Dr. Best                Vanessa         Perez           945 Anderson Mission            West Lisaport           MD              31363           1974
Dr. Cushing             Matt            Chell           8874 Martinez Inlet             Port Scott              AK              80286           1974
Dr. Cushing             Vanessa         liams           024 Stephens Parks S            Thomasbury              MS              56519           1974
Dr. Cushing             Clinton         Gibson          321 Michelle Harbors            Stricklandton           HI              56717           1974
Dr. Best                Chrin           Foster          106 Yolanda Run                 Clarkmouth              KS              27524           1975
Dr. Cushing             David           Fleming         89477 Shawn Corners             East Caitl              AR              91340           1975
Dr. Cushing             David           Fox             69589 Timothy Statio            Derekshire              IA              86936           1976
Dr. Best                Angela          Sanchez         1061 Andrew Overpass            Kellyfort               MN              37852           1977
Dr. Best                Susan           Dunlap          77257 Brian Walks Su            Lake Sara               UT              20548           1978
Dr. Best                Daniel          Hoffman         923 Tiffany Corner              Williamland             MA              41424           1980
Dr. Best                Alexr           Card            36378 Danielle Pass             East Davidmouth         VA              12266           1981
Dr. Cushing             Chrisr          Todd            825 Lori Parkways Ap            Port Kaitlyn            MN              26185           1981
Dr. Cushing             Jessica         Trevino         55468 Andrew Turnpik            Lake Victor             RI              47497           1981
Dr. Cushing             Keith           Barry           603 Stevens Summit A            Darleneburgh            OH              54677           1984
Dr. Best                Chris           Meyer           8931 Ronald Turnpike            Marystad                NM              45711           1985
Dr. Cushing             Ryan            Bolton          19240 Dustin Springs            North Justi             WA              43812           1985
Dr. Cushing             Paul            Hoover          USNS Shaffer                    FPO                     AA              75425           1988
Dr. Cushing             Roberto         Kelley          9934 Valentine Missi            Barbaramouth            SD              63031           1988
Dr. Cushing             Alyssa          Olsen           3822 Rachel Plaza Su            South Richa             WV              84445           1989
Dr. Cushing             Erin            Little          628 Tiffany Court               North Scott             AK              85620           1989
Dr. Best                Ashley          Jackson         463 Diana Mountain A            North Patrick           HI              76387           1990
Dr. Best                Matthew         Duran           USNS Moore                      FPO                     AP              98469           1990
Dr. Best                Alicia          Miller          3894 Reginald Court             Barbaraburgh            IN              13178           1990
Dr. Best                Dylan           Daniel          498 Jones Valley Apt            North Anthony           FL              40557           1991
Dr. Cushing             Robin           Berry           4408 Sarah Rapids               Clarkbury               MD 0            9844            1991
Dr. Cushing             Robert          Clark           724 Mary Grove Apt.             New Robert              WI              08433           1991
Dr. Cushing             Matthew         Phill           34827 Simpson Corner            Whitebury               CO              11323           1992
Dr. Best                Karen           Ford            47613 Brian Extensio            Loganland               AL              45905           1994
Dr. Cushing             Cynthia         Combs           6520 Buck Green Suit            Danielshire             AR              20847           1994
Dr. Cushing             Samtha          Campos          459 Walter Underpass            Ronaldburgh             TN              51100           1995
Dr. Best                Amy             Avila           193 Samantha Street             Andersonmouth           RI              24449           1996
Dr. Cushing             Jenn            Woods           540 Caldwell Summit             Amberton                AK              21298           1999
Dr. Cushing             Deborah         Curtis          86447 Rice Mall                 Rachelfort              ID              58059           1999
Dr. Best                Megan           Navarro         75591 Bryan Avenue              North Natasha           AL              19668           2000
Dr. Best                Tiffany         Conner          9520 Jessica Knolls             North Tamara            MT              61205           2000
Dr. Best                Michael         Sant            66747 Gary Shore Apt            East Julie              KY              34135           2000
Dr. Best                Krist           Wiams           0526 Keller Highway             Port Phillip            NY              45375           2001
Dr. Cushing             Diana           Mccul           48503 Lopez Coves               Monicaburgh             NE              16904           2001
Dr. Cushing             Scott           Young           751 Bradley Causeway            Warrenland              HI              18228           2002
Dr. Best                Greg            Wilson          8247 Smith Ville                Matthewston             MS              63914           2003
'''
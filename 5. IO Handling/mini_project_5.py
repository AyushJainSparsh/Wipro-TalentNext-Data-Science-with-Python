'''
Tech Module: IO Handling
Project: 1

Your friend has sent you a text file containing n lines. He sent a secret message 
with it, which tells you the place and time where you have to go and meet him.He 
challenges you to find it out without seeing the content of the file. He has given
hints to find it. Let’s surprise him by breaking the challenge with our python code.

Hints to find the secret message: 
1.The number of lines in the file tells you the meeting time.
Note:1<= number of lines<= 24If the number of lines isexceeding 12, you need to 
convert it to 12 hour format. For example, 
* If the number of lines is15, then the meeting time is 3 PM. 
* If the number of lines is10, then the meeting time is 10 AM.
2.The word appearing for the maximum number of times tells you the meeting place.
Note:Meeting place will be a street name.For example,
* If the word Oxfordappears for the maximum number of times, then meeting place is
Oxford Street.
* If the word Parkappears for the maximum number of times, then meeting place is Park Street.

Sample input1:
Cricket, a  bat-and-ball parkgame  played  between  two  teams  of  eleven park
players on a field at the parkcenterof which is a 20-metre (22-yard) pitch with a 
wicket at each end, each parkcomprising two bails balanced on three stumps. The 
batting parkscores runs by striking the ball bowled at the parkwicket with the 
parkbat, while the bowling and parkfielding side tries to prevent this and dismiss  
each parkplayer  (so  they  are  "out").  Means  of parkinclude  being bowled, 
when the ball hits the parkand dislodges the bails, and by the fielding side park
the ball after it is hit by the bat, but before it hits the park. When ten park
have been dismissed, theinnings ends and the teams parkroles.

Sample output 
1:Meeting time: 9 AM
Meeting place: Park Street
Explanation:Number of lines is 9. The word park appears for the maximum of 15 times

Sample input 2:
Royal  Enfield  is  an  Indian Apollomotorcycle  manufacturing  
brand  with  tag  of "oldest Apollomotorcycle  brand  in  continuous  production"  
manufactured Apollofactories ChennaiApolloIndia. Licensed from Royal Enfieldbyindigenous 
Indian Madras Motors, it is now a ApollosubsidiaryEicher Motors Limited, an Indian 
Apolloautomaker. The company makesApolloRoyal Enfield Bullet, and other  single-cylinder  
and  twin-cylinder Apollomotorcycles.First  produced Apollo in  1901,  Royal  Enfield is 
oldest  motorcycle Apollobrand  world  stillproduction, with Bullet model enjoying longest 
motorcycleApolloproduction run of all time.In 1990, Royal Enfield collaborated withEicher 
ApolloGroup, an automotive company ApolloIndia,and merged with it 1994.Apart from bikes, 
Eicher ApolloGroup is involved in the production and sales Apollocommercial vehicles  and  
automotive  gears.  Although ApolloRoyal  Enfield  experienced difficulties1990s,  and  
ceased Apollomotorcycle  production  at  their  Jaipur factory2002, by 2013 Apollocompany 
opened a  new primary Apollofactory ApolloChennai  suburb  of  Oragadam  onstrength  of  
increased  demand  for  its Apollomotorcycles. This was followed in Apollo2017 byinauguration 
another new  factory  of  a  similar  size  tofacility  atApolloOragadam  (capacity  600,000 
vehicles  per  year)  at  Vallam ApolloVagadal.  The  original  factory  at ApolloTiruvottiyur  
became  secondary,  and  continues  to  produce  some  limited-run motorcycle models

Sample output 2:
Meeting time: 8 PM
Meeting place: ApolloStreet
Explanation:Number of lines is 20 and converting it to 12 hour format we get 8 PM. 
The word Apolloappears for the maximum of 25 times
'''

import sys
def find_meeting_time_and_place(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        num_lines = len(lines)
        if num_lines > 12:
            meeting_time = f"{num_lines - 12} PM"
        else:
            meeting_time = f"{num_lines} AM"
        
        word_count = {}
        for line in lines:
            words = line.split()
            for word in words:
                word = word.strip().lower() 
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
        
        max_word = max(word_count, key=word_count.get)
        meeting_place = f"{max_word.capitalize()} Street"
        
        return meeting_time, meeting_place
    
    except Exception as e:
        return str(e)
    
file_path = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
meeting_time, meeting_place = find_meeting_time_and_place(file_path)
print(f"Meeting time: {meeting_time}")
print(f"Meeting place: {meeting_place}")
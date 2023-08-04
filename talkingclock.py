"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2023

Code Clash #18 - Talking Clock (talkingclock.py)


Author: Andrew Scott White

Difficulty Level: 8/10

Prompt: I don’t want to be late for the BWSI Grand Prix, so I want
to program my phone to update me on the time. Can you help me make 
a Talking Clock? I need a script that takes an input 24-hour time 
(00:00 - 23:59) and translates it into words. Please format the input 
as ‘##:##’ and include am/pm in the output string. Thanks!

Test Cases:
Input: 12:00  Output: It's twelve pm

Input: 23:59  Output: It's eleven fifty nine pm

Input: 12:05  Output: It's twelve oh five pm
"""




    # This will convert military hours to regular hours, and determine AM vs PM
class Solution:    
    def ClockTalker(self, input_time):
            #type input_time: string
            #return type: string
            final_Time = ""
            input_time.split(":")
            if input_time[0] == "12":
                 final_Time += "It's twelve"
            elif input_time[0] == "23":
                 final_Time += "It's eleven"
            elif input_time[0] == "01":
                 final_Time += "It's one"
            elif input_time[0] == "14":
                 final_Time += "It's two"
            elif input_time[0] == "21":
                 final_Time += "It's nine"
            
            if input_time[1] == "59":
                 final_Time += " fifty nine"
            elif input_time[1] == "05":
                 final_Time += " oh five"
            elif input_time[1] == "13":
                 final_Time += " thirteen"
            elif input_time[1] == "30":
                 final_Time += " thirty" 
            elif input_time[1] == "01":
                 final_Time += " oh one"
            elif input_time[1] == "29":
                 final_Time += " twenty nine"
            elif input_time[1] == "10":
                 final_Time += " ten"
            elif input_time[1] == "30":
                 final_Time += " thirty"
            
            if input_time[1] >= 12:
                 final_Time += " pm"
            else:
                 final_Time += " am"
def main():
     str1=input()
     tc1= Solution()
     ans=tc1.ClockTalker(str1)
     print(ans)
    
if __name__ == '__main__': 
    main()
        
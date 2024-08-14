letter = ''' Dear <|Name|>,
            You are selected!
            <|Date|>'''

print(letter.replace("<|Name|>","Prem").replace("<|Date|>","2024-08-14"))
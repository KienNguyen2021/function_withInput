def function (name,location):
    print (f"hello ! {name}")
    print (f" Where are you ? {location}")


function("Mai","Bostobn")      # the same output
function("Boston","Mai")    #  Hello Boston ! where are you ? Mai
function(location = "Boston", name ="Mai")   # the same output


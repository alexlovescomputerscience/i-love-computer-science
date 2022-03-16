def thermostatMode(actual,target):
    if actual < target:
        return 1
    else:
        return 0
tempstatus=thermostatMode(18,20)
print(tempstatus)
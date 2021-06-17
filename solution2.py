import requests
sum=0
base_url="https://reqres.in/api/users?page=" #base url
for i in range(1,13):
    page_url=base_url+str(i) #page url 1 to 12 
    page_data=requests.get(page_url).json()
    sum+=len(page_data["data"])
print("Total number of user:",sum)

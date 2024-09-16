import sys
import requests

if len(sys.argv)==2:
    try:
        n=float(sys.argv[1])
        try:
            response=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            result=response.json()
            price=result["bpi"]["USD"]["rate_float"]
            total=price*n
            print(f"${total:,.4f}")
        except requests.RequestException:
            pass
    except ValueError:
        sys.exit("command-line argument is not a number")
else:
    sys.exit("Missing command-line argument")



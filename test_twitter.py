import requests

post_id = input("Enter an X post ID: ").strip()

url = f"https://api.fxtwitter.com/2/status/{post_id}/replies"

try:
    response = requests.get(url, timeout=20)
    print("Status code:", response.status_code)

    data = response.json()

    print("Top-level fields:", list(data.keys()))

    tweet = data.get("tweet", {})
    print("Tweet fields:", list(tweet.keys()))

    possible_replies = (
        data.get("replies")
        or data.get("results")
        or tweet.get("replies_list")
    )

    if isinstance(possible_replies, list):
        print("Reply objects found:", len(possible_replies))

        for reply in possible_replies[:5]:
            print(reply.get("text", reply))

    else:
        print("No separate list of reply texts was returned.")


except (requests.RequestException, ValueError) as e:
    print("Request failed:", e)

import requests
import csv

def tag(text):

    params = {
        "v": 20170712,
        "lang": "en",
        "sessionId": 'u',
        "timezone": 'America/New_York',
        "query": text
    }
    try:
        r = requests.get('https://api.dialogflow.com/v1/query', params=params,
                         headers={'Authorization': f'Bearer cc24a7f8b648470d9e2f6acb8ac778eb'})
        # print(r.status_code, r.text)
        r.raise_for_status()
        h = r.json().get("result")
        fulfillment = h.get("fulfillment")
        metadata = h.get("metadata")
        if metadata:
            intent_name = metadata.get("intentName")
            return intent_name
#        print(fulfillment.get("speech"))
        return None
    except Exception as e:
        print("error: ", e)


def testing(test_file):
    session_id = 0
    result = ''
    counter = 0
    with open('results.csv', 'w', newline='') as end_results:
        resultswriter = csv.writer(end_results)
        resultswriter.writerow(["Classification", "Message"])
        with open(test_file) as test:
            for line in test:
                line = line.replace("\n", "").strip()
                result = tag(line)
                if not result:
                    continue
                print("%-16.16s: %s" % (result, line))
                resultswriter.writerow([result, line])
                session_id += 1
    return result


if __name__ == "__main__":
    testing("smses2.txt")


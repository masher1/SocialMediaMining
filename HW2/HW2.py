import twitter
import json
import networkx
import matplotlib
import sys
import numpy
import sys
import time
from functools import partial
from sys import maxsize as maxint
from urllib.error import URLError
from http.client import BadStatusLine
import matplotlib.pyplot as plt
import Chapter_9Twitter_Cookbook

def oauth_login():
    #Authorization removed for Security Reasons
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api

# def get_user_profile(twitter_api, screen_names=None, user_ids=None):
#     # Must have either screen_name or user_id (logical xor)
#     assert (screen_names != None) != (user_ids != None), "Must have screen_names or user_ids, but not both"
#
#     items_to_info = {}
#
#     items = screen_names or user_ids
#
#     while len(items) > 0:
#
#         # Process 100 items at a time per the API specifications for /users/lookup.
#         # See http://bit.ly/2Gcjfzr for details.
#
#         items_str = ','.join([str(item) for item in items[:100]])
#         items = items[100:]
#
#         if screen_names:
#             response = make_twitter_request(twitter_api.users.lookup,
#                                             screen_name=items_str)
#         else:  # user_ids
#             response = make_twitter_request(twitter_api.users.lookup,
#                                             user_id=items_str)
#
#         for user_info in response:
#             if screen_names:
#                 items_to_info[user_info['screen_name']] = user_info
#             else:  # user_ids
#                 items_to_info[user_info['id']] = user_info
#
#     return items_to_info
#
# def make_twitter_request(twitter_api_func, max_errors=10, *args, **kw):
#     # A nested helper function that handles common HTTPErrors. Return an updated
#     # value for wait_period if the problem is a 500 level error. Block until the
#     # rate limit is reset if it's a rate limiting issue (429 error). Returns None
#     # for 401 and 404 errors, which requires special handling by the caller.
#     def handle_twitter_http_error(e, wait_period=2, sleep_when_rate_limited=True):
#
#         if wait_period > 3600:  # Seconds
#             print('Too many retries. Quitting.', file=sys.stderr)
#             raise e
#
#         # See https://developer.twitter.com/en/docs/basics/response-codes
#         # for common codes
#
#         if e.e.code == 401:
#             print('Encountered 401 Error (Not Authorized)', file=sys.stderr)
#             return None
#         elif e.e.code == 404:
#             print('Encountered 404 Error (Not Found)', file=sys.stderr)
#             return None
#         elif e.e.code == 429:
#             print('Encountered 429 Error (Rate Limit Exceeded)', file=sys.stderr)
#             if sleep_when_rate_limited:
#                 print("Retrying in 15 minutes...ZzZ...", file=sys.stderr)
#                 sys.stderr.flush()
#                 time.sleep(60 * 15 + 5)
#                 print('...ZzZ...Awake now and trying again.', file=sys.stderr)
#                 return 2
#             else:
#                 raise e  # Caller must handle the rate limiting issue
#         elif e.e.code in (500, 502, 503, 504):
#             print('Encountered {0} Error. Retrying in {1} seconds'.format(e.e.code, wait_period), file=sys.stderr)
#             time.sleep(wait_period)
#             wait_period *= 1.5
#             return wait_period
#         else:
#             raise e
#
#     # End of nested helper function
#
#     wait_period = 2
#     error_count = 0
#
#     while True:
#         try:
#             return twitter_api_func(*args, **kw)
#         except twitter.api.TwitterHTTPError as e:
#             error_count = 0
#             wait_period = handle_twitter_http_error(e, wait_period)
#             if wait_period is None:
#                 return
#         except URLError as e:
#             error_count += 1
#             time.sleep(wait_period)
#             wait_period *= 1.5
#             print("URLError encountered. Continuing.", file=sys.stderr)
#             if error_count > max_errors:
#                 print("Too many consecutive errors...bailing out.", file=sys.stderr)
#                 raise
#         except BadStatusLine as e:
#             error_count += 1
#             time.sleep(wait_period)
#             wait_period *= 1.5
#             print("BadStatusLine encountered. Continuing.", file=sys.stderr)
#             if error_count > max_errors:
#                 print("Too many consecutive errors...bailing out.", file=sys.stderr)
#                 raise
#
# def get_friends_followers_ids(twitter_api, screen_name=None, user_id=None,
#                               friends_limit=maxint, followers_limit=maxint):
#     # Must have either screen_name or user_id (logical xor)
#     assert (screen_name != None) != (user_id != None), \
#         "Must have screen_name or user_id, but not both"
#
#     # See http://bit.ly/2GcjKJP and http://bit.ly/2rFz90N for details
#     # on API parameters
#
#     get_friends_ids = partial(make_twitter_request, twitter_api.friends.ids,
#                               count=5000)
#     get_followers_ids = partial(make_twitter_request, twitter_api.followers.ids,
#                                 count=5000)
#
#     friends_ids, followers_ids = [], []
#
#     for twitter_api_func, limit, ids, label in [
#         [get_friends_ids, friends_limit, friends_ids, "friends"],
#         [get_followers_ids, followers_limit, followers_ids, "followers"]
#     ]:
#
#         if limit == 0: continue
#
#         cursor = -1
#         while cursor != 0:
#
#             # Use make_twitter_request via the partially bound callable...
#             if screen_name:
#                 response = twitter_api_func(screen_name=screen_name, cursor=cursor)
#             else:  # user_id
#                 response = twitter_api_func(user_id=user_id, cursor=cursor)
#
#             if response is not None:
#                 ids += response['ids']
#                 cursor = response['next_cursor']
#
#             print('Fetched {0} total {1} ids for {2}'.format(len(ids), \
#                                                              label, (user_id or screen_name)), file=sys.stderr)
#
#             # XXX: You may want to store data during each iteration to provide an
#             # an additional layer of protection from exceptional circumstances
#
#             if len(ids) >= limit or response is None:
#                 break
#
#     # Do something useful with the IDs, like store them to disk...
#     return friends_ids[:friends_limit], followers_ids[:followers_limit]
#
# def setwise_friends_followers_analysis(screen_name, friends_ids, followers_ids):
#     friends_ids, followers_ids = set(friends_ids), set(followers_ids)
#     print('{0} is following {1}'.format(screen_name, len(friends_ids)))
#     print('{0} is being followed by {1}'.format(screen_name, len(followers_ids)))
#     print('{0} of {1} are not following {2} back'.format(
#         len(friends_ids.difference(followers_ids)),
#         len(friends_ids), screen_name))
#     print('{0} of {1} are not being followed back by {2}'.format(
#         len(followers_ids.difference(friends_ids)),
#         len(followers_ids), screen_name))
#     print('{0} has {1} mutual friends'.format(
#         screen_name, len(friends_ids.intersection(followers_ids))))

def get_nameID(screenName):
    try:
        screenName = int(screenName)
        user = json.loads(json.dumps(twitter_api.users.lookup(user_id=screenName), indent=4))
    except:
        name = screenName.replace(" ","")
        user = json.loads(json.dumps(twitter_api.users.lookup(screen_name=name), indent=4))
    user = user[0]
    name_id = (user["id"],user["name"])
    return name_id

def get_resp_friends(twitter_api, parent, depth, graph):
    if depth > 0:
        top_5 = find_top_5_frineds(twitter_api, parent[0])
        print("Parent:")
        print(parent)
        print("Top 5 Friends:")
        print(top_5)
        add_top_5(parent,top_5, graph)
        for i in top_5:
            get_resp_friends(twitter_api, i,depth-1,graph)

def find_top_5_frineds(twitter_api, user_id):
    friends = []
    num_followers = []
    names = []
    #TODO Make sure that the Top 5 are based on top Popular friends which is based on their followers_count
    try:
        following, followers = Chapter_9Twitter_Cookbook.get_friends_followers_ids(twitter_api, user_id=user_id, friends_limit=maxint, followers_limit=maxint)

        following = set(following)
        followers = set(followers)

        print("Following:", followers)
        print("Followers:", following)

        #followers = set(json.loads(json.dumps(twitter_api.followers.lookup(user_id=user_id), count=5000), indent=4))["ids"]
        #following = set(json.loads(json.dumps(twitter_api.friends.lookup(user_id=user_id), count=5000), indent=4))["ids"]
        reciprocal = followers.intersection(following)
        reciprocal = list(reciprocal)
        print("Reciprocals:", reciprocal)
        p = 0
        # reciprocal
        if len(reciprocal) < 15:
            num = len(reciprocal)
        else:
            num = 15
        for i in range(num):# used to be 15
            num_foll = json.loads(json.dumps(twitter_api.users.lookup(user_id=reciprocal[i]),indent = 4))
            num_foll = num_foll[0]
            num_followers.append(num_foll["followers_count"])
            names.append(num_foll["name"])
            print(p)
            p += 1

        print("Here")
        five_index = max_5_index(num_followers)

        try:
            for j in five_index:
                friends.append((reciprocal[j], names[j]))
        except:
            print("Unexpected error:", sys.exc_info())
        print("These are the friends:")
        print(friends)
        return friends
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return friends

def make_resp_tree(twitter_api,user_ID,depth):
    tree = networkx.nx.Graph()
    seed = get_nameID(user_ID)
    tree.add_node((seed[0],seed[1]))
    get_resp_friends(twitter_api,seed,depth,tree)
    return tree

def add_top_5(parent, children, graph):
    for i in children:
        graph.add_node((i[0],i[1]))
        graph.add_edge((parent[0], parent[1]), (i[0],i[1]))

def max_5_index(lister):
    indexes = []
    list = lister
    def looper (list, acc, num):
        if num >= 0:
            maxim = list[0]
            max_index = 0
            for i in range(len(list)):
                if(list[i]>maxim):
                    maxim = list[i]
                    max_index =i
            acc.append(max_index)
            list[max_index] = 0
            looper(list, acc, num-1)

    looper(list, indexes, 5)
    print("The indexes are:")
    print(indexes)
    return indexes

if __name__ == '__main__':
    twitter_api = oauth_login()
    #hamsterlanda
    #magicmathur3
    screenName = "hamsterlanda"
    tree = make_resp_tree(twitter_api,get_nameID(screenName)[0],2)
    string = screenName, "'s SociaL Network"
    networkx.nx.draw(tree, arrows = True, with_labels=1, label = string)
    print("Diameter of the tree:")
    print(networkx.nx.diameter(tree))
    print("Shortest Path Length:")
    print(networkx.nx.average_shortest_path_length(tree))
    #print(json.dumps(twitter_api.users.lookup(user_id=758093293397868544),indent =4) )
    plt.show()

    # screen_name = "magicmathur3"
    # friends_ids, followers_ids = get_friends_followers_ids(twitter_api,
    #                                                        screen_name="thisisibrahimd",
    #                                                        friends_limit=maxint,
    #                                                        followers_limit=maxint)
    # print("Following:", len(friends_ids))
    # print("Following:", friends_ids)
    # print("Followers:", len(followers_ids))
    # print("Followers:", followers_ids)
    #
    # friends = {friends_ids}
    # followers = {followers_ids}
    # print("Following:", friends)
    # print("Followers:", followers)

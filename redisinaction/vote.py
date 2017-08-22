SECONDS_IN_WEEK = 7 * 24 * 3600
VOTE_SCORE = 432

def article_vote(conn, user, article):
    cutoff = time.time() - SECONDS_IN_WEEK
    if conn.zscore('time:', article) < cutoff:
        return

    article_id = article.partition(':')[-1]
    if conn.sadd('voted:' + article_id, user):
        conn.zincrby('score:', article, VOTE_SCORE)
        conn.hincrby(article, 'votes:', 1)

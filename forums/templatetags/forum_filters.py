from django import template

register = template.Library()

@register.filter(name='get_num_posts')
def get_num_posts(threads):
    num_posts = 0
    for t in threads:
        num_posts += t.posts.count()

    return num_posts
